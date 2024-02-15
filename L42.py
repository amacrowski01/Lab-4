import turtle
amy=turtle.Turtle()
turtle.color("yellow")

for side in range(4):
    if side==0:
        amy.color("yellow")
    if side==1:
        amy.color("violet")
    if side==2:
        amy.color("blue")
    if side==3:
        amy.color("magenta")
    amy.forward(100)
    amy.right(90)
    
