import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Cohen-Sutherland Line Clipping Algorithm")
screen.setup(width=800, height=600)
screen.setworldcoordinates(0, 0, 600, 500)

# Create a turtle
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(5)

# Clipping window coordinates
x_left = 120
x_right = 500
y_bottom = 100
y_top = 350

# Line coordinates
line_x1 = 50
line_y1 = 100
line_x2 = 600
line_y2 = 300

# Region codes
Left = 1
Right = 2
Bottom = 4
Top = 8

def region_code(x, y):
    """Calculate the region code for a point (x, y)"""
    code = 0
    if x > x_right:
        code |= Right
    elif x < x_left:
        code |= Left
    if y > y_top:
        code |= Top
    elif y < y_bottom:
        code |= Bottom
    return code

def draw_line(x1, y1, x2, y2, color="white"):
    """Draw a line from (x1, y1) to (x2, y2)"""
    pen.penup()
    pen.goto(x1, y1)
    pen.pendown()
    pen.color(color)
    pen.goto(x2, y2)

def draw_rectangle(x1, y1, x2, y2, color="blue"):
    """Draw a rectangle with corners at (x1, y1) and (x2, y2)"""
    pen.penup()
    pen.goto(x1, y1)
    pen.pendown()
    pen.color(color)
    
    # Draw rectangle
    pen.goto(x2, y1)  # Bottom right
    pen.goto(x2, y2)  # Top right
    pen.goto(x1, y2)  # Top left
    pen.goto(x1, y1)  # Back to bottom left

def cohen_sutherland(x1, y1, x2, y2):
    """Cohen-Sutherland line clipping algorithm"""
    code1 = region_code(x1, y1)
    code2 = region_code(x2, y2)
    
    while True:
        # Line is completely inside
        if not (code1 | code2):
            draw_line(x1, y1, x2, y2, "blue")
            return
        
        # Line is completely outside
        elif code1 & code2:
            break
        
        # Line is partially inside
        else:
            # Choose an endpoint that is outside the clipping window
            code = code1 if code1 else code2
            
            # Find intersection point
            if code & Top:
                y = y_top
                x = x1 + (x2 - x1) / (y2 - y1) * (y - y1)
            elif code & Bottom:
                y = y_bottom
                x = x1 + (x2 - x1) / (y2 - y1) * (y - y1)
            elif code & Left:
                x = x_left
                y = y1 + (y2 - y1) / (x2 - x1) * (x - x1)
            elif code & Right:
                x = x_right
                y = y1 + (y2 - y1) / (x2 - x1) * (x - x1)
            
            # Replace the outside endpoint with the intersection point
            if code == code1:
                x1 = x
                y1 = y
                code1 = region_code(x1, y1)
            else:
                x2 = x
                y2 = y
                code2 = region_code(x2, y2)

def main():
    # Draw clipping window in yellow
    draw_rectangle(x_left, y_bottom, x_right, y_top, "green")
    
    # Draw original line in a different color (red) to show the difference
    draw_line(line_x1, line_y1, line_x2, line_y2, "red")
    
    # Add text labels
    pen.penup()
    pen.goto(50, 450)
    pen.color("black")
    pen.write("Cohen-Sutherland Line Clipping", font=("Arial", 16, "bold"))
    
    pen.goto(50, 420)
    pen.write("Red: Original line", font=("Arial", 12, "normal"))
    
    pen.goto(50, 400)
    pen.write("Blue: Clipped line", font=("Arial", 12, "normal"))
    
    pen.goto(50, 380)
    pen.write("Green: Clipping window", font=("Arial", 12, "normal"))
    
    # Apply Cohen-Sutherland clipping algorithm
    cohen_sutherland(line_x1, line_y1, line_x2, line_y2)
    
    # Hide turtle and wait for click
    pen.hideturtle()
    screen.exitonclick()

if __name__ == "__main__":
    main()