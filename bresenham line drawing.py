import turtle

# Function to draw a pixel (dot)
def putpixel(x, y, color="black"):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot(3, color)   # 3px dot simulates a pixel

# Bresenham's Line Drawing Algorithm
def drawLine(x1, y1, x2, y2):
    if x1 > x2:  # Ensure left-to-right drawing
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    dx = x2 - x1
    dy = abs(y2 - y1)
    p = 2 * dy - dx
    y = y1
    y_step = 1 if y1 < y2 else -1

    for x in range(x1, x2 + 1):
        putpixel(x, y)
        if p >= 0:
            y += y_step
            p += 2 * (dy - dx)
        else:
            p += 2 * dy

def main():
    turtle.speed(5)     # Fastest
    turtle.hideturtle() # Hide turtle cursor
    turtle.setup(800, 600)  # Window size

    x1, y1 = -200, -100   # Adjusted for turtle's center (0,0)
    x2, y2 = 200, 170

    drawLine(x1, y1, x2, y2)

    turtle.done()

if __name__ == "__main__":
    main()
