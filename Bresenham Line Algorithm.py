import matplotlib.pyplot as plt

x1, y1 = 2, 3
x2, y2 = 15, 10

x = x1
y = y1

dx = abs(x2 - x1)
dy = abs(y2 - y1)

sx = 1 if x2 > x1 else -1
sy = 1 if y2 > y1 else -1

p = 2 * dy - dx

points_x = []
points_y = []

while x != x2 or y != y2:
    points_x.append(x)
    points_y.append(y)

    if p < 0:
        x = x + sx
        p = p + 2 * dy
    else:
        x = x + sx
        y = y + sy
        p = p + 2 * dy - 2 * dx

points_x.append(x2)
points_y.append(y2)

plt.plot(points_x, points_y, 'o-')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Bresenham's Line Drawing Algorithm")
plt.grid(True)
plt.show()
