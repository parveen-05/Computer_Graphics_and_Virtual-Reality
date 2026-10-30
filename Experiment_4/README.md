# Experiment 3 – 2D Transformations using Homogeneous Coordinates

## Aim
To implement 2D transformations using homogeneous coordinate representation.

## Implemented operations
- Translation
- Rotation
- Scaling
- Reflection about X-axis
- Reflection about Y-axis
- Shearing

## How it works
A rectangle is represented by four vertices. Each vertex `(x, y)` is represented in homogeneous form as `(x, y, 1)`. A 3 × 3 transformation matrix is multiplied by each vertex. The original rectangle is shown with a gray dashed outline and the transformed rectangle in blue.

## Matrices
Translation: `[[1,0,tx],[0,1,ty],[0,0,1]]`

Rotation: `[[cosθ,-sinθ,0],[sinθ,cosθ,0],[0,0,1]]`

Scaling: `[[sx,0,0],[0,sy,0],[0,0,1]]`

Reflection X: `[[1,0,0],[0,-1,0],[0,0,1]]`

Reflection Y: `[[-1,0,0],[0,1,0],[0,0,1]]`

Shearing: `[[1,shx,0],[shy,1,0],[0,0,1]]`

## Run on macOS
```bash
cd ~/Downloads/CGVR_Experiment_03_2D_Transformations_FIXED
python3 main.py
```
Tkinter is used from Python's standard library; no pip packages are required if Tkinter is installed.

## Controls
- Translation: Parameter 1 = tx, Parameter 2 = ty
- Rotation: Parameter 1 = angle in degrees
- Scaling: Parameter 1 = sx, Parameter 2 = sy
- Shearing: Parameter 1 = shx, Parameter 2 = shy
- Reflection buttons apply reflection about the named axis.
- Use Reset before trying a new transformation to start from the original rectangle.

## Expected output
A GUI with a rectangle, axes, transformation buttons and parameter fields. Gray dashed outline shows the original rectangle; blue outline shows the transformed rectangle.

`output_preview.png` is illustrative, not a screenshot of an actual program run. Capture your own runtime screenshot for submission.

## Viva questions
1. What are 2D transformations?
2. Why are homogeneous coordinates used?
3. Why is a 3 × 3 matrix used for 2D homogeneous transformations?
4. What is translation?
5. What is the difference between rotation and scaling?
6. What is reflection?
7. What is shearing?

## Note
The lab manual specifies C++/OpenGL. This Python/Tkinter adaptation should be submitted only if your faculty accepts Python.
