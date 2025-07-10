#graphics design

import turtle as tr

def draw_pattern(colors):
    for i in range(3):
        for n in range(400):
            tr.color(colors[n % 4])
            tr.circle(190 - n / 2, 90)
            tr.left(90)
            tr.circle(190 - n / 2, 90)
            tr.color(colors[n % 4])
        tr.left(30)

s = tr.Screen()

tr.setup(800, 800)
s.bgcolor('#262626')
tr.pencolor('#540d6e')
tr.speed(120)
tr.tracer(100)
tr.pensize(1)

col1 = ('Coral', 'Goldenrod', 'Blue', 'Deep Pink')
col2 = ('Goldenrod', 'Blue', 'Coral', 'Deep Pink')

draw_pattern(col1)
draw_pattern(col2)
s.exitonclick()




