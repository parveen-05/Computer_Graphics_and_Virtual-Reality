# EXPERIMENT 6 – Z-BUFFER ALGORITHM FOR HIDDEN SURFACE REMOVAL

## Aim
To implement the Z-buffer algorithm for hidden surface removal.

## Software requirements
- Python 3
- Tkinter (Python standard GUI library)
- macOS Terminal or Python IDLE

## Theory
The Z-buffer algorithm is a visible-surface detection technique used to determine which surfaces are visible and which are hidden when multiple 3D surfaces project onto the same screen location.

A depth value (z value) is stored for every pixel in a depth buffer. When a new surface fragment reaches a pixel, its depth is compared with the stored depth:
- If the new fragment is closer to the viewer, its depth and colour replace the stored values.
- Otherwise, the fragment is hidden and the stored values remain unchanged.

**Convention used in this program:** smaller z values represent points closer to the viewer.

## Algorithm
1. Initialize every Z-buffer entry to infinity.
2. Initialize the colour buffer with the background colour.
3. Process each triangle.
4. Find the screen-space bounding box of the triangle.
5. For each pixel in that bounding box, test whether the pixel lies inside the triangle.
6. Interpolate the triangle's depth at that pixel.
7. Compare the new depth with the stored Z-buffer value.
8. If the new depth is smaller, update both the Z-buffer and colour buffer.
9. Display the final colour buffer. Only the nearest surface remains visible at each pixel.

## Scene used
The program rasterizes two overlapping triangles:
- Triangle A: blue, depth `z = 0.65`
- Triangle B: orange, depth `z = 0.30`

Since smaller z is closer, Triangle B appears in front wherever the two triangles overlap. The visible portions of Triangle A remain blue.

## How to run on macOS
1. Extract the ZIP file.
2. Open Terminal and run:
   ```bash
   cd ~/Downloads/CGVR_Experiment_06_Z_Buffer_Hidden_Surface_Removal
   python3 main.py
   ```
No pip installation is required if Tkinter is included in your Python installation.

## Expected output
A GUI displays two overlapping filled triangles. The blue triangle is partially hidden by the orange triangle in the overlap region. The status line reports the number of visible raster pixels for each triangle.

`output_preview.png` is an illustrative preview of the expected Z-buffer result, not a screenshot captured from a live run. Capture your actual program window and save it as `output_screenshot.png` before submission.

## Viva questions
1. What is hidden surface removal?
2. What is the Z-buffer algorithm?
3. What information is stored in a Z-buffer?
4. Why is the Z-buffer initialized to infinity in this implementation?
5. What happens when a new fragment has a smaller depth value?
6. What is the purpose of the colour buffer?
7. What is one limitation of the Z-buffer algorithm?

## Submission note
The lab manual specifies C++/OpenGL. This is a Python/Tkinter adaptation; submit it only if your faculty accepts Python implementations.
