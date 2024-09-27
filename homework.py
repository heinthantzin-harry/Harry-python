import turtle

# Screen setup
screen = turtle.Screen()
screen.title("Simple Robot Drawing with Turtle")

# Turtle setup
robot = turtle.Turtle()
robot.speed(1)

def draw_rectangle(t, width, height):
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

# Draw body
robot.penup()
robot.goto(-50, -50)
robot.pendown()
robot.color("gray")
draw_rectangle(robot, 100, 150)  # Body of the robot

# Draw head
robot.penup()
robot.goto(-30, 100)
robot.pendown()
robot.color("gray")
draw_rectangle(robot, 60, 60)  # Head of the robot

# Draw eyes
robot.penup()
robot.goto(-20, 140)
robot.pendown()
robot.dot(10, "black")  # Left eye

robot.penup()
robot.goto(20, 140)
robot.pendown()
robot.dot(10, "black")  # Right eye

# Draw mouth
robot.penup()
robot.goto(-15, 120)
robot.pendown()
robot.forward(30)  # Simple mouth line

# Draw left arm
robot.penup()
robot.goto(-50, 50)
robot.pendown()
robot.left(90)
robot.forward(40)  # Left arm

# Draw right arm
robot.penup()
robot.goto(50, 50)
robot.pendown()
robot.forward(40)  # Right arm

# Draw legs
robot.penup()
robot.goto(-30, -50)
robot.pendown()
robot.right(90)
robot.forward(50)  # Left leg

robot.penup()
robot.goto(30, -50)
robot.pendown()
robot.forward(50)  # Right leg

# Hide turtle and finish
robot.hideturtle()
screen.mainloop()