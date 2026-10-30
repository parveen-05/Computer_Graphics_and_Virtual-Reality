import tkinter as tk

# EXPERIMENT 6: Z-BUFFER ALGORITHM FOR HIDDEN SURFACE REMOVAL
# Smaller z values are treated as closer to the viewer.

WIDTH = 600
HEIGHT = 420
BACKGROUND = "#f8fafc"

# Each triangle is defined by three (x, y, z) vertices.
# The two triangles overlap on the screen and have different depth values.
TRIANGLES = [
    {
        "name": "Triangle A",
        "color": "#2563eb",
        "vertices": [(90, 65, 0.65), (510, 90, 0.65), (280, 365, 0.65)]
    },
    {
        "name": "Triangle B",
        "color": "#f97316",
        "vertices": [(170, 115, 0.30), (470, 130, 0.30), (325, 390, 0.30)]
    }
]


def edge(ax, ay, bx, by, px, py):
    return (px - ax) * (by - ay) - (py - ay) * (bx - ax)


def interpolate_depth(vertices, px, py):
    """Return interpolated z at (px, py), or None if outside the triangle."""
    (x1, y1, z1), (x2, y2, z2), (x3, y3, z3) = vertices
    area = edge(x1, y1, x2, y2, x3, y3)
    if area == 0:
        return None

    w1 = edge(x2, y2, x3, y3, px, py) / area
    w2 = edge(x3, y3, x1, y1, px, py) / area
    w3 = edge(x1, y1, x2, y2, px, py) / area

    epsilon = 1e-9
    if w1 < -epsilon or w2 < -epsilon or w3 < -epsilon:
        return None

    return w1 * z1 + w2 * z2 + w3 * z3


def run_z_buffer(width, height, triangles):
    """Rasterize triangles and retain the nearest fragment at every pixel."""
    z_buffer = [[float("inf") for _ in range(width)] for _ in range(height)]
    color_buffer = [[BACKGROUND for _ in range(width)] for _ in range(height)]

    for triangle in triangles:
        vertices = triangle["vertices"]
        xs = [v[0] for v in vertices]
        ys = [v[1] for v in vertices]
        min_x = max(0, int(min(xs)))
        max_x = min(width - 1, int(max(xs)) + 1)
        min_y = max(0, int(min(ys)))
        max_y = min(height - 1, int(max(ys)) + 1)

        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                z = interpolate_depth(vertices, x + 0.5, y + 0.5)
                if z is not None and z < z_buffer[y][x]:
                    z_buffer[y][x] = z
                    color_buffer[y][x] = triangle["color"]

    return z_buffer, color_buffer


class ZBufferDemo:
    def __init__(self, root):
        self.root = root
        root.title("Experiment 6 - Z-Buffer Hidden Surface Removal")
        root.geometry("900x650")
        root.configure(bg="#f3f4f6")

        tk.Label(
            root, text="EXPERIMENT 6: Z-BUFFER ALGORITHM",
            font=("Arial", 18, "bold"), bg="#f3f4f6", fg="#17365d"
        ).pack(pady=(14, 4))

        tk.Label(
            root,
            text="Hidden Surface Removal: the fragment with the smaller depth (z) is visible",
            font=("Arial", 10), bg="#f3f4f6", fg="#374151"
        ).pack(pady=(0, 10))

        self.canvas = tk.Canvas(
            root, width=WIDTH, height=HEIGHT, bg=BACKGROUND,
            highlightthickness=1, highlightbackground="#9ca3af"
        )
        self.canvas.pack(pady=8)

        info = tk.Frame(root, bg="#f3f4f6")
        info.pack(pady=6)
        tk.Label(info, text="Blue: Triangle A (z = 0.65)",
                 fg="#2563eb", bg="#f3f4f6",
                 font=("Arial", 10, "bold")).pack(side="left", padx=12)
        tk.Label(info, text="Orange: Triangle B (z = 0.30)",
                 fg="#ea580c", bg="#f3f4f6",
                 font=("Arial", 10, "bold")).pack(side="left", padx=12)

        self.status = tk.Label(
            root, text="", font=("Arial", 10),
            bg="#f3f4f6", fg="#374151"
        )
        self.status.pack(pady=5)

        tk.Button(
            root, text="Run Z-Buffer Again", command=self.render,
            font=("Arial", 10, "bold"), bg="#2563eb",
            fg="white", padx=12, pady=6
        ).pack(pady=5)

        self.render()

    def render(self):
        self.canvas.delete("all")
        z_buffer, color_buffer = run_z_buffer(WIDTH, HEIGHT, TRIANGLES)

        # Draw horizontal runs of equal color, reducing canvas drawing operations.
        for y, row in enumerate(color_buffer):
            x = 0
            while x < WIDTH:
                color = row[x]
                start = x
                while x + 1 < WIDTH and row[x + 1] == color:
                    x += 1
                if color != BACKGROUND:
                    self.canvas.create_rectangle(
                        start, y, x + 1, y + 1,
                        fill=color, outline=color
                    )
                x += 1

        # Draw triangle outlines to make the overlapping geometry clear.
        for triangle in TRIANGLES:
            coords = []
            for x, y, _z in triangle["vertices"]:
                coords.extend((x, y))
            coords.extend(coords[:2])
            self.canvas.create_line(*coords, fill="#111827", width=2)

        visible_pixels = sum(
            1 for row in color_buffer for color in row if color != BACKGROUND
        )
        orange_pixels = sum(
            1 for row in color_buffer for color in row if color == "#f97316"
        )
        blue_pixels = sum(
            1 for row in color_buffer for color in row if color == "#2563eb"
        )

        self.status.config(
            text=(f"Z-buffer completed | Visible raster pixels: {visible_pixels} | "
                  f"Triangle A visible: {blue_pixels} | Triangle B visible: {orange_pixels}")
        )


if __name__ == "__main__":
    window = tk.Tk()
    app = ZBufferDemo(window)
    window.mainloop()
