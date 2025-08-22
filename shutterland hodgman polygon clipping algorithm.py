import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Sutherland-Hodgman Polygon Clipping Algorithm")
screen.setup(width=900, height=700)
screen.setworldcoordinates(0, 0, 900, 700)

# Create a turtle
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)

# Clipping window coordinates
clip_window = {
    'left': 200,
    'right': 600,
    'bottom': 150,
    'top': 450
}

def draw_polygon(vertices, color="white", fill=False):
    """Draw a polygon given a list of vertices"""
    if len(vertices) < 3:
        return
    pen.penup()
    pen.goto(vertices[0][0], vertices[0][1])
    pen.pendown()
    pen.color(color)
    if fill:
        pen.fillcolor(color)
        pen.begin_fill()
    
    for i in range(1, len(vertices)):
        pen.goto(vertices[i][0], vertices[i][1])
    # Close the polygon
    pen.goto(vertices[0][0], vertices[0][1])
    if fill:
        pen.end_fill()

def draw_clipping_window():
    """Draw the clipping window"""
    vertices = [
        (clip_window['left'], clip_window['bottom']),
        (clip_window['right'], clip_window['bottom']),
        (clip_window['right'], clip_window['top']),
        (clip_window['left'], clip_window['top'])
    ]
    draw_polygon(vertices, "red")

def is_inside(point, edge):
    """Check if a point is inside relative to a clipping edge"""
    x, y = point
    if edge == 'left':
        return x >= clip_window['left']
    elif edge == 'right':
        return x <= clip_window['right']
    elif edge == 'bottom':
        return y >= clip_window['bottom']
    elif edge == 'top':
        return y <= clip_window['top']
    return False

def compute_intersection(p1, p2, edge):
    """Compute intersection point of line segment with clipping edge"""
    x1, y1 = p1
    x2, y2 = p2
    if edge == 'left':
        x = clip_window['left']
        if x2 - x1 != 0:
            y = y1 + (y2 - y1) * (x - x1) / (x2 - x1)
        else:
            y = y1
        return (x, y)
    elif edge == 'right':
        x = clip_window['right']
        if x2 - x1 != 0:
            y = y1 + (y2 - y1) * (x - x1) / (x2 - x1)
        else:
            y = y1
        return (x, y)
    elif edge == 'bottom':
        y = clip_window['bottom']
        if y2 - y1 != 0:
            x = x1 + (x2 - x1) * (y - y1) / (y2 - y1)
        else:
            x = x1
        return (x, y)
    elif edge == 'top':
        y = clip_window['top']
        if y2 - y1 != 0:
            x = x1 + (x2 - x1) * (y - y1) / (y2 - y1)
        else:
            x = x1
        return (x, y)

def clip_polygon_against_edge(vertices, edge):
    """Clip polygon against a single edge using Sutherland-Hodgman algorithm"""
    if len(vertices) == 0:
        return []
    clipped_vertices = []
    if len(vertices) > 0:
        # Start with the last vertex
        prev_vertex = vertices[-1]
        for current_vertex in vertices:
            # Check if current vertex is inside
            if is_inside(current_vertex, edge):
                # If previous vertex was outside, add intersection
                if not is_inside(prev_vertex, edge):
                    intersection = compute_intersection(prev_vertex, current_vertex, edge)
                    clipped_vertices.append(intersection)
                # Add current vertex
                clipped_vertices.append(current_vertex)
            else:
                # Current vertex is outside
                # If previous vertex was inside, add intersection
                if is_inside(prev_vertex, edge):
                    intersection = compute_intersection(prev_vertex, current_vertex, edge)
                    clipped_vertices.append(intersection)
            prev_vertex = current_vertex
    return clipped_vertices

def sutherland_hodgman_clip(vertices):
    """Apply Sutherland-Hodgman clipping algorithm"""
    # Clip against each edge in order: left, right, bottom, top
    edges = ['left', 'right', 'bottom', 'top']
    clipped_polygon = vertices[:]
    for edge in edges:
        clipped_polygon = clip_polygon_against_edge(clipped_polygon, edge)
        if len(clipped_polygon) == 0:
            break
    return clipped_polygon

def draw_text_info():
    """Draw information text"""
    pen.penup()
    pen.goto(50, 650)
    pen.color("black")
    pen.write("Sutherland-Hodgman Polygon Clipping Algorithm", font=("Arial", 16, "bold"))
    pen.goto(50, 620)
    pen.write("Blue: Original polygon", font=("Arial", 12, "normal"))
    pen.goto(50, 600)
    pen.write("Blue: Clipped polygon", font=("Arial", 12, "normal"))
    pen.goto(50, 580)
    pen.write("Red: Clipping window", font=("Arial", 12, "normal"))
    


def main():
    # Draw information text
    draw_text_info()
    # Draw clipping window
    draw_clipping_window()
    # Example 1: Polygon that intersects the clipping window
    original_polygon1 = [
        (100, 400),
        (300, 400),
        (400, 500),
        (500, 400),
        (700, 400),
        (550, 250),
        (500, 100),
        (400, 200),
        (300, 100),
        (250, 250),

    ]
    
    # Draw original polygon
    draw_polygon(original_polygon1, "blue")
    # Apply Sutherland-Hodgman clipping
    clipped_polygon1 = sutherland_hodgman_clip(original_polygon1)
    # Draw clipped polygon
    if clipped_polygon1:
        draw_polygon(clipped_polygon1, "blue", fill=True)
    # Add labels with arrows pointing to polygons
    pen.penup()
    pen.goto(135, 370)
    pen.color("black")
    pen.write("Original", font=("Arial", 10, "bold"))
    if clipped_polygon1:
        pen.goto(350, 300)
        pen.color("black")
        pen.write("Clipped", font=("Arial", 10, "bold"))
    # Example 2: Another polygon (smaller, to show different clipping result)
    pen.penup()
    pen.goto(50, 100)
    pen.color("cyan")
    pen.hideturtle()
    screen.exitonclick()

if __name__ == "__main__":
    main()