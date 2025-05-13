import turtle


def draw_star(side_length):
    for _ in range(5):  
        turtle.forward(side_length)
        turtle.right(144)  


turtle.speed(10)  


for _ in range(5):
    draw_star(100)  
    turtle.penup()
    turtle.forward(350)  
    turtle.right(144)  
    turtle.pendown()


turtle.exitonclick()
