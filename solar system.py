import turtle
import math
import random

# Setup the screen
window = turtle.Screen()
window.bgcolor("black")
window.title("Interactive Solar System with Cursor Following Stars")
window.tracer(0)

# Create the turtle for drawing the Sun
sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.shapesize(2, 2)
sun.penup()

# Function to draw a planet
def draw_planet(planet, radius, color, distance):
    planet.shape("circle")
    planet.color(color)
    planet.shapesize(radius / 10)  # Adjust size for better visibility
    planet.penup()
    planet.goto(distance, 0)
    planet.pendown()

# Create turtles for planets
mercury = turtle.Turtle()
venus = turtle.Turtle()
earth = turtle.Turtle()
mars = turtle.Turtle()
jupiter = turtle.Turtle()
saturn = turtle.Turtle()
uranus = turtle.Turtle()
neptune = turtle.Turtle()

# Draw the planets with different colors and distances from the Sun
draw_planet(mercury, 4, "gray", 40)
draw_planet(venus, 5, "orange", 70)
draw_planet(earth, 6, "blue", 100)  # Corrected function call
draw_planet(mars, 5, "red", 150)
draw_planet(jupiter, 8, "brown", 200)
draw_planet(saturn, 7, "yellow", 250)
draw_planet(uranus, 6, "light blue", 300)
draw_planet(neptune, 6, "blue", 350)

# Function to move the planets in a circular orbit
def move_planet(planet, distance, speed, angle):
    angle += speed
    x = distance * math.cos(math.radians(angle))
    y = distance * math.sin(math.radians(angle))
    planet.goto(x, y)
    return angle

# Initialize angles for each planet
angles = {
    "mercury": 0,
    "venus": 0,
    "earth": 0,
    "mars": 0,
    "jupiter": 0,
    "saturn": 0,
    "uranus": 0,
    "neptune": 0
}

# Function to create a star
def create_star(x, y):
    star = turtle.Turtle()
    star.shape("circle")
    star.color(random_color())
    star.shapesize(0.2)
    star.penup()
    star.goto(x, y)
    return star

# Function to generate a random color
def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

# List to keep track of stars
stars = []

# Function to update the position of stars to follow the cursor
def follow_cursor(x, y):
    global stars
    star = create_star(x, y)
    stars.append(star)
    if len(stars) > 50:  # Limit the number of stars
        old_star = stars.pop(0)
        old_star.hideturtle()
        old_star.clear()

# Function to track the cursor position and create stars
def track_cursor():
    x, y = turtle.getcanvas().winfo_pointerx() - window.window_width() // 2, \
           window.window_height() // 2 - turtle.getcanvas().winfo_pointery()
    follow_cursor(x, y)
    window.ontimer(track_cursor, 50)

# Bind the mouse click event to the follow_cursor function
window.onscreenclick(follow_cursor)

# Start tracking the cursor
track_cursor()

# Move the planets with different speeds
while True:
    angles["mercury"] = move_planet(mercury, 40, 8, angles["mercury"])
    angles["venus"] = move_planet(venus, 70, 4, angles["venus"])
    angles["earth"] = move_planet(earth, 100, 2, angles["earth"])
    angles["mars"] = move_planet(mars, 150, 1.6, angles["mars"])
    angles["jupiter"] = move_planet(jupiter, 200, 1, angles["jupiter"])
    angles["saturn"] = move_planet(saturn, 250, 0.6, angles["saturn"])
    angles["uranus"] = move_planet(uranus, 300, 0.4, angles["uranus"])
    angles["neptune"] = move_planet(neptune, 350, 0.2, angles["neptune"])
    window.update()

# Keep the window open
turtle.done()
