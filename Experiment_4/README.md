# Experiment 4 – Composite Transformations using Matrix Representation

## Aim
To implement composite 2D transformations using matrix representation.

## Description
This program combines scaling, rotation, and translation into one 3 × 3 homogeneous transformation matrix. It uses column vectors and the multiplication order:

`M = T × R × S`

The rightmost matrix acts first, so the object is scaled first, then rotated, and finally translated.

## Matrices
Scaling:

`S = [[sx, 0, 0], [0, sy, 0], [0, 0, 1]]`

Rotation:

`R = [[cosθ, -sinθ, 0], [sinθ, cosθ, 0], [0, 0, 1]]`

Translation:

`T = [[1, 0, tx], [0, 1, ty], [0, 0, 1]]`

Composite matrix:

`M = T × R × S`

Each vertex is transformed using `P' = M × P`, where `P = [x, y, 1]ᵀ`.

## How to run on macOS
1. Extract the ZIP.
2. In Terminal:
   ```bash
   cd ~/Downloads/CGVR_Experiment_04_Composite_Transformations
   python3 main.py
   ```
Tkinter is part of the Python standard library when included in the installation. No pip packages are required.

## Default test values
- Translation X = 80
- Translation Y = 40
- Rotation = 30 degrees
- Scale X = 1.3
- Scale Y = 1.3

Click **Apply Composite Transformation**. The original rectangle is shown with a gray dashed outline; the composite-transformed rectangle is blue. The combined 3 × 3 matrix is displayed below the canvas. Click **Reset** to restore the original shape.

## Viva questions
1. What is a composite transformation?
2. Why are homogeneous coordinates used?
3. What is the order of matrix multiplication for this program?
4. Why does the rightmost matrix act first for column vectors?
5. What is the difference between individual and composite transformations?
6. Can changing the order of transformations change the result?
7. What is the size of a 2D homogeneous transformation matrix?

## Output image note
`output_preview.png` is an illustrative preview of the expected application output, not a screenshot captured from a live run. Capture your own runtime screenshot as `output_screenshot.png` before submission.

## Submission note
The lab manual specifies C++/OpenGL. This Python/Tkinter adaptation should be submitted only if your faculty accepts Python implementations.
