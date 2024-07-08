import tkinter as tk
import random

# Create the main application window
root = tk.Tk()
root.title("Advanced Interactive Cursor Follow Effect")
root.geometry("800x600")  # Set the size of the window

# Create a canvas widget
canvas = tk.Canvas(root, width=800, height=600, bg="white")
canvas.pack()

# Initialize the shape properties
circle_radius = 10
trail_length = 10  # Number of shapes in the trail
trail = []
shape_type = "circle"  # Default shape
background_color = "white"

# Function to generate a random color
def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

# Function to update the position of the shape and add trail effect
def follow_cursor(event):
    global trail

    # Get the cursor position
    x, y = event.x, event.y

    # Draw the shape at the cursor position
    if shape_type == "circle":
        shape = canvas.create_oval(x - circle_radius, y - circle_radius, x + circle_radius, y + circle_radius, fill=random_color(), outline="")
    elif shape_type == "square":
        shape = canvas.create_rectangle(x - circle_radius, y - circle_radius, x + circle_radius, y + circle_radius, fill=random_color(), outline="")
    elif shape_type == "triangle":
        shape = canvas.create_polygon(x, y - circle_radius, x - circle_radius, y + circle_radius, x + circle_radius, y + circle_radius, fill=random_color(), outline="")

    trail.append(shape)

    # Keep the trail length constant
    if len(trail) > trail_length:
        canvas.delete(trail.pop(0))

# Function to increase the shape size
def increase_size(event):
    global circle_radius
    circle_radius += 2

# Function to decrease the shape size
def decrease_size(event):
    global circle_radius
    if circle_radius > 2:
        circle_radius -= 2

# Function to increase the trail length
def increase_trail(event):
    global trail_length
    trail_length += 1

# Function to decrease the trail length
def decrease_trail(event):
    global trail_length
    if trail_length > 1:
        trail_length -= 1

# Function to change the shape type
def change_shape(event):
    global shape_type
    shape_types = ["circle", "square", "triangle"]
    current_index = shape_types.index(shape_type)
    shape_type = shape_types[(current_index + 1) % len(shape_types)]

# Function to change the background color
def change_bg_color(event):
    global background_color
    background_color = random_color()
    canvas.config(bg=background_color)

# Bind the mouse motion event to the follow_cursor function
canvas.bind("<Motion>", follow_cursor)
# Bind keys to their respective functions
root.bind("<Up>", increase_size)
root.bind("<Down>", decrease_size)
root.bind("<Right>", increase_trail)
root.bind("<Left>", decrease_trail)
root.bind("s", change_shape)
root.bind("b", change_bg_color)

# Start the main event loop
root.mainloop()
