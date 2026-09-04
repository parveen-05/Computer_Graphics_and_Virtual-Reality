from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import sys


# ---------------------------------------------------------
# Matrix multiplication
# ---------------------------------------------------------
def multiply_matrix(A, B):
    result = [[0.0 for _ in range(4)] for _ in range(4)]

    for i in range(4):
        for j in range(4):
            for k in range(4):
                result[i][j] += A[i][k] * B[k][j]

    return result


# ---------------------------------------------------------
# Transformation matrices
# ---------------------------------------------------------
def translation(tx, ty):
    return [
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1,  0],
        [0, 0, 0,  1]
    ]


def scaling(sx, sy):
    return [
        [sx, 0,  0, 0],
        [0, sy,  0, 0],
        [0,  0,  1, 0],
        [0,  0,  0, 1]
    ]


def rotation(angle):
    rad = math.radians(angle)
    c = math.cos(rad)
    s = math.sin(rad)

    return [
        [c, -s, 0, 0],
        [s,  c, 0, 0],
        [0,  0, 1, 0],
        [0,  0, 0, 1]
    ]


# ---------------------------------------------------------
# Apply matrix to a point
# ---------------------------------------------------------
def transform_point(M, x, y):
    point = [x, y, 0, 1]

    result = [0, 0, 0, 0]

    for i in range(4):
        for j in range(4):
            result[i] += M[i][j] * point[j]

    return result[0], result[1]


# ---------------------------------------------------------
# Draw square
# ---------------------------------------------------------
def draw_square(points):
    glBegin(GL_LINE_LOOP)

    for x, y in points:
        glVertex2f(x, y)

    glEnd()


# ---------------------------------------------------------
# Display
# ---------------------------------------------------------
def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Original square
    original = [
        (-1, -1),
        (1, -1),
        (1, 1),
        (-1, 1)
    ]

    # -----------------------------------------------------
    # Composite Transformation
    #
    # First Scale
    # Then Rotate
    # Then Translate
    #
    # M = T * R * S
    # -----------------------------------------------------

    S = scaling(1.5, 0.8)
    R = rotation(30)
    T = translation(3, 2)

    RS = multiply_matrix(R, S)
    M = multiply_matrix(T, RS)

    # Transform points
    transformed = []

    for x, y in original:
        transformed.append(transform_point(M, x, y))

    # Original square
    glColor3f(0.0, 1.0, 0.0)
    draw_square(original)

    # Transformed square
    glColor3f(1.0, 0.0, 0.0)
    draw_square(transformed)

    # Draw axes
    glColor3f(1.0, 1.0, 1.0)

    glBegin(GL_LINES)

    # X axis
    glVertex2f(-10, 0)
    glVertex2f(10, 0)

    # Y axis
    glVertex2f(0, -10)
    glVertex2f(0, 10)

    glEnd()

    glutSwapBuffers()


# ---------------------------------------------------------
# Initialization
# ---------------------------------------------------------
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluOrtho2D(-10, 10, -10, 10)

    glMatrixMode(GL_MODELVIEW)


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------
def main():
    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(100, 100)

    glutCreateWindow(
        b"Experiment 4 - Composite Transformations"
    )

    init()

    glutDisplayFunc(display)

    glutMainLoop()


if __name__ == "__main__":
    main()

