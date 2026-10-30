# Experiment 2 – Midpoint Circle Drawing Algorithm

## Aim
To implement the Midpoint Circle Drawing Algorithm to generate a circle on a raster display.

## Objectives
- Understand the midpoint decision parameter used in circle generation.
- Use eight-way symmetry to reduce calculations.
- Plot the circle using raster points.

## Software / Tools
- Python 3
- Tkinter (Python standard GUI library)
- Python IDLE or macOS Terminal

## Algorithm
1. Read the radius `r` and choose the circle centre `(xc, yc)`.
2. Initialize `x = 0`, `y = r`, and decision parameter `p = 1 - r`.
3. Plot the eight symmetric points around the centre.
4. Increment `x`.
5. If `p < 0`, update `p = p + 2x + 1`.
6. Otherwise, decrement `y` and update `p = p + 2(x - y) + 1`.
7. Repeat while `x <= y`.

## How to Run on macOS
1. Extract this ZIP file.
2. Open Terminal and move into the extracted folder:
   ```bash
   cd ~/Downloads/CGVR_Experiment_02_Python_Midpoint_Circle
   ```
3. Run:
   ```bash
   python3 main.py
   ```
No pip installation is required if Tkinter is included in your Python installation.

## Test Case
- Radius: `100`
- Centre: `(410, 225)`

## Expected Output
A circular outline made from raster points appears on the canvas. The application displays the radius, centre, and number of unique raster points plotted.

`output_preview.png` is an illustrative preview, not a screenshot captured from your actual run. Capture your own application screenshot and save it as `output_screenshot.png` before submitting.

<img width="850" height="620" alt="output_preview" src="https://github.com/user-attachments/assets/48c6cc52-d341-4be7-99d2-f6526ea8bd33" />

