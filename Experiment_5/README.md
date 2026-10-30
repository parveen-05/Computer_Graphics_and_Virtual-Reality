# EXPERIMENT 5 – COHEN–SUTHERLAND LINE CLIPPING ALGORITHM

**Course:** Computer Graphics and Virtual Reality  
**Experiment number:** 5

## Aim
To implement the Cohen–Sutherland line clipping algorithm to clip a line segment against a rectangular clipping window.

## Software requirements
- Python 3
- Tkinter (Python standard GUI library)
- macOS Terminal or Python IDLE

## Theory / Working principle
The Cohen–Sutherland algorithm divides the 2D plane around a rectangular clipping window into nine regions. Each endpoint of a line segment receives a 4-bit region code:
- TOP: point is above the clipping window
- BOTTOM: point is below the clipping window
- RIGHT: point is to the right of the clipping window
- LEFT: point is to the left of the clipping window

The algorithm uses the region codes to decide whether a line can be accepted, rejected, or must be clipped.

### Cases
1. **Trivial acceptance:** both endpoint region codes are `0000`. The complete line is inside the clipping window.
2. **Trivial rejection:** the bitwise AND of the two endpoint codes is non-zero. The line is completely outside in a common region.
3. **Partial clipping:** otherwise, calculate the intersection of an outside endpoint with the relevant clipping-window boundary. Replace that endpoint, recalculate its region code, and repeat.

## Algorithm
1. Define the rectangular clipping window.
2. Calculate the 4-bit region code for each line endpoint.
3. If both region codes are zero, accept the line.
4. If the bitwise AND of the region codes is non-zero, reject the line.
5. Otherwise, select an endpoint that lies outside the window.
6. Calculate its intersection with the appropriate boundary: top, bottom, right, or left.
7. Replace the outside endpoint with the intersection point and recalculate its region code.
8. Repeat until the line is accepted or rejected.

## Program input / default test case
- First endpoint: `(70, 80)`
- Second endpoint: `(540, 350)`
- Clipping window: `xmin = 150`, `ymin = 100`, `xmax = 450`, `ymax = 300`

For this test case, the visible clipped segment is approximately `(150.0, 125.96)` to `(450.0, 298.34)`. The GUI displays the calculated coordinates.

## Expected output
The application displays:
- A green rectangular clipping window.
- The original line as a gray dashed line.
- The visible clipped line segment in blue.
- A result message with the clipped endpoint coordinates, or a rejection message if the line is completely outside.

`output_preview.png` is an illustrative preview of the expected output. It is not a screenshot captured from the running application. Capture your own program window and save it as `output_screenshot.png` for submission.

## How to run on macOS
1. Download and extract the ZIP.
2. Open Terminal and run:
   ```bash
   cd ~/Downloads/CGVR_Exp05_Cohen_Sutherland_FRESH
   python3 main.py
   ```
No pip installation is needed if Tkinter is included in your Python installation.

<img width="1050" height="650" alt="output_preview" src="https://github.com/user-attachments/assets/fcca720a-b1dd-44a7-915e-86a18e69b788" />

