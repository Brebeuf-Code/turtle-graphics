import turtle

t = turtle.Turtle()

for c in range(1000):
    t.speed(10)
    if c%20<10:
        t.color('red')
    else:
        t.color('purple')
    t.forward((c)%3*40+40)
    t.left(101)import turtle

t = turtle.Turtle()

for c in range(1000):
    t.speed(10)
    if c%20<10:
        t.color('red')
    else:
        t.color('purple')
    t.forward((c)%3*40+40)
    t.left(101)