import turtle
import math

# Set up enhanced screen
screen = turtle.Screen()
screen.bgcolor("white")  # Dark background
screen.title("2D Geometric Transformations - Translation, Rotation, Scaling")
screen.setup(width=1200, height=800)
screen.setworldcoordinates(-600, -400, 600, 400)

def setup_turtle():
    """Setup turtle with optimized settings"""
    turtle.speed(0)
    turtle.hideturtle()
    turtle.pensize(2)

def draw_axes():
    """Draw enhanced coordinate axes with labels"""
    # Main axes
    turtle.pensize(3)
    turtle.color("#4a90e2")  # Blue axes
    
    # X-axis
    turtle.penup()
    turtle.goto(-550, 0)
    turtle.pendown()
    turtle.goto(550, 0)
    
    # Y-axis
    turtle.penup()
    turtle.goto(0, -350)
    turtle.pendown()
    turtle.goto(0, 350)
    
    # Add axis labels
    turtle.color("#ffffff")
    turtle.penup()
    turtle.goto(520, 15)
    turtle.write("X", font=("Arial", 16, "bold"))
    turtle.goto(15, 320)
    turtle.write("Y", font=("Arial", 16, "bold"))
    
    # Add grid lines
    turtle.color("#2a2a2a")
    turtle.pensize(1)
    
    # Vertical grid lines
    for x in range(-500, 501, 50):
        if x != 0:  # Skip center line
            turtle.penup()
            turtle.goto(x, -350)
            turtle.pendown()
            turtle.goto(x, 350)
    
    # Horizontal grid lines
    for y in range(-300, 301, 50):
        if y != 0:  # Skip center line
            turtle.penup()
            turtle.goto(-550, y)
            turtle.pendown()
            turtle.goto(550, y)

def draw_polygon(points, color, fill_color=None, width=3):
    """Draw enhanced polygon with optional fill"""
    turtle.pensize(width)
    turtle.color(color)
    
    if fill_color:
        turtle.fillcolor(fill_color)
        turtle.begin_fill()
    
    turtle.penup()
    turtle.goto(points[0])
    turtle.pendown()
    
    for p in points[1:]:
        turtle.goto(p)
    turtle.goto(points[0])  # Close the polygon
    
    if fill_color:
        turtle.end_fill()
    
    turtle.penup()

def draw_arrow(start, end, color="#ffff00"):
    """Draw an arrow from start to end point"""
    turtle.color(color)
    turtle.pensize(2)
    turtle.penup()
    turtle.goto(start)
    turtle.pendown()
    turtle.goto(end)
    
    # Draw arrowhead
    angle = math.atan2(end[1] - start[1], end[0] - start[0])
    arrow_length = 15
    arrow_angle = math.pi / 6
    
    # Left side of arrowhead
    x1 = end[0] - arrow_length * math.cos(angle - arrow_angle)
    y1 = end[1] - arrow_length * math.sin(angle - arrow_angle)
    turtle.goto(x1, y1)
    
    turtle.goto(end)
    
    # Right side of arrowhead
    x2 = end[0] - arrow_length * math.cos(angle + arrow_angle)
    y2 = end[1] - arrow_length * math.sin(angle + arrow_angle)
    turtle.goto(x2, y2)

def add_title():
    """Add main title"""
    turtle.color("#ffffff")
    turtle.penup()
    turtle.goto(0, 350)
    turtle.write("2D GEOMETRIC TRANSFORMATIONS", 
                align="center", font=("Arial", 24, "bold"))

def add_operation_label(x, y, title, description, color):
    """Add operation title and description"""
    turtle.color(color)
    turtle.penup()
    turtle.goto(x, y + 30)
    turtle.write(title, align="center", font=("Arial", 16, "bold"))
    
    turtle.color("#cccccc")
    turtle.goto(x, y + 10)
    turtle.write(description, align="center", font=("Arial", 11, "normal"))

# -------------------- Transformations --------------------
def translate(points, tx, ty):
    """Translate polygon by (tx, ty)"""
    return [(x + tx, y + ty) for x, y in points]

def rotate(points, angle):
    """Rotate polygon about origin"""
    rad = math.radians(angle)
    return [
        (x*math.cos(rad) - y*math.sin(rad),
         x*math.sin(rad) + y*math.cos(rad))
        for x, y in points
    ]

def scale(points, sx, sy):
    """Scale polygon about origin"""
    return [(x*sx, y*sy) for x, y in points]

def main():
    setup_turtle()
    add_title()
    draw_axes()
    
    # Create a more interesting original shape (house-like)
    polygon = [(-30, -20), (30, -20), (30, 20), (0, 40), (-30, 20)]
    
    # ==================== TRANSLATION ====================
    # Position in 1st quadrant
    trans_center = (200, 150)
    trans_origin = [(x + trans_center[0], y + trans_center[1]) for x, y in polygon]
    
    # Original shape
    draw_polygon(trans_origin, "#4a90e2", "#1a4a7a", 3)  # Blue
    
    # Translated shape
    translated = translate(trans_origin, 120, 80)
    draw_polygon(translated, "#ff6b6b", "#cc4444", 3)  # Red
    
    # Draw translation arrow
    centroid_orig = (trans_center[0], trans_center[1] + 10)
    centroid_trans = (trans_center[0] + 120, trans_center[1] + 90)
    draw_arrow(centroid_orig, centroid_trans, "#ffff00")
    
    # Add labels
    add_operation_label(trans_center[0] + 60, trans_center[1] + 150, 
                       "TRANSLATION", "Moving object by (Δx, Δy)", "black")
    
    turtle.color("black")
    turtle.penup()
    turtle.goto(trans_center[0] - 20, trans_center[1] - 50)
    turtle.write("Original", font=("Arial", 10, "normal"))
    turtle.goto(trans_center[0] + 100, trans_center[1] + 30)
    turtle.write("Translated\n(+120, +80)", font=("Arial", 10, "normal"))
    
    # ==================== ROTATION ====================
    # Position in 2nd quadrant
    rot_center = (-100, 300)
    rot_origin = [(x + rot_center[0], y + rot_center[1]) for x, y in polygon]
    
    # Original shape
    draw_polygon(rot_origin, "#4a90e2", "#1a4a7a", 3)  # Blue
    
    # Rotated shape
    rotated = rotate(rot_origin, 60)  # 60 degrees
    draw_polygon(rotated, "#4ecdc4", "#2a7a72", 3)  # Teal
    
    # Draw rotation arc (simplified)
    turtle.color("black")
    turtle.pensize(2)
    turtle.penup()
    turtle.goto(rot_center[0], rot_center[1])
    turtle.pendown()
    turtle.circle(50, 60)  # Arc showing rotation
    
    # Add labels
    add_operation_label(rot_center[0]-200, rot_center[1] , 
                       "ROTATION", "Rotating object by θ degrees", "black")
    # ==================== SCALING ====================
    # Position in 3rd quadrant
    scale_center = (-200, -150)
    scale_origin = [(x + scale_center[0], y + scale_center[1]) for x, y in polygon]
    
    # Original shape
    draw_polygon(scale_origin, "#4a90e2", "#1a4a7a", 3)  # Blue
    
    # Scaled shape
    scaled = scale(scale_origin, 2.0, 1.5)  # Scale by 2x horizontally, 1.5x vertically
    draw_polygon(scaled, "#95e1d3", "#5a8c7a", 3)  # Mint green
    
    # Draw scaling indicators (lines from center to corners)
    turtle.color("green")
    turtle.pensize(1)
    for point_orig, point_scaled in zip(scale_origin, scaled):
        turtle.penup()
        turtle.goto(point_orig)
        turtle.pendown()
        turtle.goto(point_scaled)
    
    # Add labels
    add_operation_label(scale_center[0]-100, scale_center[1] + 80, 
                       "SCALING", "Resizing object by (Sx, Sy)", "black")
    
    screen.exitonclick()

if __name__ == "__main__":
    main()