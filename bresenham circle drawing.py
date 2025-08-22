import turtle

# Function to plot symmetric points in all 8 octants
def plot_circle_points(xc, yc, x, y):
    turtle.penup()
    turtle.goto(xc + x, yc + y)
    turtle.pendown()
    turtle.dot(3, "blue")

    turtle.penup()
    turtle.goto(xc - x, yc + y)
    turtle.pendown()
    turtle.dot(3, "blue")

    turtle.penup()
    turtle.goto(xc + x, yc - y)
    turtle.pendown()
    turtle.dot(3, "blue")

    turtle.penup()
    turtle.goto(xc - x, yc - y)
    turtle.pendown()
    turtle.dot(3, "blue")

    turtle.penup()
    turtle.goto(xc + y, yc + x)
    turtle.pendown()
    turtle.dot(3, "blue")

    turtle.penup()
    turtle.goto(xc - y, yc + x)
    turtle.pendown()
    turtle.dot(3, "blue")

    turtle.penup()
    turtle.goto(xc + y, yc - x)
    turtle.pendown()
    turtle.dot(3, "blue")

    turtle.penup()
    turtle.goto(xc - y, yc - x)
    turtle.pendown()
    turtle.dot(3, "blue")

# Bresenham’s Circle Drawing Algorithm
def drawCircle(xc, yc, r):
    x = 0
    y = r
    p = 3 - 2 * r

    while x <= y:
        plot_circle_points(xc, yc, x, y)
        if p < 0:
            p += 4 * x + 6
        else:
            p += 4 * (x - y) + 10
            y -= 1
        x += 1

def main():
    turtle.speed(0)
    turtle.hideturtle()
    turtle.setup(800, 600)  # Window size

    # Center (xc, yc), radius r
    xc, yc, r = 0, 0, 100
    drawCircle(xc, yc, r)

    turtle.done()

if __name__ == "__main__":
    main()
