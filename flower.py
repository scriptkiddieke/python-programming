import turtle
import random

def draw_petal(t, radius, angle):
    for _ in range(2):
        t.circle(radius, angle)
        t.left(180 - angle)

def draw_flower(t, num_petals, radius, angle, petal_colors):
    for i in range(num_petals):
        t.color(petal_colors[i % len(petal_colors)])
        draw_petal(t, radius, angle)
        t.left(360 / num_petals)

def draw_center(t, radius, num_layers):
    colors = ["yellow", "orange"]
    for i in range(num_layers):
        t.penup()
        t.goto(0, -radius + i*radius/num_layers)
        t.pendown()
        t.color(colors[i % len(colors)])
        t.begin_fill()
        t.circle(radius - i*radius/num_layers)
        t.end_fill()

def draw_stem(t, length, width):
    t.color("green")
    t.width(width)
    t.right(90)
    t.forward(length)

def draw_leaf(t, length, width):
    t.color("green")
    t.begin_fill()
    t.circle(width, 90)
    t.left(90)
    t.circle(width, 90)
    t.end_fill()

def main():
    # Set up the screen
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Create a turtle named "flower"
    flower = turtle.Turtle()
    flower.shape("turtle")
    flower.speed(10)

    # Draw the flower petals
    petal_colors = ["red", "pink", "purple"]
    flower.penup()
    flower.goto(0, 0)
    flower.pendown()
    draw_flower(flower, num_petals=12, radius=100, angle=60, petal_colors=petal_colors)

    # Draw the center of the flower
    flower.penup()
    flower.goto(0, -20)
    flower.pendown()
    draw_center(flower, radius=20, num_layers=2)

    # Draw the stem
    flower.penup()
    flower.goto(0, -20)
    flower.setheading(-90)
    flower.pendown()
    draw_stem(flower, length=200, width=10)

    # Draw leaves
    flower.penup()
    flower.goto(0, -120)
    flower.setheading(-45)
    flower.pendown()
    draw_leaf(flower, length=100, width=50)

    flower.penup()
    flower.goto(0, -150)
    flower.setheading(-135)
    flower.pendown()
    draw_leaf(flower, length=100, width=50)

    # Hide the turtle and display the result
    flower.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
