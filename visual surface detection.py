import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Graphics Shapes")
screen.setup(width=800, height=600)
pen = turtle.Turtle()
pen.speed(5)

def draw_triangle():
    # Move to starting position
    pen.penup()
    pen.goto(10, 100)
    pen.pendown()
    # Set color to green
    pen.color("green")
    pen.fillcolor("green")
    # Begin fill
    pen.begin_fill()
    # Draw triangle using the original coordinates
    pen.goto(50, 20)   # First vertex
    pen.goto(100, 100) # Second vertex
    pen.goto(10, 100)  # Back to start
    # End fill
    pen.end_fill()

def draw_circle():
    # Move to center position for circle
    pen.penup()
    pen.goto(100, 55)  # Adjusted Y to account for turtle circle drawing from bottom
    pen.pendown()
    # Set color to blue
    pen.color("blue")
    pen.fillcolor("blue")
    # Begin fill
    pen.begin_fill()
    # Draw circle with radius 45
    pen.circle(45)
    # End fill
    pen.end_fill()

def draw_rectangle():
    # Move to starting position
    pen.penup()
    pen.goto(100, 100)
    pen.pendown()
    # Set color to red
    pen.color("red")
    pen.fillcolor("red")
    # Begin fill
    pen.begin_fill()
    # Draw rectangle (80x80 to match original 180-100=80)
    for _ in range(2):
        pen.forward(80)
        pen.right(90)
        pen.forward(80)
        pen.right(90)
    # End fill
    pen.end_fill()

def main():
    # Clear the screen
    pen.clear()
    # Drawing sequence
    sequence = "RCT"
    for x in sequence:
        if x == 'C':
            draw_circle()
        elif x == 'T':
            draw_triangle()
        else:
            draw_rectangle()
    # Hide the turtle and keep window open
    pen.hideturtle()
    screen.exitonclick()  # Click to close (similar to getch())

if __name__ == "__main__":
    main()