import tkinter as tk
from tkinter import messagebox
import math

# EXPERIMENT 7: PHONG ILLUMINATION MODEL FOR A 3D OBJECT
# This program performs software shading of a sphere using the Phong model.

IMAGE_SIZE = 420
BACKGROUND = (245, 247, 250)


def clamp(value):
    return max(0.0, min(1.0, value))


def phong_shade(nx, ny, nz, lx, ly, lz, vx, vy, vz,
                ka, kd, ks, shininess, base_color):
    """Calculate RGB colour using ambient, diffuse and specular terms."""
    # Normalize normal, light and view vectors.
    n_len = math.sqrt(nx*nx + ny*ny + nz*nz)
    l_len = math.sqrt(lx*lx + ly*ly + lz*lz)
    v_len = math.sqrt(vx*vx + vy*vy + vz*vz)
    nx, ny, nz = nx/n_len, ny/n_len, nz/n_len
    lx, ly, lz = lx/l_len, ly/l_len, lz/l_len
    vx, vy, vz = vx/v_len, vy/v_len, vz/v_len

    # Ambient component.
    ambient = ka

    # Diffuse component: max(0, N dot L).
    ndotl = max(0.0, nx*lx + ny*ly + nz*lz)
    diffuse = kd * ndotl

    # Reflection vector R = 2(N dot L)N - L.
    rx = 2.0*ndotl*nx - lx
    ry = 2.0*ndotl*ny - ly
    rz = 2.0*ndotl*nz - lz
    r_len = math.sqrt(rx*rx + ry*ry + rz*rz)
    if r_len:
        rx, ry, rz = rx/r_len, ry/r_len, rz/r_len

    # Specular component: ks * max(0, R dot V)^shininess.
    rdotv = max(0.0, rx*vx + ry*vy + rz*vz)
    specular = ks * (rdotv ** shininess)

    intensity = clamp(ambient + diffuse + specular)
    return tuple(int(max(0, min(255, round(channel * intensity))))
                 for channel in base_color)


def render_phong_sphere(size, ka, kd, ks, shininess):
    """Create a shaded sphere image using per-pixel Phong illumination."""
    pixels = bytearray()
    radius = size * 0.43
    center = (size - 1) / 2.0

    # Directional light from upper-left/front and viewer looking along +Z.
    light = (-0.45, -0.55, 1.0)
    view = (0.0, 0.0, 1.0)
    base_color = (55, 135, 235)

    for py in range(size):
        for px in range(size):
            x = (px - center) / radius
            y = (center - py) / radius
            r2 = x*x + y*y

            if r2 <= 1.0:
                z = math.sqrt(1.0 - r2)
                color = phong_shade(
                    x, y, z, *light, *view,
                    ka, kd, ks, shininess, base_color
                )
                pixels.extend(color)
            else:
                pixels.extend(BACKGROUND)

    return bytes(pixels)


class PhongIlluminationApp:
    def __init__(self, root):
        self.root = root
        root.title("Experiment 7 - Phong Illumination Model")
        root.geometry("760x690")
        root.configure(bg="#f3f4f6")

        tk.Label(
            root, text="EXPERIMENT 7: PHONG ILLUMINATION MODEL",
            font=("Arial", 17, "bold"), bg="#f3f4f6", fg="#17365d"
        ).pack(pady=(14, 4))

        tk.Label(
            root,
            text="Per-pixel shading of a 3D sphere using ambient, diffuse and specular light",
            font=("Arial", 10), bg="#f3f4f6", fg="#374151"
        ).pack(pady=(0, 8))

        self.photo_label = tk.Label(root, bg="#f3f4f6")
        self.photo_label.pack(pady=8)

        controls = tk.LabelFrame(
            root, text="Phong illumination parameters",
            bg="#f3f4f6", padx=12, pady=8
        )
        controls.pack(padx=18, pady=8, fill="x")

        self.entries = {}
        settings = [
            ("Ambient coefficient (ka)", "ka", "0.20"),
            ("Diffuse coefficient (kd)", "kd", "0.70"),
            ("Specular coefficient (ks)", "ks", "0.60"),
            ("Shininess exponent", "shininess", "32")
        ]
        for i, (label, key, value) in enumerate(settings):
            row, col = divmod(i, 2)
            tk.Label(controls, text=label, bg="#f3f4f6").grid(
                row=row*2, column=col, sticky="w", padx=12, pady=(5, 0)
            )
            entry = tk.Entry(controls, width=12)
            entry.insert(0, value)
            entry.grid(row=row*2+1, column=col, sticky="w", padx=12, pady=(0, 5))
            self.entries[key] = entry

        tk.Button(
            root, text="Render with Phong Model", command=self.render,
            bg="#2563eb", fg="white", font=("Arial", 10, "bold"),
            padx=14, pady=7
        ).pack(pady=8)

        self.status = tk.Label(
            root, text="Default Phong shading displayed.",
            bg="#f3f4f6", fg="#374151", font=("Arial", 10)
        )
        self.status.pack(pady=5)

        self.render()

    def render(self):
        try:
            ka = float(self.entries["ka"].get())
            kd = float(self.entries["kd"].get())
            ks = float(self.entries["ks"].get())
            shininess = int(self.entries["shininess"].get())
            if not (0 <= ka <= 1 and 0 <= kd <= 1 and 0 <= ks <= 1):
                raise ValueError
            if not (1 <= shininess <= 256):
                raise ValueError
        except ValueError:
            messagebox.showerror(
                "Invalid parameters",
                "ka, kd and ks must be between 0 and 1. Shininess must be an integer from 1 to 256."
            )
            return

        rgb = render_phong_sphere(IMAGE_SIZE, ka, kd, ks, shininess)
        ppm = f"P6 {IMAGE_SIZE} {IMAGE_SIZE} 255 ".encode("ascii") + rgb
        self.photo = tk.PhotoImage(data=ppm, format="PPM")
        self.photo_label.configure(image=self.photo)

        self.status.config(
            text=f"Rendered sphere | ka={ka:g}, kd={kd:g}, ks={ks:g}, shininess={shininess}"
        )


if __name__ == "__main__":
    window = tk.Tk()
    app = PhongIlluminationApp(window)
    window.mainloop()
