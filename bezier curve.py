import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Bezier Curve")
screen.setup(width=800, height=600)
screen.setworldcoordinates(0, 0, 500, 300)
# Create a turtle
pen = turtle.Turtle()
pen.speed(5)
pen.pensize(3)

def factorial(n):
    """Calculate factorial of n"""
    if n:
        return n * factorial(n - 1)
    return 1

def nCr(n, r):
    """Calculate binomial coefficient (n choose r)"""
    return factorial(n) / (factorial(r) * factorial(n - r))

def bezier_function(k, n, u):
    """Calculate Bezier basis function"""
    return nCr(n, k) * pow(u, k) * pow((1 - u), (n - k))

def draw_point(x, y, color="white", radius=5):
    """Draw a point (circle) at given coordinates"""
    pen.penup()
    pen.goto(x, y - radius)
    pen.pendown()
    pen.color(color)
    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

def put_pixel(x, y, color="black"):
    """Simulate putpixel by drawing a very small dot"""
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    pen.dot(1)

def bezier_curve(points):
    """Draw Bezier curve using given control points"""
    n = len(points) - 1
    eps = 0.01  # Slightly larger step for better performance
    
    # Draw the Bezier curve
    pen.color("blue")
    first_point = True
    
    for u in [i * eps for i in range(int(1/eps) + 1)]:
        if u > 1:
            u = 1
            
        x = 0
        y = 0
        
        # Calculate point on curve
        for k in range(n + 1):
            bez = bezier_function(k, n, u)
            x += points[k][0] * bez
            y += points[k][1] * bez
        
        # Draw the curve
        if first_point:
            pen.penup()
            pen.goto(x, y)
            pen.pendown()
            first_point = False
        else:
            pen.goto(x, y)
    
    # Draw control points
    for i, point in enumerate(points):
        draw_point(point[0], point[1], "red", 5)
        
        # Label the control points
        pen.penup()
        pen.goto(point[0] + 10, point[1] + 10)
        pen.color("black")
        pen.write(f"P{i}({point[0]}, {point[1]})", font=("Arial", 10, "normal"))
    
    # Draw control polygon (lines connecting control points)
    pen.color("black")
    pen.penup()
    pen.goto(points[0][0], points[0][1])
    pen.pendown()
    pen.pensize(2)
    
    for i in range(1, len(points)):
        pen.goto(points[i][0], points[i][1])

def main():
    # Control points for the Bezier curve
    points = [(27, 243), (101, 47), (324, 197), (437, 23)]
    
    # Add title and information
    pen.penup()
    pen.goto(250, 350)
    pen.color("black")
    pen.write("Bezier Curve Visualization", align="center", font=("Arial", 16, "bold"))
    
    pen.goto(50, 330)
    pen.write("Blue: Bezier Curve", font=("Arial", 12, "normal"))
    pen.goto(50, 320)
    pen.write("Red: Control Points", font=("Arial", 12, "normal"))
    pen.goto(50, 310)
    pen.write("Black: Control Polygon", font=("Arial", 12, "normal"))
    
    # Draw the Bezier curve
    bezier_curve(points)
    
    
    # Hide turtle and wait for click
    pen.hideturtle()
    screen.exitonclick()

if __name__ == "__main__":
    main()