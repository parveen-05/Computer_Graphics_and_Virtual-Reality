# Experiment 10: 3D Viewing Pipeline Including Projection and Viewport Mapping

## Aim
To demonstrate the stages of the 3D viewing pipeline, including projection and viewport mapping.

## Implementation note
This project is a **Python/Tkinter educational visualization**. It demonstrates model/view transformation, perspective and orthographic projection, and viewport scaling in a simplified way. It is not an OpenGL implementation and does not reproduce a full graphics API pipeline. Use it as a learning/demo adaptation; confirm with your faculty whether Python is accepted for submission.

## Requirements
- Python 3
- Tkinter (usually included with the standard macOS Python distribution)

## Run
```bash
python3 main.py
```

## Controls
- Perspective projection: objects farther from the camera appear smaller.
- Orthographic projection: object size does not change with depth.
- Object rotation: rotates the cube for a different view.
- Camera zoom: changes the apparent size of the scene.
- Viewport scale: changes the mapping scale within the screen viewport.
- Reset: restores the initial settings.

## Pipeline shown
1. Model coordinates: vertices are defined in the object's local coordinate system.
2. View transformation: coordinates are adjusted relative to a simplified camera.
3. Projection: 3D points are mapped to a 2D view using perspective or orthographic projection.
4. Viewport mapping: projected points are placed within the screen viewport.

## Result
The cube is displayed using the selected projection mode, and the user can adjust rotation, zoom, and viewport scale.

## Viva questions
1. What is the 3D viewing pipeline?
2. What is a view transformation?
3. What is projection?
4. What is the difference between perspective and orthographic projection?
5. What is a viewport?
6. What is viewport mapping?
7. Why does perspective projection make distant objects appear smaller?
