

import tkinter as tk
from tkinter import messagebox


class MidpointCircleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Experiment 2 - Midpoint Circle Drawing Algorithm")
        self.root.geometry("900x650")
        self.root.configure(bg="#f4f6f8")

        header = tk.Label(
            root, text="Midpoint Circle Drawing Algorithm",
            font=("Arial", 19, "bold"), bg="#f4f6f8", fg="#172554"
        )
        header.pack(pady=(14, 4))

        controls = tk.Frame(root, bg="#f4f6f8")
        controls.pack(pady=8)

        tk.Label(controls, text="Radius:", font=("Arial", 11), bg="#f4f6f8").grid(row=0, column=0, padx=5)
        self.radius_entry = tk.Entry(controls, width=8, font=("Arial", 11))
        self.radius_entry.insert(0, "100")
        self.radius_entry.grid(row=0, column=1, padx=5)

        tk.Button(
            controls, text="Draw Circle", command=self.draw_circle,
            bg="#2563eb", fg="white", font=("Arial", 10, "bold"),
            padx=12, pady=5
        ).grid(row=0, column=2, padx=8)

        tk.Button(
            controls, text="Clear", command=self.clear,
            font=("Arial", 10), padx=12, pady=5
        ).grid(row=0, column=3, padx=5)

        self.canvas = tk.Canvas(root, width=820, height=450, bg="white",
                                highlightthickness=1, highlightbackground="#cbd5e1")
        self.canvas.pack(pady=10)

        self.status = tk.Label(root, text="Enter a radius and click Draw Circle.",
                               font=("Arial", 10), bg="#f4f6f8", fg="#334155")
        self.status.pack(pady=4)

        self.draw_circle()

    def plot_symmetric_points(self, xc, yc, x, y, color="#2563eb"):
        points = [
            (xc + x, yc + y), (xc - x, yc + y),
            (xc + x, yc - y), (xc - x, yc - y),
            (xc + y, yc + x), (xc - y, yc + x),
            (xc + y, yc - x), (xc - y, yc - x)
        ]
        for px, py in points:
            self.canvas.create_rectangle(px, py, px + 1, py + 1,
                                         outline=color, fill=color)

    def draw_circle(self):
        try:
            radius = int(self.radius_entry.get())
            if radius <= 0 or radius > 200:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid radius", "Enter a whole-number radius from 1 to 200.")
            return

        self.canvas.delete("all")
        xc, yc = 410, 225

        # Draw coordinate axes and center point.
        self.canvas.create_line(20, yc, 800, yc, fill="#e2e8f0")
        self.canvas.create_line(xc, 15, xc, 435, fill="#e2e8f0")
        self.canvas.create_oval(xc - 3, yc - 3, xc + 3, yc + 3, fill="#dc2626", outline="")

        # Midpoint Circle Drawing Algorithm.
        x, y = 0, radius
        decision = 1 - radius
        plotted = set()

        while x <= y:
            for px, py in [
                (xc + x, yc + y), (xc - x, yc + y),
                (xc + x, yc - y), (xc - x, yc - y),
                (xc + y, yc + x), (xc - y, yc + x),
                (xc + y, yc - x), (xc - y, yc - x)
            ]:
                plotted.add((px, py))
            x += 1
            if decision < 0:
                decision += 2 * x + 1
            else:
                y -= 1
                decision += 2 * (x - y) + 1

        for px, py in plotted:
            self.canvas.create_rectangle(px, py, px + 1, py + 1,
                                         outline="#2563eb", fill="#2563eb")

        self.status.config(
            text=f"Radius = {radius} | Center = ({xc}, {yc}) | Unique raster points plotted = {len(plotted)}"
        )

    def clear(self):
        self.canvas.delete("all")
        self.status.config(text="Canvas cleared. Enter a radius and click Draw Circle.")


if __name__ == "__main__":
    root = tk.Tk()
    app = MidpointCircleApp(root)
    root.mainloop()
