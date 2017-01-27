import turtle

def draw_triangle():
    triangle = turtle.Turtle()
    triangle.shape("arrow")
    triangle.shapesize(2,2,2)
    triangle.color("orange")
    triangle.speed(10)
    for i in range(0,50):
       for j in range(0,2):
           triangle.forward(100)
           triangle.left(120)
       triangle.left(5)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")
    draw_square()
    draw_triangle()
    window.exitonclick()
   

    
def draw_square():
    brad = turtle.Turtle()
    brad.speed(10)
    brad.shape("turtle")
    brad.color("pink")

    angie = turtle.Turtle()
    angie.speed(10)
    angie.shape("arrow")
    angie.color("green")

    outer = turtle.Turtle()
    outer.speed(10)
    outer.shape("arrow")
    outer.color("red")

#    for i in range(0,5):
#       for j in range(0,4):
#          outer.left(90)
#          outer.forward(170)
#       outer.left(10)
       
    for i in range(0,80):
       for j in range(0,4):
          brad.left(90)
          brad.forward(110)
       brad.left(7)

#    for i in range(0,74):
#       for j in range(0,4):
#          angie.left(90)
#          angie.forward(70)
#       angie.left(5)

draw_art()
