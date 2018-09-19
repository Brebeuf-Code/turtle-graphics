import turtle

t = turtle.Turtle()
t.pensize(0.1)

for c in range(80):
    for i in range(3):
        t.speed(10)
        if c%30<10:
            t.color('red')
        elif c%30<20:
            t.color('purple')
        else:
            t.color('blue')
        t.forward((80-c))
        t.left(122)