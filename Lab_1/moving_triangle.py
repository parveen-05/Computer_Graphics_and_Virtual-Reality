import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader


vertices = [
    -0.2, -0.2, 0.0,
     0.2, -0.2, 0.0,
     0.0,  0.3, 0.0
]


vertex_shader = """
#version 120

attribute vec3 position;

uniform float offset;

void main()
{
    gl_Position = vec4(position.x + offset, position.y, position.z, 1.0);
}
"""


fragment_shader = """
#version 120

void main()
{
    gl_FragColor = vec4(1.0, 0.2, 0.1, 1.0);
}
"""


if not glfw.init():
    raise Exception("GLFW failed")


window = glfw.create_window(
    800,
    600,
    "Moving Triangle",
    None,
    None
)

if not window:
    glfw.terminate()
    raise Exception("Window failed")


glfw.make_context_current(window)


shader = compileProgram(
    compileShader(vertex_shader, GL_VERTEX_SHADER),
    compileShader(fragment_shader, GL_FRAGMENT_SHADER)
)

glUseProgram(shader)


VBO = glGenBuffers(1)

glBindBuffer(GL_ARRAY_BUFFER, VBO)

glBufferData(
    GL_ARRAY_BUFFER,
    len(vertices) * 4,
    (GLfloat * len(vertices))(*vertices),
    GL_STATIC_DRAW
)


position_location = glGetAttribLocation(shader, "position")

glEnableVertexAttribArray(position_location)

glVertexAttribPointer(
    position_location,
    3,
    GL_FLOAT,
    GL_FALSE,
    0,
    None
)


position = -0.8
speed = 0.003
direction = 1

offset_location = glGetUniformLocation(shader, "offset")


while not glfw.window_should_close(window):

    glClearColor(0.05, 0.05, 0.05, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)


    position += speed * direction

    if position > 0.8 or position < -0.8:
        direction *= -1


    glUniform1f(offset_location, position)

    glDrawArrays(GL_TRIANGLES, 0, 3)


    glfw.swap_buffers(window)
    glfw.poll_events()


glfw.terminate()
