import tkinter as tk
from tkinter import messagebox
import math

# EXPERIMENT 4: COMPOSITE TRANSFORMATIONS USING MATRIX REPRESENTATION
# Column-vector convention is used: P' = T * R * S * P.
# Therefore scaling is applied first, then rotation, then translation.

class CompositeTransformApp:
    def __init__(self, root):
        self.root = root
        root.title("Experiment 4 - Composite Transformations")
        root.geometry("1050x760")
        root.configure(bg="#f3f4f6")

        tk.Label(root, text="EXPERIMENT 4: COMPOSITE TRANSFORMATIONS",
                 font=("Arial", 18, "bold"), bg="#f3f4f6",
                 fg="#17365d").pack(pady=(12, 3))
        tk.Label(root, text="Combined 2D transformation matrix: M = T × R × S",
                 font=("Arial", 11), bg="#f3f4f6", fg="#374151").pack()

        controls = tk.LabelFrame(root, text="Transformation parameters",
                                 font=("Arial", 11, "bold"), bg="#f3f4f6",
                                 padx=10, pady=8)
        controls.pack(padx=12, pady=10, fill="x")

        self.entries = {}
        fields = [
            ("Translate X (tx)", "tx", "80"),
            ("Translate Y (ty)", "ty", "40"),
            ("Rotate (degrees)", "angle", "30"),
            ("Scale X (sx)", "sx", "1.3"),
            ("Scale Y (sy)", "sy", "1.3"),
        ]
        for i, (label, key, default) in enumerate(fields):
            r, c = divmod(i, 3)
            tk.Label(controls, text=label, bg="#f3f4f6").grid(row=r*2, column=c, sticky="w", padx=10, pady=(3, 0))
            entry = tk.Entry(controls, width=12)
            entry.insert(0, default)
            entry.grid(row=r*2+1, column=c, sticky="w", padx=10, pady=(0, 5))
            self.entries[key] = entry

        actions = tk.Frame(root, bg="#f3f4f6")
        actions.pack(pady=4)
        tk.Button(actions, text="Apply Composite Transformation",
                  command=self.apply_composite, bg="#2563eb", fg="white",
                  font=("Arial", 10, "bold"), padx=12, pady=7).pack(side="left", padx=5)
        tk.Button(actions, text="Reset",
                  command=self.reset, font=("Arial", 10),
                  padx=18, pady=7).pack(side="left", padx=5)

        self.canvas = tk.Canvas(root, width=980, height=410, bg="white",
                                highlightthickness=1, highlightbackground="#9ca3af")
        self.canvas.pack(padx=12, pady=8)

        self.matrix_box = tk.Text(root, height=5, width=100, font=("Courier", 10),
                                  wrap="none", state="disabled")
        self.matrix_box.pack(padx=12, pady=5)

        self.status = tk.Label(root, text="Original shape is gray dashed; composite-transformed shape is blue.",
                               bg="#f3f4f6", fg="#374151", font=("Arial", 10))
        self.status.pack(pady=(2, 10))

        self.original = [(-65, -45), (65, -45), (65, 45), (-65, 45)]
        self.transformed = self.original[:]
        self.draw()

    @staticmethod
    def multiply(a, b):
        return [[sum(a[i][k] * b[k][j] for k in range(3))
                 for j in range(3)] for i in range(3)]

    @staticmethod
    def apply_to_point(m, point):
        x, y = point
        v = [x, y, 1]
        result = [sum(m[i][j] * v[j] for j in range(3)) for i in range(3)]
        return result[0], result[1]

    def get_parameters(self):
        try:
            return {key: float(entry.get()) for key, entry in self.entries.items()}
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter numeric values in all parameter fields.")
            return None

    def apply_composite(self):
        p = self.get_parameters()
        if p is None:
            return

        theta = math.radians(p["angle"])
        c, s = math.cos(theta), math.sin(theta)

        # Homogeneous transformation matrices.
        S = [
            [p["sx"], 0, 0],
            [0, p["sy"], 0],
            [0, 0, 1]
        ]
        R = [
            [c, -s, 0],
            [s, c, 0],
            [0, 0, 1]
        ]
        T = [
            [1, 0, p["tx"]],
            [0, 1, p["ty"]],
            [0, 0, 1]
        ]

        # For column vectors, M = T * R * S.
        composite = self.multiply(T, self.multiply(R, S))
        self.transformed = [self.apply_to_point(composite, pt) for pt in self.original]

        self.show_matrix(composite)
        self.draw()
        self.status.config(
            text=f"Composite applied in order: Scaling → Rotation ({p['angle']:g}°) → Translation."
        )

    def show_matrix(self, matrix):
        lines = ["Composite matrix M = T × R × S",
                 "[ " + "  ".join(f"{v:9.3f}" for v in row) + " ]" for row in matrix]
        self.matrix_box.config(state="normal")
        self.matrix_box.delete("1.0", "end")
        self.matrix_box.insert("1.0", "\n".join(lines))
        self.matrix_box.config(state="disabled")

    def reset(self):
        self.transformed = self.original[:]
        self.matrix_box.config(state="normal")
        self.matrix_box.delete("1.0", "end")
        self.matrix_box.config(state="disabled")
        self.status.config(text="Reset to original rectangle. Enter values and apply the composite transformation.")
        self.draw()

    def canvas_points(self, points):
        return [(490 + x, 205 - y) for x, y in points]

    def draw_polygon(self, points, color, dashed=False):
        coords = []
        for x, y in self.canvas_points(points):
            coords.extend((x, y))
        self.canvas.create_polygon(*coords, fill="", outline=color, width=3,
                                    dash=(7, 4) if dashed else ())

    def draw(self):
        self.canvas.delete("all")
        self.canvas.create_line(20, 205, 960, 205, fill="#d1d5db")
        self.canvas.create_line(490, 15, 490, 395, fill="#d1d5db")
        self.canvas.create_text(950, 218, text="X", fill="#6b7280")
        self.canvas.create_text(502, 20, text="Y", fill="#6b7280")
        self.canvas.create_oval(486, 201, 494, 209, fill="red", outline="red")
        self.draw_polygon(self.original, "#9ca3af", True)
        self.draw_polygon(self.transformed, "#2563eb")
        self.canvas.create_text(35, 25, anchor="w",
                                text="Gray dashed: Original    Blue: Composite transformed",
                                fill="#374151", font=("Arial", 10, "bold"))

if __name__ == "__main__":
    window = tk.Tk()
    app = CompositeTransformApp(window)
    window.mainloop()
