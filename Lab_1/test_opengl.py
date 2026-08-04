from OpenGL.GL import *
import glfw

if not glfw.init():
    raise RuntimeError("Failed to initialize GLFW")

window = glfw.create_window(800, 600, "My First OpenGL Window", None, None)

if not window:
    glfw.terminate()
    raise RuntimeError("Failed to create window")

glfw.make_context_current(window)

while not glfw.window_should_close(window):
    glClearColor(0.2, 0.3, 0.8, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()
