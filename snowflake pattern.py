import turtle
import math
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Koch Snowflake Fractal")
screen.setup(width=800, height=700)
screen.setworldcoordinates(0, 0, 500, 400)

# Create a turtle for drawing
pen = turtle.Turtle()
pen.speed(10)
pen.pensize(3)
pen.color("cyan")

def draw_line(x1, y1, x2, y2):
    """Draw a line from (x1, y1) to (x2, y2)"""
    pen.penup()
    pen.goto(x1, y1)
    pen.pendown()
    pen.goto(x2, y2)

def snowflake(x1, y1, x5, y5, iteration):
    """
    Recursive function to draw Koch snowflake
    (x1, y1) - starting point
    (x5, y5) - ending point
    iteration - recursion depth
    """
    if iteration > 0:
        # Calculate the five key points for Koch curve
        dx = (x5 - x1) / 3
        dy = (y5 - y1) / 3
        
        # Point 1: Starting point
        x0, y0 = x1, y1
        
        # Point 2: 1/3 along the line
        x1_new, y1_new = x1 + dx, y1 + dy
        
        # Point 3: The peak of the equilateral triangle
        # This uses rotation of 60 degrees to create the triangle peak
        x2_new = (x1 + x5) / 2 + math.sqrt(3) * (y1 - y5) / 6
        y2_new = (y1 + y5) / 2 + math.sqrt(3) * (x5 - x1) / 6
        
        # Point 4: 2/3 along the line
        x3_new, y3_new = x1 + 2 * dx, y1 + 2 * dy
        
        # Point 5: Ending point
        x4_new, y4_new = x5, y5
        
        # Store all points
        points = [
            (x0, y0),
            (x1_new, y1_new),
            (x2_new, y2_new),
            (x3_new, y3_new),
            (x4_new, y4_new)
        ]
        
        # Recursively draw the four segments
        for i in range(4):
            snowflake(points[i][0], points[i][1], points[i+1][0], points[i+1][1], iteration - 1)
    else:
        # Base case: draw a straight line
        draw_line(x1, y1, x5, y5)
        time.sleep(0.001)  # Small delay to visualize the drawing process


def main():
    
    # Set up the initial triangle vertices (same as C++ code)
    # These form an equilateral triangle
    triangle_vertices = [
        (250, 15),   # Top vertex
        (50, 350),   # Bottom left vertex  
        (450, 350)   # Bottom right vertex
    ]
    
    # Set iteration depth
    iteration = 4
    
    # Add iteration counter display
    counter_pen = turtle.Turtle()

    
    # Draw the three sides of the Koch snowflake
    pen.color("blue")
    for i in range(3):
        # Get current and next vertex (wrapping around with modulo)
        x1, y1 = triangle_vertices[i]
        x2, y2 = triangle_vertices[(i + 1) % 3]
        
        # Draw Koch curve for this side
        snowflake(x1, y1, x2, y2, iteration)
    
    # Hide the drawing pen and wait for click
    pen.hideturtle()
    screen.exitonclick()

if __name__ == "__main__":
    main()