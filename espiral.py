from jupyturtle import make_turtle, forward, left
import turtle

# Criando uma tela e uma tartaruga
screen = turtle.Screen()
t = turtle.Turtle()

def spiral(turn_angle, step_increment, num_steps):
    """
    Draws a spiral using the turtle module.

    Parameters:
    - turn_angle: The angle (in degrees) the turtle turns after each step.
    - step_increment: How much longer each subsequent step becomes.
    - num_steps: Total number of steps in the spiral.
    """
    step_length = 0  # Initial step length

    for _ in range(num_steps):
        t.forward(step_length)
        t.left(turn_angle)
        step_length += step_increment  # Increment the step length



# Draw a spiral
spiral(turn_angle=20, step_increment=2, num_steps=100)