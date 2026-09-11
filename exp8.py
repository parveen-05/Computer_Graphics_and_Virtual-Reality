import glfw
from OpenGL.GL import *
import math


# --------------------------------------------------
# Matrix Multiplication
# --------------------------------------------------
def multiply_matrix(A, B):
    result = [[0 for _ in range(3)] for _ in range(3)]

    for i in range(3):
        for j in range(3):
            for k in range(3):
                result[i][j] += A[i][k] * B[k][j]

    return result


# --------------------------------------------------
# Apply Matrix to Point
# --------------------------------------------------
def transform_point(M, p):
    x = M[0][0] * p[0] + M[0][1] * p[1] + M[0][2]
    y = M[1][0] * p[0] + M[1][1] * p[1] + M[1][2]
    return [x, y]


# --------------------------------------------------
# Translation Matrix
# --------------------------------------------------
def translation(tx, ty):
    return [
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ]


# --------------------------------------------------
# Scaling Matrix
# --------------------------------------------------
def scaling(sx, sy):
    return [
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ]


# --------------------------------------------------
# Rotation Matrix
# --------------------------------------------------
def rotation(angle):
    rad = math.radians(angle)
    c = math.cos(rad)
    s = math.sin(rad)

    return [
        [c, -s, 0],
        [s,  c, 0],
        [0,  0, 1]
    ]


# --------------------------------------------------
# Reflection Matrix
# --------------------------------------------------
def reflection_x():
    return [
        [1, 0, 0],
        [0, -1, 0],
        [0, 0, 1]
    ]


# --------------------------------------------------
# Shearing Matrix
# --------------------------------------------------
def shearing(shx, shy):
    return [
        [1, shx, 0],
        [shy, 1, 0],
        [0, 0, 1]
    ]


# --------------------------------------------------
# Draw Polygon
# --------------------------------------------------
def draw_polygon(points):
    glBegin(GL_LINE_LOOP)

    for x, y in points:
        glVertex2f(x, y)

    glEnd()


# --------------------------------------------------
# Main Program
# --------------------------------------------------
def main():

    if not glfw.init():
        return

    window = glfw.create_window(
        800,
        600,
        "Experiment 8 - 2D Geometric Transformations",
        None,
        None
    )

    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    # Coordinate system
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-400, 400, -300, 300, -1, 1)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Original triangle
    triangle = [
        [-100, -50],
        [100, -50],
        [0, 100]
    ]

    while not glfw.window_should_close(window):

        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()

        # -----------------------------
        # Original Object
        # -----------------------------
        glLineWidth(3)
        draw_polygon(triangle)

        # -----------------------------
        # Translation
        # -----------------------------
        T = translation(200, 0)

        translated = [
            transform_point(T, p)
            for p in triangle
        ]

        draw_polygon(translated)

        # -----------------------------
        # Rotation
        # -----------------------------
        R = rotation(45)

        rotated = [
            transform_point(R, p)
            for p in triangle
        ]

        draw_polygon(rotated)

        # -----------------------------
        # Scaling
        # -----------------------------
        S = scaling(0.5, 0.5)

        scaled = [
            transform_point(S, p)
            for p in triangle
        ]

        draw_polygon(scaled)

        # -----------------------------
        # Reflection
        # -----------------------------
        F = reflection_x()

        reflected = [
            transform_point(F, p)
            for p in triangle
        ]

        draw_polygon(reflected)

        # -----------------------------
        # Shearing
        # -----------------------------
        H = shearing(0.5, 0)

        sheared = [
            transform_point(H, p)
            for p in triangle
        ]

        draw_polygon(sheared)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()
