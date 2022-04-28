from turtle import Turtle           
import numpy as np
import matplotlib.pyplot as plt

VCOEF = 1.1                         # Coefficient for accelerating and decelerating of the hunter

def init_hunter(x=-400, y=300):
    """ Initializes the hunter object """
    hunter = Turtle()
    hunter.penup()
    hunter.speed(0)                 # Animace speed (0 - highest; not related with physical velocities)
    hunter.color("green")
    hunter.setposition(x, y)
    hunter.pendown()

    return hunter

def init_dog(x=-400, y=-300):
    """ Initializes the dog object """
    dog = Turtle()
    dog.penup()
    dog.speed(0)
    dog.color("red")
    dog.setposition(x, y)
    dog.pendown()

    return dog

def chasing_curve_straight(hunter_velocity=2, dog_velocity=10, dt=1):
    """ Straight motion of the hunter """
    hunter = init_hunter()
    dog = init_dog()

    hunter_screen = hunter.getscreen()
    hunter_screen.delay(1)          # This speeds up the animation

    while hunter.distance(dog) > dog_velocity * dt:
        hunter.forward(dt * hunter_velocity)
        dog.setheading(dog.towards(hunter))
        dog.forward(dt * dog_velocity)

def chasing_curve_circle(hunter_velocity=2, dog_velocity=5, hunter_turn_velocity=0.5, dt=1):
    """ Circular motion of the hunter """
    hunter = init_hunter(x=0)
    dog = init_dog()

    hunter_screen = hunter.getscreen()
    hunter_screen.delay(1)          # This speeds up the animation

    while hunter.distance(dog) > dog_velocity * dt:
        hunter.forward(dt * hunter_velocity)
        hunter.right(hunter_turn_velocity)
        dog.setheading(dog.towards(hunter))
        dog.forward(dt * dog_velocity)

def chasing_curve_events(hunter_velocity=2, dog_velocity=5, dt=1):
    """ Chasing curve with interactive hunter 
        (left key - turn left, right key - turn right, up key - accelerate, down key - decelerate)
    """

    hunter = init_hunter()
    dog = init_dog()

    def left_event():
        hunter.left(3)

    def right_event():
        hunter.right(3)

    def up_event():
        nonlocal hunter_velocity
        hunter_velocity *= VCOEF

    def down_event():
        nonlocal hunter_velocity
        hunter_velocity /= VCOEF

    hunter_screen = hunter.getscreen()
    hunter_screen.delay(1)          # This speeds up the animation
    hunter_screen.onkeypress(left_event, "Left")
    hunter_screen.onkeypress(right_event, "Right")
    hunter_screen.onkeypress(up_event, "Up")
    hunter_screen.onkeypress(down_event, "Down")
    hunter_screen.listen()          # Necessary for the screen to listen to the events

    while hunter.distance(dog) > dog_velocity * dt:
        hunter.forward(dt * hunter_velocity)
        dog.setheading(dog.towards(hunter))
        dog.forward(dt * dog_velocity)

def chasing_curve_acceleration(hunter_velocity=2, dog_velocity=5, dt=1):
    """ Chasing curve with interactive hunter 
        (left key - turn left, right key - turn right, up key - accelerate, down key - decelerate)
    """

    hunter = init_hunter()
    dog = init_dog()

    def left_event():
        hunter.left(3)

    def right_event():
        hunter.right(3)

    def up_event():
        nonlocal hunter_velocity
        hunter_velocity *= VCOEF

    def down_event():
        nonlocal hunter_velocity
        hunter_velocity /= VCOEF

    hunter_screen = hunter.getscreen()
    hunter_screen.delay(1)          # This speeds up the animation
    hunter_screen.onkeypress(left_event, "Left")
    hunter_screen.onkeypress(right_event, "Right")
    hunter_screen.onkeypress(up_event, "Up")
    hunter_screen.onkeypress(down_event, "Down")
    hunter_screen.listen()          # Necessary for the screen to listen to the events

    plt.ion()
    plt.xlabel("$t\ [s]$")
    plt.ylabel("$a\ [ms^{-2}]$")

    t = 0

    while hunter.distance(dog) > dog_velocity * dt:
        hunter.forward(dt * hunter_velocity)

        phi1 = dog.heading()
        phi2 = dog.towards(hunter)

        dphi = phi2 - phi1
        dphi += 360
        dphi %= 360

        print(dphi)

        a = dog_velocity * dphi / dt

        dog.setheading(dog.towards(hunter))
        dog.forward(dt * dog_velocity)

        plt.scatter(t, a, color="black", s=1)

        t += dt

#chasing_curve_circle(hunter_velocity=10, hunter_turn_velocity=3)
#chasing_curve_events()

chasing_curve_acceleration()