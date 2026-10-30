import tkinter as tk
from tkinter import messagebox

# EXPERIMENT 5: COHEN-SUTHERLAND LINE CLIPPING ALGORITHM

INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8


def compute_code(x, y, xmin, ymin, xmax, ymax):
    """Return the 4-bit region code for point (x, y)."""
    code = INSIDE
    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT
    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP
    return code


def cohen_sutherland_clip(x1, y1, x2, y2, xmin, ymin, xmax, ymax):
    """Clip a line segment against a rectangular clipping window."""
    code1 = compute_code(x1, y1, xmin, ymin, xmax, ymax)
    code2 = compute_code(x2, y2, xmin, ymin, xmax, ymax)

    while True:
        # Trivial acceptance: both endpoints are inside.
        if code1 == 0 and code2 == 0:
            return (x1, y1, x2, y2)

        # Trivial rejection: both endpoints share an outside region.
        if code1 & code2:
            return None

        # Choose one endpoint that is outside the clipping window.
        out_code = code1 if code1 != 0 else code2

        if out_code & TOP:
            if y2 == y1:
                return None
            x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
            y = ymax
        elif out_code & BOTTOM:
            if y2 == y1:
                return None
            x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
            y = ymin
        elif out_code & RIGHT:
            if x2 == x1:
                return None
            y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
            x = xmax
        else:  # LEFT
            if x2 == x1:
                return None
            y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
            x = xmin

        # Replace the endpoint that was outside and calculate its new code.
        if out_code == code1:
            x1, y1 = x, y
            code1 = compute_code(x1, y1, xmin, ymin, xmax, ymax)
        else:
            x2, y2 = x, y
            code2 = compute_code(x2, y2, xmin, ymin, xmax, ymax)


class LineClippingApp:
    def __init__(self, root):
        self.root = root
        root.title("Experiment 5 - Cohen-Sutherland Line Clipping")
        root.geometry("1050x760")
        root.configure(bg="#f3f4f6")

        tk.Label(
            root, text="EXPERIMENT 5: COHEN-SUTHERLAND LINE CLIPPING",
            font=("Arial", 17, "bold"), bg="#f3f4f6", fg="#17365d"
        ).pack(pady=(12, 4))

        tk.Label(
            root, text="Enter line endpoints in canvas coordinates (0 to 600, 0 to 400)",
            font=("Arial", 10), bg="#f3f4f6", fg="#374151"
        ).pack()

        controls = tk.LabelFrame(root, text="Line endpoint coordinates",
                                 bg="#f3f4f6", padx=10, pady=8)
        controls.pack(pady=10)

        defaults = [("x1", "70"), ("y1", "80"), ("x2", "540"), ("y2", "350")]
        self.entries = {}
        for i, (name, value) in enumerate(defaults):
            tk.Label(controls, text=name + ":", bg="#f3f4f6").grid(row=0, column=i*2, padx=4)
            entry = tk.Entry(controls, width=8)
            entry.insert(0, value)
            entry.grid(row=0, column=i*2+1, padx=4)
            self.entries[name] = entry

        buttons = tk.Frame(root, bg="#f3f4f6")
        buttons.pack(pady=3)
        tk.Button(buttons, text="Clip Line", command=self.clip_line,
                  bg="#2563eb", fg="white", font=("Arial", 10, "bold"),
                  padx=14, pady=6).pack(side="left", padx=5)
        tk.Button(buttons, text="Reset Example", command=self.reset_example,
                  padx=12, pady=6).pack(side="left", padx=5)

        self.canvas = tk.Canvas(root, width=800, height=500, bg="white",
                                highlightthickness=1, highlightbackground="#9ca3af")
        self.canvas.pack(pady=10)

        self.result = tk.Label(root, text="The rectangle is the clipping window. Click Clip Line.",
                               bg="#f3f4f6", fg="#374151", font=("Arial", 10))
        self.result.pack(pady=4)
        self.draw_scene()

    def get_values(self):
        try:
            values = [float(self.entries[k].get()) for k in ("x1", "y1", "x2", "y2")]
        except ValueError:
            messagebox.showerror("Invalid input", "Enter numeric values for x1, y1, x2 and y2.")
            return None
        if any(v < 0 or v > 600 for v in values[0::2]) or any(v < 0 or v > 400 for v in values[1::2]):
            messagebox.showerror("Out of range", "Use x values from 0 to 600 and y values from 0 to 400.")
            return None
        return values

    def canvas_point(self, x, y):
        # Map algorithm coordinates (0..600, 0..400) to canvas coordinates.
        return 100 + x, 60 + (400 - y)

    def draw_line(self, p1, p2, color, width=3, dash=None):
        x1, y1 = self.canvas_point(*p1)
        x2, y2 = self.canvas_point(*p2)
        self.canvas.create_line(x1, y1, x2, y2, fill=color, width=width, dash=dash)

    def draw_scene(self):
        self.canvas.delete("all")
        # Draw coordinate grid and axes.
        for x in range(0, 601, 50):
            sx, _ = self.canvas_point(x, 0)
            self.canvas.create_line(sx, 60, sx, 460, fill="#eef2f7")
            self.canvas.create_text(sx, 475, text=str(x), fill="#64748b", font=("Arial", 8))
        for y in range(0, 401, 50):
            _, sy = self.canvas_point(0, y)
            self.canvas.create_line(100, sy, 700, sy, fill="#eef2f7")
            self.canvas.create_text(82, sy, text=str(y), fill="#64748b", font=("Arial", 8))

        xmin, ymin, xmax, ymax = 150, 100, 450, 300
        left, bottom = self.canvas_point(xmin, ymin)
        right, top = self.canvas_point(xmax, ymax)
        self.canvas.create_rectangle(left, top, right, bottom,
                                     outline="#16a34a", width=3)
        self.canvas.create_text((left+right)/2, top-14,
                                text="CLIPPING WINDOW", fill="#15803d",
                                font=("Arial", 9, "bold"))
        self.canvas.create_text(710, 60, anchor="nw",
                                text="Green: clipping window\nGray dashed: original line\nBlue: visible clipped segment",
                                fill="#374151", font=("Arial", 9))

    def clip_line(self):
        values = self.get_values()
        if values is None:
            return
        x1, y1, x2, y2 = values
        xmin, ymin, xmax, ymax = 150, 100, 450, 300

        self.draw_scene()
        self.draw_line((x1, y1), (x2, y2), "#9ca3af", 3, (7, 4))

        clipped = cohen_sutherland_clip(x1, y1, x2, y2, xmin, ymin, xmax, ymax)
        if clipped is None:
            self.result.config(text="Result: Line rejected — it lies completely outside the clipping window.")
        else:
            cx1, cy1, cx2, cy2 = clipped
            self.draw_line((cx1, cy1), (cx2, cy2), "#2563eb", 4)
            self.result.config(
                text=f"Result: Line accepted after clipping. Visible segment: ({cx1:.1f}, {cy1:.1f}) to ({cx2:.1f}, {cy2:.1f})."
            )

    def reset_example(self):
        for key, value in {"x1":"70", "y1":"80", "x2":"540", "y2":"350"}.items():
            self.entries[key].delete(0, "end")
            self.entries[key].insert(0, value)
        self.draw_scene()
        self.result.config(text="Default line restored. Click Clip Line to see the clipped segment.")


if __name__ == "__main__":
    window = tk.Tk()
    app = LineClippingApp(window)
    window.mainloop()
