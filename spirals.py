import turtle


turtle.speed(100)  

def reg_spiral():    
    side_length = 5  
    angle = 90  

    for _ in range(100):  
        turtle.forward(side_length)
        turtle.right(angle)
        side_length += 2  

def cool_spiral():
    side_length = 5  
    angle = 89  

    for _ in range(100):  
        turtle.forward(side_length)
        turtle.right(angle)
        side_length += 2  

#uncomment these two calls below
#reg_spiral() 
#cool_spiral()

turtle.exitonclick()
