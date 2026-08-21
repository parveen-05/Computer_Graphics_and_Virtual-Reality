from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

points = [
    [1, 1],
    [4, 1],
    [4, 3],
    [1, 3]
]

tx = 2
ty = 2
sx = 1.5
sy = 1.5
angle = math.radians(30)

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Original rectangle
    glColor3f(1, 1, 1)

    glBegin(GL_LINE_LOOP)

    for p in points:
        glVertex2f(p[0], p[1])

    glEnd()

    # Transformed rectangle
    glColor3f(1, 0, 0)

    glBegin(GL_LINE_LOOP)

    for p in points:

        x = p[0]
        y = p[1]

        # Scaling
        x = x * sx
        y = y * sy

        # Rotation
        x1 = x * math.cos(angle) - y * math.sin(angle)
        y1 = x * math.sin(angle) + y * math.cos(angle)

        # Translation
        x1 = x1 + tx
        y1 = y1 + ty

        glVertex2f(x1, y1)

    glEnd()

    glFlush()


def main():

    glutInit()

    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    glutInitWindowSize(600, 600)

    glutCreateWindow(b"2D Transformations")

    glClearColor(0, 0, 0, 1)

    gluOrtho2D(-10, 10, -10, 10)

    glutDisplayFunc(display)

    glutMainLoop()


main()
