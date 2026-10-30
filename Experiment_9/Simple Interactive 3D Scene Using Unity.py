import tkinter as tk
from tkinter import ttk
import math

class Interactive3DScene:
    """Interactive 3D-scene-style visualization using Tkinter (not Unity)."""
    def __init__(self, root):
        self.root=root
        root.title("Experiment 9 - Interactive 3D Scene")
        root.geometry("1100x720")
        root.minsize(850,580)
        self.rx=tk.DoubleVar(value=20)
        self.ry=tk.DoubleVar(value=-25)
        self.zoom=tk.DoubleVar(value=1.0)
        self.axes=tk.BooleanVar(value=True)
        self.wire=tk.BooleanVar(value=False)
        self.canvas=tk.Canvas(root,bg="#101827",highlightthickness=0)
        self.canvas.pack(side="left",fill="both",expand=True,padx=10,pady=10)
        self.canvas.bind("<Configure>",lambda e:self.draw())
        panel=ttk.Frame(root,padding=12,width=300)
        panel.pack(side="right",fill="y")
        panel.pack_propagate(False)
        ttk.Label(panel,text="INTERACTIVE 3D SCENE",font=("Arial",15,"bold")).pack(anchor="w")
        ttk.Label(panel,text="Rotate, zoom and inspect a simple scene.",wraplength=270).pack(anchor="w",pady=(4,12))
        for label,var,lo,hi in [("Rotate X",self.rx,-180,180),("Rotate Y",self.ry,-180,180),("Zoom",self.zoom,.55,1.8)]:
            ttk.Label(panel,text=label).pack(anchor="w",pady=(5,0))
            ttk.Scale(panel,from_=lo,to=hi,variable=var,command=lambda _:self.draw()).pack(fill="x")
        ttk.Checkbutton(panel,text="Show coordinate axes",variable=self.axes,command=self.draw).pack(anchor="w",pady=(12,2))
        ttk.Checkbutton(panel,text="Wireframe view",variable=self.wire,command=self.draw).pack(anchor="w",pady=2)
        ttk.Button(panel,text="Reset view",command=self.reset).pack(fill="x",pady=(12,8))
        ttk.Separator(panel).pack(fill="x",pady=8)
        ttk.Label(panel,text="Scene objects",font=("Arial",11,"bold")).pack(anchor="w")
        ttk.Label(panel,text="• Ground plane\\n• Central cube\\n• X, Y and Z axes\\n• Perspective-style camera",justify="left").pack(anchor="w",pady=5)
        ttk.Label(panel,text="Controls: use the sliders to rotate around X/Y and zoom in/out.",wraplength=270).pack(anchor="w",pady=(8,0))
        ttk.Label(panel,text="Manual note: the lab specifies Unity. This Tkinter project is a visual substitute, not a Unity scene or Unity build.",wraplength=270,foreground="#9a4b00").pack(anchor="w",pady=(14,0))
        self.draw()

    def reset(self):
        self.rx.set(20); self.ry.set(-25); self.zoom.set(1.0)
        self.axes.set(True); self.wire.set(False); self.draw()

    def project(self,p,w,h):
        x,y,z=p
        ax=math.radians(self.rx.get()); ay=math.radians(self.ry.get())
        y1=y*math.cos(ax)-z*math.sin(ax)
        z1=y*math.sin(ax)+z*math.cos(ax)
        x2=x*math.cos(ay)+z1*math.sin(ay)
        z2=-x*math.sin(ay)+z1*math.cos(ay)
        depth=z2+5.0
        scale=min(w,h)*.34*self.zoom.get()*(4.0/max(depth,1.0))
        return (w/2+x2*scale,h/2-y1*scale,depth)

    def line3d(self,p1,p2,color,width=2):
        w,h=self.canvas.winfo_width(),self.canvas.winfo_height()
        a=self.project(p1,w,h); b=self.project(p2,w,h)
        self.canvas.create_line(a[0],a[1],b[0],b[1],fill=color,width=width)

    def draw(self):
        c=self.canvas; c.delete("all")
        w,h=max(c.winfo_width(),1),max(c.winfo_height(),1)
        c.create_text(18,16,anchor="nw",text="3D SCENE VIEWPORT",fill="#dce7ff",font=("Arial",11,"bold"))
        for i in range(-5,6):
            self.line3d((i,-1.05,-5),(i,-1.05,5),"#29374d",1)
            self.line3d((-5,-1.05,i),(5,-1.05,i),"#29374d",1)
        v=[(-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1)]
        edges=[(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)]
        faces=[(0,1,2,3),(4,5,6,7),(0,1,5,4),(2,3,7,6),(1,2,6,5),(0,3,7,4)]
        q=[self.project(p,w,h) for p in v]
        if not self.wire.get():
            cols=["#385f91","#4479b5","#31577f","#294b70","#3b6fa8","#274765"]
            ordered=sorted(enumerate(faces),key=lambda item:sum(q[i][2] for i in item[1])/4,reverse=True)
            for fi,face in ordered:
                pts=[]
                for idx in face: pts.extend(q[idx][:2])
                c.create_polygon(*pts,fill=cols[fi],outline="#b9d5ff",width=2)
        else:
            for a,b in edges: c.create_line(*q[a][:2],*q[b][:2],fill="#9bc7ff",width=2)
        if self.axes.get():
            self.line3d((0,0,0),(2.2,0,0),"#ff6666",3)
            self.line3d((0,0,0),(0,2.2,0),"#65e39b",3)
            self.line3d((0,0,0),(0,0,2.2),"#6ea8ff",3)
        c.create_text(w/2,h-24,text="X axis: red     Y axis: green     Z axis: blue",fill="#dce7ff",font=("Arial",9))

if __name__=="__main__":
    root=tk.Tk()
    app=Interactive3DScene(root)
    root.mainloop()
