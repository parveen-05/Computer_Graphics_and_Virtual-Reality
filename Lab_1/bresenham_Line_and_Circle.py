from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Window dimensions
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

def draw_pixel(x, y):
    """Utility function to draw a single pixel at (x, y)."""
    glBegin(GL_POINTS)
    glVertex2i(int(x), int(y))
    glEnd()

def bresenham_line(x1, y1, x2, y2):
    """General Bresenham's Line Algorithm handling all slopes and directions."""
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    # Determine step directions
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    
    x, y = x1, y1
    
    # Case 1: Slope is less than or equal to 1 (Horizontal dominant)
    if dx > dy:
        p = 2 * dy - dx
        for _ in range(dx + 1):
            draw_pixel(x, y)
            if p >= 0:
                y += sy
                p -= 2 * dx
            x += sx
            p += 2 * dy
    # Case 2: Slope is greater than 1 (Vertical dominant)
    else:
        p = 2 * dx - dy
        for _ in range(dy + 1):
            draw_pixel(x, y)
            if p >= 0:
                x += sx
                p -= 2 * dy
            y += sy
            p += 2 * dx

def bresenham_circle(xc, yc, r):
    """Bresenham's / Midpoint Circle Drawing Algorithm using 8-way symmetry."""
    x = 0
    y = r
    p = 3 - 2 * r  # Initial decision parameter
    
    def plot_symmetric_points(xc, yc, x, y):
        """Plots pixels in all 8 octants based on symmetry."""
        draw_pixel(xc + x, yc + y)
        draw_pixel(xc - x, yc + y)
        draw_pixel(xc + x, yc - y)
        draw_pixel(xc - x, yc - y)
        draw_pixel(xc + y, yc + x)
        draw_pixel(xc - y, yc + x)
        draw_pixel(xc + y, yc - x)
        draw_pixel(xc - y, yc - x)

    # Initial plot
    plot_symmetric_points(xc, yc, x, y)
    
    while x <= y:
        x += 1
        if p < 0:
            p += 4 * x + 6
        else:
            y -= 1
            p += 4 * (x - y) + 10
            
        plot_symmetric_points(xc, yc, x, y)

def display():
    """OpenGL Render Callback function."""
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Draw a line using Bresenham's Algorithm (Red color)
    glColor3f(1.0, 0.0, 0.0) 
    # Parameters: (x1, y1, x2, y2)
    bresenham_line(50, 50, 450, 300)
    bresenham_line(450, 300, 550, 550) # Secondary test line
    
    # Draw a circle using Bresenham's Algorithm (Cyan color)
    glColor3f(0.0, 1.0, 1.0)
    # Parameters: (centerX, centerY, radius)
    bresenham_circle(300, 300, 150)
    bresenham_circle(300, 300, 50)   # Nested circle
    
    glFlush()

def init():
    """Initialization function to set up the projection viewport."""
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Black background
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Establish a 2D coordinate system matching window pixels
    gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)

def main():
    # Initialize GLUT
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Bresenham's Line & Circle Algorithms")
    
    # Register callbacks
    init()
    glutDisplayFunc(display)
    
    # Start the persistent main rendering loop
    glutMainLoop()

if __name__ == "__main__":
    main()
