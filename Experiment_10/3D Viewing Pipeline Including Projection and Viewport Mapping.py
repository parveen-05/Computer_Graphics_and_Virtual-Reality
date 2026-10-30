import tkinter as tk
from tkinter import ttk
import math

class ViewingPipelineDemo:
    """Interactive educational demonstration of 3D viewing and viewport mapping."""
    def __init__(self,root):
        self.root=root
        root.title("Experiment 10 - 3D Viewing Pipeline")
        root.geometry("1120x720")
        root.minsize(900,600)
        self.projection=tk.StringVar(value="Perspective")
        self.angle=tk.DoubleVar(value=25)
        self.zoom=tk.DoubleVar(value=1.0)
        self.viewport_scale=tk.DoubleVar(value=1.0)

        main=ttk.Frame(root,padding=10); main.pack(fill="both",expand=True)
        self.canvas=tk.Canvas(main,bg="#101827",highlightthickness=0)
        self.canvas.pack(side="left",fill="both",expand=True)
        self.canvas.bind("<Configure>",lambda e:self.draw())
        panel=ttk.Frame(main,width=310,padding=10); panel.pack(side="right",fill="y")
        panel.pack_propagate(False)

        ttk.Label(panel,text="3D VIEWING PIPELINE",font=("Arial",15,"bold")).pack(anchor="w")
        ttk.Label(panel,text="Explore projection and viewport mapping.",wraplength=280).pack(anchor="w",pady=(4,12))
        ttk.Label(panel,text="Projection type").pack(anchor="w")
        ttk.Radiobutton(panel,text="Perspective projection",variable=self.projection,value="Perspective",command=self.draw).pack(anchor="w")
        ttk.Radiobutton(panel,text="Orthographic projection",variable=self.projection,value="Orthographic",command=self.draw).pack(anchor="w",pady=(0,8))

        ttk.Label(panel,text="Object rotation").pack(anchor="w")
        ttk.Scale(panel,from_=-60,to=60,variable=self.angle,command=lambda _:self.draw()).pack(fill="x")
        ttk.Label(panel,text="Camera zoom").pack(anchor="w",pady=(8,0))
        ttk.Scale(panel,from_=.6,to=1.6,variable=self.zoom,command=lambda _:self.draw()).pack(fill="x")
        ttk.Label(panel,text="Viewport scale").pack(anchor="w",pady=(8,0))
        ttk.Scale(panel,from_=.5,to=1.3,variable=self.viewport_scale,command=lambda _:self.draw()).pack(fill="x")
        ttk.Button(panel,text="Reset",command=self.reset).pack(fill="x",pady=12)

        ttk.Separator(panel).pack(fill="x",pady=8)
        ttk.Label(panel,text="Pipeline stages",font=("Arial",11,"bold")).pack(anchor="w")
        stages=[
            "1. Model coordinates: define object vertices.",
            "2. View transformation: position the scene relative to the camera.",
            "3. Projection: map 3D coordinates to a 2D projection plane.",
            "4. Viewport mapping: map projected coordinates to screen pixels."
        ]
        for item in stages:
            ttk.Label(panel,text=item,wraplength=280,justify="left").pack(anchor="w",pady=4)
        ttk.Label(panel,text="Manual note: this is a Python visualization of the pipeline, not an OpenGL implementation.",wraplength=280,foreground="#9a4b00").pack(anchor="w",pady=(12,0))
        self.draw()

    def reset(self):
        self.projection.set("Perspective"); self.angle.set(25)
        self.zoom.set(1.0); self.viewport_scale.set(1.0); self.draw()

    def transform(self,p):
        x,y,z=p
        a=math.radians(self.angle.get())
        xr=x*math.cos(a)+z*math.sin(a)
        zr=-x*math.sin(a)+z*math.cos(a)
        # A fixed illustrative camera/view transform.
        yr=y*math.cos(math.radians(18))-zr*math.sin(math.radians(18))
        zr2=y*math.sin(math.radians(18))+zr*math.cos(math.radians(18))
        return xr,yr,zr2

    def project_to_canvas(self,p,w,h):
        x,y,z=self.transform(p)
        scale=min(w,h)*.27*self.zoom.get()*self.viewport_scale.get()
        if self.projection.get()=="Perspective":
            factor=4.5/max(4.5+z,1.0)
            sx=w/2+x*scale*factor
            sy=h/2-y*scale*factor
        else:
            sx=w/2+x*scale
            sy=h/2-y*scale
        return sx,sy

    def draw(self):
        c=self.canvas; c.delete("all")
        w,h=max(c.winfo_width(),1),max(c.winfo_height(),1)
        c.create_text(18,16,anchor="nw",text="3D WORLD → 2D VIEWPORT",fill="#dce7ff",font=("Arial",11,"bold"))
        # A small 3D grid on the ground plane.
        for i in range(-4,5):
            p1=self.project_to_canvas((i,-1.2,-4),w,h)
            p2=self.project_to_canvas((i,-1.2,4),w,h)
            q1=self.project_to_canvas((-4,-1.2,i),w,h)
            q2=self.project_to_canvas((4,-1.2,i),w,h)
            c.create_line(*p1,*p2,fill="#29374d",width=1)
            c.create_line(*q1,*q2,fill="#29374d",width=1)

        verts=[(-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),
               (-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1)]
        faces=[(0,1,2,3),(4,5,6,7),(0,1,5,4),(2,3,7,6),(1,2,6,5),(0,3,7,4)]
        edges=[(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)]
        pts=[self.project_to_canvas(v,w,h) for v in verts]
        cols=["#385f91","#4479b5","#31577f","#294b70","#3b6fa8","#274765"]
        # Depth-sort faces for a simple painter-style illustration.
        depth_faces=[]
        for fi,face in enumerate(faces):
            depth=sum(self.transform(verts[i])[2] for i in face)/4
            depth_faces.append((depth,fi,face))
        for _,fi,face in sorted(depth_faces,reverse=True):
            coords=[]
            for idx in face: coords.extend(pts[idx])
            c.create_polygon(*coords,fill=cols[fi],outline="#b9d5ff",width=2)

        # Screen viewport frame shows the final mapped region.
        margin=35
        c.create_rectangle(margin,margin,w-margin,h-margin,outline="#8ba4c8",dash=(5,4),width=1)
        label=f"Projection: {self.projection.get()}   |   Viewport scale: {self.viewport_scale.get():.2f}"
        c.create_text(w/2,h-16,text=label,fill="#dce7ff",font=("Arial",9))
        c.create_text(w-18,18,anchor="ne",text="Dashed rectangle = viewport boundary",fill="#9fb4dc",font=("Arial",8))

if __name__=="__main__":
    root=tk.Tk()
    app=ViewingPipelineDemo(root)
    root.mainloop()
