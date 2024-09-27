import turtle

def draw_oval(radius, angle):
    for _ in range(2):  # Draw an ellipse by modifying the circle method
        turtle.circle(radius, angle)  # Draw the long side of the ellipse
        turtle.circle(radius//4, angle)  # Draw the short side

# Screen setup
screen = turtle.Screen()
screen.title("Cow Drawing with Turtle")

# Turtle setup
cow = turtle.Turtle()
cow.speed(1)  # Slow drawing speed to see the progress

# Draw body
cow.penup()
cow.goto(-50, 0)  # Start position
cow.pendown()
cow.color("black")
draw_oval(50, 90)  # Draw an oval for the body

# Draw head
cow.penup()
cow.goto(0, 50)  # Position the turtle to head start
cow.pendown()
cow.circle(30)  # Head as a circle

# Draw eyes
cow.penup()
cow.goto(-10, 70)  # Position for left eye
cow.pendown()
cow.dot(5)

cow.penup()
cow.goto(10, 70)  # Position for right eye
cow.pendown()
cow.dot(5)

# Draw ears
cow.penup()
cow.goto(-35, 75)
cow.pendown()
cow.circle(10, 180)  # Left ear as a half circle

cow.penup()
cow.goto(15, 75)
cow.pendown()
cow.circle(-10, 180)  # Right ear as a half circle

# Draw legs
cow.penup()
cow.goto(-40, -10)
cow.pendown()
cow.right(90)
cow.forward(30)  # Front left leg

cow.penup()
cow.goto(10, -10)
cow.pendown()
cow.forward(30)  # Front right leg

# Draw tail
cow.penup()
cow.goto(-70, 10)
cow.pendown()
cow.left(30)
cow.forward(40)  # Tail sticking out

# Hide turtle and finish
cow.hideturtle()
screen.mainloop()