from turtle import Turtle, Screen
from itertools import cycle

letter_frequencies = [ \
    ('a', 10.52), ('b', 1.94), ('c', 6.91), ('d', 6.83), ('e', 22.65), \
    ('f', 9.42), ('g', 4.1), ('h', 4.68), ('i', 11.92), ('j', 0.56), \
    ('k', 1.2), ('l', 10.8), ('m', 3.29), ('n', 11.33), ('o', 12.95), \
    ('p', 5.83), ('q', 0.01), ('r', 11.14), ('s', 14.11), ('t', 14.69), \
    ('u', 4.05), ('v', 1.93), ('w', 2.96), ('x', 2.78), ('y', 3.02), ('z', 0.16)]

COLORS = cycle(['yellow', 'green', 'red', 'cyan', 'white', 'blue', 'mediumpurple'])

RADIUS = 175
LABEL_RADIUS = RADIUS * 1.33
FONTSIZE = 18
FONT = ("Ariel", FONTSIZE, "bold")

# The pie slices

total = sum(fraction for _, fraction in letter_frequencies)  # data doesn't sum to 100 so adjust

baker = Turtle()  # because we're baking a pie
baker.penup()
baker.sety(-RADIUS)
baker.pendown()

for _, fraction in letter_frequencies:
    baker.fillcolor(next(COLORS))
    baker.begin_fill()
    baker.circle(RADIUS, fraction * 360 / total)
    position = baker.position()
    baker.goto(0, 0)
    baker.end_fill()
    baker.setposition(position)

# The labels

baker.penup()
baker.sety(-LABEL_RADIUS)

for label, fraction in letter_frequencies:
    baker.circle(LABEL_RADIUS, fraction * 360 / total / 2)
    baker.write(label, align="center", font=FONT)
    baker.circle(LABEL_RADIUS, fraction * 360 / total / 2)

baker.hideturtle()

screen = Screen()
screen.exitonclick()