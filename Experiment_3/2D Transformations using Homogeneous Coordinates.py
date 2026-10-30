import tkinter as tk
from tkinter import messagebox
import math

# EXPERIMENT 3: 2D TRANSFORMATIONS USING HOMOGENEOUS COORDINATES

class Transformations2D:
    def __init__(self, root):
        self.root = root
        root.title("Experiment 3 - 2D Transformations")
        root.geometry("1000x700")
        root.configure(bg="#f3f4f6")

        tk.Label(root, text="EXPERIMENT 3: 2D TRANSFORMATIONS",
                 font=("Arial", 18, "bold"), bg="#f3f4f6",
                 fg="#17365d").pack(pady=12)
        tk.Label(root, text="Translation | Rotation | Scaling | Reflection | Shearing",
                 font=("Arial", 11), bg="#f3f4f6").pack()

        controls = tk.Frame(root, bg="#f3f4f6")
        controls.pack(pady=12)

        tk.Label(controls, text="Parameter 1:", bg="#f3f4f6").grid(row=0, column=0, padx=4)
        self.a = tk.Entry(controls, width=8)
        self.a.insert(0, "50")
        self.a.grid(row=0, column=1, padx=4)

        tk.Label(controls, text="Parameter 2:", bg="#f3f4f6").grid(row=0, column=2, padx=4)
        self.b = tk.Entry(controls, width=8)
        self.b.insert(0, "30")
        self.b.grid(row=0, column=3, padx=4)

        buttons = tk.Frame(root, bg="#f3f4f6")
        buttons.pack(pady=5)
        for label, fn in [
            ("Translation", self.translation),
            ("Rotation", self.rotation),
            ("Scaling", self.scaling),
            ("Reflect X", self.reflect_x),
            ("Reflect Y", self.reflect_y),
            ("Shearing", self.shearing),
            ("Reset", self.reset)
        ]:
            tk.Button(buttons, text=label, command=fn, padx=8, pady=5).pack(side="left", padx=3)

        self.canvas = tk.Canvas(root, width=940, height=490, bg="white",
                                highlightthickness=1, highlightbackground="#9ca3af")
        self.canvas.pack(pady=12)
        self.status = tk.Label(root, text="Original shape: gray dashed. Transformed shape: blue.",
                               bg="#f3f4f6", font=("Arial", 10))
        self.status.pack()
        self.original = [(-80,-55), (80,-55), (80,55), (-80,55)]
        self.points = self.original[:]
        self.draw()

    def transform(self, m, label):
        new = []
        for x, y in self.points:
            v = (x, y, 1)
            nx = sum(m[0][i] * v[i] for i in range(3))
            ny = sum(m[1][i] * v[i] for i in range(3))
            new.append((nx, ny))
        self.points = new
        self.draw()
        self.status.config(text=label)

    def values(self):
        try:
            return float(self.a.get()), float(self.b.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Enter numeric values.")
            return None

    def translation(self):
        v = self.values()
        if v is None: return
        tx, ty = v
        self.transform([[1,0,tx],[0,1,ty],[0,0,1]], f"Translation: tx={tx:g}, ty={ty:g}")

    def rotation(self):
        v = self.values()
        if v is None: return
        angle = math.radians(v[0])
        c, s = math.cos(angle), math.sin(angle)
        self.transform([[c,-s,0],[s,c,0],[0,0,1]],
                       f"Rotation: {v[0]:g} degrees about origin")

    def scaling(self):
        v = self.values()
        if v is None: return
        sx, sy = v
        self.transform([[sx,0,0],[0,sy,0],[0,0,1]], f"Scaling: sx={sx:g}, sy={sy:g}")

    def reflect_x(self):
        self.transform([[1,0,0],[0,-1,0],[0,0,1]], "Reflection about X-axis")

    def reflect_y(self):
        self.transform([[-1,0,0],[0,1,0],[0,0,1]], "Reflection about Y-axis")

    def shearing(self):
        v = self.values()
        if v is None: return
        shx, shy = v
        self.transform([[1,shx,0],[shy,1,0],[0,0,1]],
                       f"Shearing: shx={shx:g}, shy={shy:g}")

    def reset(self):
        self.points = self.original[:]
        self.draw()
        self.status.config(text="Reset to original rectangle")

    def draw_polygon(self, pts, color, dashed=False):
        coords = []
        for x, y in pts:
            coords.extend((470+x, 245-y))
        self.canvas.create_polygon(*coords, fill="", outline=color, width=3,
                                   dash=(6,4) if dashed else ())

    def draw(self):
        self.canvas.delete("all")
        self.canvas.create_line(20,245,920,245,fill="#d1d5db")
        self.canvas.create_line(470,15,470,475,fill="#d1d5db")
        self.canvas.create_text(910,258,text="X",fill="#6b7280")
        self.canvas.create_text(482,20,text="Y",fill="#6b7280")
        self.draw_polygon(self.original, "#9ca3af", True)
        self.draw_polygon(self.points, "#2563eb")
        self.canvas.create_oval(466,241,474,249,fill="red",outline="red")
        self.canvas.create_text(85,25,anchor="w",
            text="Gray dashed = Original     Blue = Transformed", fill="#374151")

if __name__ == "__main__":
    app = tk.Tk()
    Transformations2D(app)
    app.mainloop()
