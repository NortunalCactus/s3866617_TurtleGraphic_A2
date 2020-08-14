import turtle



jem = turtle.Screen()
jem.bgcolor("pink")

nina = turtle.Turtle()
nina.pensize(0.5)
nina.pu()
nina.setposition(-600.00,300.00)
nina.pd()
nina.speed(20)


def draw_flag():
    nina.fillcolor("dark blue")
    nina.begin_fill()
    for i in range(2):
        nina.fd(1200)
        nina.right(90)
        nina.fd(600)
        nina.right(90)
    nina.end_fill()
draw_flag()

def main_program_uk():

    width = 600
    height = 300

    def draw_rec(w,h):
        for i in range(2):
            nina.fillcolor('white')
            nina.begin_fill()
            nina.fd(w)
            nina.right(90)
            nina.fd(h)
            nina.right(90)
            nina.end_fill()
    draw_rec(width, height)


    def draw_redcross(w , h):
        defaultColor = 'red'
        nina.pencolor(defaultColor)
        nina.fillcolor(defaultColor)
        nina.penup()
        nina.goto(-600,)
        nina.pendown()
        nina.begin_fill()
        for i in range(2):      #drawing the horizontal red rectangle
            nina.fd(w)
            nina.right(90)
            nina.fd(h/5)
            nina.right(90)
        nina.penup()
        nina.goto(30,150)
        nina.pendown() 
        nina.right(90)
        for m in range(2):      #drawing the vertical rectangle
            nina.fd(h)
            nina.right(90)
            nina.fd(h/5)
            nina.right(90)

        nina.end_fill()

        #pass

    draw_redcross(width , height)

    def draw_triangle():
        defaultColor = 'dark blue'
        nina.penup()
        nina.goto(-50, 150)
        nina.pendown()
        nina.pencolor(defaultColor)
        nina.fillcolor(defaultColor)
        nina.begin_fill()
        for i in range(2):          #drawing the blue triangles on the top left, and bottom right corners
            nina.fd(95)
            nina.right(116.5650512)  #these numbers are calculated using trigonometry
            nina.fd(212.4264579)
            nina.right(153.4349488)
            nina.fd(190)
            nina.left(90)
            nina.penup()
            nina.goto(50, -150)
            nina.pendown()
        nina.end_fill()
        nina.penup()
        nina.left(180)
        nina.goto(-50, -150)
        nina.pendown()
        nina.begin_fill()
        for i in range(2):          #drawing the blue triangles on the top right, and bottom left corners
            nina.fd(95)
            nina.left(116.5650512)  #these numbers are calculated using trigonometry
            nina.fd(212.4264579)
            nina.left(153.4349488)
            nina.fd(190)
            nina.right(90)
            nina.penup()
            nina.goto(50,150)
            nina.pendown()
        nina.end_fill()
        def draw_vertical_triangle():
            nina.penup()
            nina.goto(300, 50)
            nina.pendown()
            nina.begin_fill()
            for i in range(2):
                nina.fd(70)
                nina.left(116.5650512)
                nina.forward(156.5247583)
                nina.left(153.4349488)
                nina.fd(140)
                nina.right(90)
                nina.penup()
                nina.goto(-300,-50)
                nina.pendown()
            nina.end_fill()
            nina.goto(-300, 50)
            nina.pendown()
            nina.begin_fill()
            for i in range(2):
                nina.fd(70)
                nina.right(116.5650512)
                nina.forward(156.5247583)
                nina.right(153.4349488)
                nina.fd(140)
                nina.left(90)
                nina.penup()
                nina.goto(300, -50)
                nina.pendown()
            nina.end_fill()
        draw_vertical_triangle()
    draw_triangle()

    def draw_diagonal_lines():
        defaultColor = 'red'
        nina.pencolor(defaultColor)
        nina.right(180-116.5650512)
        nina.penup()
        nina.goto(-300, -150)
        nina.pendown()
        nina.fillcolor(defaultColor)
        nina.begin_fill()
        for i in range(2):
            nina.fd(220)
            nina.right(116.5650512-90)
            nina.fd(40)
            nina.right(90+180-116.5650512)
        nina.right(180)
        nina.penup()
        nina.goto(300, 150)
        nina.pendown()
        nina.end_fill()
        nina.begin_fill()
        for i in range(2):
            nina.fd(220)
            nina.right(116.5650512-90)
            nina.fd(40)
            nina.right(90+180-116.5650512)
        nina.end_fill()
        nina.penup()
        nina.goto(300, -150)
        nina.pendown()
        nina.right(52.5)
        def draw_the_rest():
            for i in range(2):
                nina.forward(188.6796226)
                nina.right(180-26.5650512)
                nina.fd(25)
                nina.right(26.5650512)
                nina.fd(170)
                nina.right(180-116.5650512)
                nina.fd(20)

        draw_the_rest()

    draw_diagonal_lines()
main_program_uk()









jem.exitonclick()

