# Experiment 8: Basic OpenGL Program Using Vertex and Fragment Shaders

## Aim
To understand the roles of vertex and fragment shaders in a basic graphics rendering pipeline.

## Important implementation note
The lab manual specifies OpenGL and GLSL. This deliverable is a **Python/Tkinter educational simulation** because it can run with the standard Python installation on macOS. It displays the shader stages and an illustrative GLSL code pair, but it does **not** create an OpenGL context, compile GLSL, or execute GPU shaders. Confirm with your faculty whether this Python adaptation is acceptable. It is not a substitute for an actual OpenGL/GLSL submission if that is required.

## Requirements
- Python 3
- Tkinter (usually included with the standard macOS Python distribution)

## Run
```bash
python3 main.py
```

## What the program demonstrates
1. Vertex shader: processes vertex positions and vertex colour attributes.
2. Primitive assembly: forms a triangle from the processed vertices.
3. Rasterization: identifies the fragments/pixels covered by the triangle.
4. Fragment shader: determines the final colour of each fragment.

Use the radio buttons to switch between:
- Interpolated colour gradient
- Flat colour
- Grayscale

## Illustrative GLSL
The application displays a simple vertex shader and fragment shader example. The snippets are for learning and are not compiled by this Python program.

## Result
The simulated triangle displays different fragment shading modes and the four main stages of the shader pipeline.

## Viva questions
1. What is a vertex shader?
2. What is a fragment shader?
3. What is the purpose of `gl_Position`?
4. What is rasterization?
5. What is the difference between a vertex and a fragment?
6. Why are vertex attributes interpolated across a triangle?
