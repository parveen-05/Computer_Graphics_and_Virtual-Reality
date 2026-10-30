# Experiment 9: Simple Interactive 3D Scene Using Unity

## Aim
To create and interact with a simple 3D scene containing objects and a controllable view.

## Important implementation note
The lab manual specifies **Unity 2022 LTS**. This deliverable is a **Python/Tkinter 3D-scene-style visualization** so it can run on macOS without installing Unity. It demonstrates a simple scene, object rotation, zoom, coordinate axes, and wireframe display, but it is **not a Unity project** and does not use Unity's scene editor, GameObjects, components, or C# scripts. Confirm with your faculty whether this adaptation is acceptable. If the submission must be made in Unity, this Python project will not satisfy that requirement.

## Requirements
- Python 3
- Tkinter (usually included with the standard macOS Python distribution)

## Run
```bash
python3 main.py
```

## Scene contents
- Ground grid
- Central 3D cube
- X, Y and Z coordinate axes
- Perspective-style camera projection

## Interaction
- Rotate X: changes the scene's X-axis rotation.
- Rotate Y: changes the scene's Y-axis rotation.
- Zoom: changes the viewport scale.
- Show coordinate axes: toggles the three axes.
- Wireframe view: switches between filled faces and cube edges.
- Reset view: restores the initial view.

## Result
An interactive 3D-scene-style view is displayed. The user can rotate and zoom the scene and toggle axes and wireframe mode.

## Viva questions
1. What is a 3D scene?
2. What is a GameObject in Unity?
3. What is a Transform component?
4. What is the purpose of a camera in a 3D scene?
5. What is the difference between a mesh and a material?
6. What is wireframe rendering?
7. Which programming language is commonly used for Unity scripting?
