# EXPERIMENT 7 – PHONG ILLUMINATION MODEL FOR A 3D OBJECT

## Aim
To implement the Phong illumination model for a 3D object.

## Software requirements
- Python 3
- Tkinter (Python standard GUI library)
- macOS Terminal or Python IDLE

## Theory
The Phong illumination model calculates the light intensity at a surface point by combining three components:

1. **Ambient reflection:** approximates general background light and provides a base level of illumination.
2. **Diffuse reflection:** models light scattered by a matte surface. It depends on the angle between the surface normal and the light direction.
3. **Specular reflection:** models the bright highlight seen on a shiny surface. It depends on the angle between the reflection direction and the viewer direction, raised to a shininess exponent.

The program evaluates these components for each visible pixel on a sphere and combines them to produce a shaded 3D appearance.

## Phong illumination equation
`I = ka × Ia + kd × Id × max(0, N·L) + ks × Is × max(0, R·V)^n`

Where:
- `ka`, `kd`, `ks` are ambient, diffuse and specular coefficients.
- `N` is the surface normal.
- `L` is the direction toward the light.
- `R` is the reflected light direction.
- `V` is the direction toward the viewer.
- `n` is the shininess exponent.

For this implementation, the light and view intensities are set to 1 and the output is clamped to the displayable colour range.

## Program operation
- A sphere is represented using a unit-sphere equation.
- For each pixel inside the projected circle, the program calculates the surface normal.
- It evaluates ambient, diffuse and specular terms using the Phong model.
- It displays the resulting RGB colour.
- The user can change `ka`, `kd`, `ks` and the shininess exponent and render again.

## Default parameters
- Ambient coefficient (`ka`) = 0.20
- Diffuse coefficient (`kd`) = 0.70
- Specular coefficient (`ks`) = 0.60
- Shininess exponent (`n`) = 32

## How to run on macOS
1. Extract the ZIP.
2. Open Terminal and run:
   ```bash
   cd ~/Downloads/CGVR_Experiment_07_Phong_Illumination_Model
   python3 main.py
   ```
No pip installation is required if Tkinter is included in your Python installation.

## Expected output
A blue shaded 3D sphere appears with ambient illumination, diffuse shading and a specular highlight. Changing the coefficients or shininess exponent changes the appearance of the sphere.

`output_preview.png` is an illustrative preview generated with the default parameters. It is not a screenshot captured from the live application. Capture your actual program window and save it as `output_screenshot.png` before submission.

<img width="760" height="560" alt="output_preview" src="https://github.com/user-attachments/assets/0776b10f-ef68-409b-a9f8-869ef0485eee" />

