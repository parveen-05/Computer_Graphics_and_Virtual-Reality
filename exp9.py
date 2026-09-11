import glfw
from OpenGL.GL import *
import math


# --------------------------------------------------
# Matrix Multiplication
# --------------------------------------------------
def multiply_matrix(A, B):
    result = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

    for i in range(3):
        for j in range(3):
            for k in range(3):
                result[i][j] += A[i][k] * B[k][j]

    return result


# --------------------------------------------------
# Transform a Point using 3x3 Matrix
# --------------------------------------------------
def transform_point(M, point):
    x, y = point

    new_x = M[0][0] * x + M[0][1] * y + M[0][2]
    new_y = M[1][0] * x + M[1][1] * y + M[1][2]

    return [new_x, new_y]


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
# Rotation Matrix
# --------------------------------------------------
def rotation(angle):
    theta = math.radians(angle)

    return [
        [math.cos(theta), -math.sin(theta), 0],
        [math.sin(theta),  math.cos(theta), 0],
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
# Reflection about X-axis
# --------------------------------------------------
def reflection():
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
# Draw Axes
# --------------------------------------------------
def draw_axes():

    glBegin(GL_LINES)

    # X-axis
    glVertex2f(-400, 0)
    glVertex2f(400, 0)

    # Y-axis
    glVertex2f(0, -300)
    glVertex2f(0, 300)

    glEnd()


# --------------------------------------------------
# Main Function
# --------------------------------------------------
def main():

    if not glfw.init():
        print("GLFW initialization failed")
        return

    window = glfw.create_window(
        800,
        600,
        "Experiment 9 - 2D Geometric Transformations",
        None,
        None
    )

    if not window:
        glfw.terminate()
        print("Window creation failed")
        return

    glfw.make_context_current(window)

    # Set 2D coordinate system
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-400, 400, -300, 300, -1, 1)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Original triangle
    triangle = [
        [-80, -60],
        [80, -60],
        [0, 100]
    ]

    # --------------------------------------------------
    # Create transformation matrices
    # --------------------------------------------------

    T = translation(200, 0)

    R = rotation(45)

    S = scaling(1.5, 1.5)

    F = reflection()

    H = shearing(0.5, 0)

    # Composite transformation
    composite = multiply_matrix(T, R)
    composite = multiply_matrix(composite, S)

    transformed_triangle = [
        transform_point(composite, p)
        for p in triangle
    ]

    # Other transformations
    translated_triangle = [
        transform_point(T, p)
        for p in triangle
    ]

    rotated_triangle = [
        transform_point(R, p)
        for p in triangle
    ]

    scaled_triangle = [
        transform_point(S, p)
        for p in triangle
    ]

    reflected_triangle = [
        transform_point(F, p)
        for p in triangle
    ]

    sheared_triangle = [
        transform_point(H, p)
        for p in triangle
    ]

    # --------------------------------------------------
    # Display Loop
    # --------------------------------------------------

    while not glfw.window_should_close(window):

        glClear(GL_COLOR_BUFFER_BIT)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glLineWidth(2)

        # Draw coordinate axes
        draw_axes()

        # Original triangle
        draw_polygon(triangle)

        # Translation
        draw_polygon(translated_triangle)

        # Rotation
        draw_polygon(rotated_triangle)

        # Scaling
        draw_polygon(scaled_triangle)

        # Reflection
        draw_polygon(reflected_triangle)

        # Shearing
        draw_polygon(sheared_triangle)

        # Composite transformation
        draw_polygon(transformed_triangle)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()


# --------------------------------------------------
# Program Entry
# --------------------------------------------------

if __name__ == "__main__":
    main()
