import turtle

turtle.bgcolor("black")

arv = turtle.Turtle()
arv.pensize(2)
arv.color("green")
arv.left(89)
arv.backward(70)
arv.speed(199999)

def drawTree(i):
    if i < 15:
        # print("Inside")
        return
    else:
        # print("Quitside")
        arv.forward(i)
        arv.color("magenta")
        arv.circle(2)
        arv.color("brown")
        arv.left(30)
        drawTree(3*i/4)
        arv.right(60)
        drawTree(3*i/4)
        arv.left(30)
        arv.backward(i)

drawTree(100)
turtle.done()