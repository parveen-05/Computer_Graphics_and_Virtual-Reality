import tkinter as tk
from tkinter import ttk, messagebox

class ShaderPipelineDemo:
    """Educational Tkinter simulation of the vertex/fragment shader pipeline.
    This is not an actual OpenGL/GLSL renderer.
    """
    def __init__(self, root):
        self.root = root
        root.title("Experiment 8 - Vertex and Fragment Shader Pipeline")
        root.geometry("1120x720")
        root.minsize(900, 620)
        self.mode = tk.StringVar(value="gradient")
        self.animate = False

        header = ttk.Frame(root, padding=12)
        header.pack(fill="x")
        ttk.Label(header, text="VERTEX + FRAGMENT SHADER PIPELINE",
                  font=("Arial", 17, "bold")).pack(anchor="w")
        ttk.Label(header, text="Interactive software demonstration of the stages used by a basic OpenGL shader program",
                  font=("Arial", 10)).pack(anchor="w", pady=(4, 0))

        body = ttk.Frame(root, padding=(12, 4, 12, 12))
        body.pack(fill="both", expand=True)
        left = ttk.Frame(body)
        left.pack(side="left", fill="both", expand=True)
        right = ttk.Frame(body, width=350)
        right.pack(side="right", fill="y", padx=(12, 0))
        right.pack_propagate(False)

        self.canvas = tk.Canvas(left, bg="#151b2b", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<Configure>", lambda e: self.draw_scene())

        ttk.Label(right, text="Fragment shading mode", font=("Arial", 11, "bold")).pack(anchor="w")
        for label, value in [("Interpolated colour gradient", "gradient"),
                             ("Flat colour", "flat"),
                             ("Grayscale", "gray")]:
            ttk.Radiobutton(right, text=label, variable=self.mode, value=value,
                            command=self.draw_scene).pack(anchor="w", pady=3)

        ttk.Separator(right).pack(fill="x", pady=12)
        ttk.Label(right, text="Shader pipeline", font=("Arial", 11, "bold")).pack(anchor="w")
        stages = [
            ("1. Vertex shader", "Processes each vertex; transforms its position and assigns an output colour."),
            ("2. Primitive assembly", "Connects processed vertices to form a triangle."),
            ("3. Rasterization", "Finds the screen pixels covered by the triangle."),
            ("4. Fragment shader", "Runs for fragments and calculates the final fragment colour."),
        ]
        for title, desc in stages:
            ttk.Label(right, text=title, font=("Arial", 9, "bold")).pack(anchor="w", pady=(7, 0))
            ttk.Label(right, text=desc, wraplength=320, justify="left").pack(anchor="w")

        ttk.Separator(right).pack(fill="x", pady=12)
        ttk.Label(right, text="Example GLSL snippets", font=("Arial", 11, "bold")).pack(anchor="w")
        self.code = tk.Text(right, height=12, width=42, font=("Courier", 8),
                            bg="#101522", fg="#dce7ff", insertbackground="white",
                            relief="flat", wrap="word")
        self.code.pack(fill="x", pady=(5, 0))
        self.update_code()
        self.mode.trace_add("write", lambda *_: self.update_code())

        ttk.Button(right, text="Redraw scene", command=self.draw_scene).pack(fill="x", pady=(12, 4))
        ttk.Label(right, text="Note: This Python/Tkinter project illustrates the shader stages. It does not compile or execute GLSL or create an OpenGL context.",
                  wraplength=320, foreground="#9a4b00", justify="left").pack(anchor="w", pady=(8, 0))

    def update_code(self):
        mode = self.mode.get()
        if mode == "gradient":
            frag = "outColor = vec4(vertexColor, 1.0);"
        elif mode == "flat":
            frag = "outColor = vec4(0.20, 0.75, 0.95, 1.0);"
        else:
            frag = "float g = dot(vertexColor, vec3(0.299,0.587,0.114));\\noutColor = vec4(vec3(g), 1.0);"
        source = """// Vertex shader (illustrative GLSL)
#version 330 core
layout(location=0) in vec3 position;
layout(location=1) in vec3 color;
out vec3 vertexColor;
void main() {
    gl_Position = vec4(position, 1.0);
    vertexColor = color;
}

// Fragment shader (illustrative GLSL)
#version 330 core
in vec3 vertexColor;
out vec4 outColor;
void main() {
    %s
}""" % frag
        self.code.delete("1.0", "end")
        self.code.insert("1.0", source)

    def draw_scene(self):
        c = self.canvas
        c.delete("all")
        w, h = max(c.winfo_width(), 1), max(c.winfo_height(), 1)
        c.create_text(22, 20, anchor="nw", text="SIMULATED SHADER OUTPUT",
                      fill="#dce7ff", font=("Arial", 11, "bold"))
        # Triangle coordinates and barycentric interpolation
        p1 = (w * .50, h * .18)
        p2 = (w * .19, h * .78)
        p3 = (w * .81, h * .78)
        colors = [(255, 75, 90), (60, 220, 150), (75, 135, 255)]
        mode = self.mode.get()
        minx, maxx = int(min(p[0] for p in [p1,p2,p3])), int(max(p[0] for p in [p1,p2,p3]))
        miny, maxy = int(min(p[1] for p in [p1,p2,p3])), int(max(p[1] for p in [p1,p2,p3]))
        # Pixel-cell rendering makes the rasterization stage visible.
        step = 3
        denom = ((p2[1]-p3[1])*(p1[0]-p3[0]) + (p3[0]-p2[0])*(p1[1]-p3[1]))
        for y in range(miny, maxy, step):
            for x in range(minx, maxx, step):
                a = ((p2[1]-p3[1])*(x-p3[0]) + (p3[0]-p2[0])*(y-p3[1])) / denom
                b = ((p3[1]-p1[1])*(x-p3[0]) + (p1[0]-p3[0])*(y-p3[1])) / denom
                d = 1 - a - b
                if a >= 0 and b >= 0 and d >= 0:
                    if mode == "flat":
                        col = (51, 191, 242)
                    else:
                        vals = [a*colors[0][i] + b*colors[1][i] + d*colors[2][i] for i in range(3)]
                        if mode == "gray":
                            g = int(.299*vals[0] + .587*vals[1] + .114*vals[2])
                            col = (g,g,g)
                        else:
                            col = tuple(int(v) for v in vals)
                    c.create_rectangle(x, y, x+step, y+step, fill="#%02x%02x%02x" % col, outline="")
        for idx, (p, color) in enumerate(zip([p1,p2,p3], ["#ff4b5a","#3cdc96","#4b87ff"]), 1):
            x,y=p
            c.create_oval(x-7,y-7,x+7,y+7,fill=color,outline="white",width=2)
            c.create_text(x, y-20, text=f"Vertex {idx}", fill="white", font=("Arial", 9, "bold"))
        c.create_text(w/2, h*.88, text="Vertex attributes are interpolated across the triangle; the fragment stage selects the pixel colour.",
                      fill="#dce7ff", font=("Arial", 9), width=w*.85)
        c.create_text(w/2, h*.94, text=f"Current fragment mode: {mode.upper()}",
                      fill="#9fb4dc", font=("Arial", 9, "bold"))

if __name__ == "__main__":
    root = tk.Tk()
    app = ShaderPipelineDemo(root)
    root.mainloop()
