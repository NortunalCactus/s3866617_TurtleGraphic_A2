import turtle
from os import path


def drawRect(t, w, h, x, y, fill):
    mat = ((1, 0), (1, 1), \
           (0, 1), (0, 0))
    t.up()
    t.goto(x, y)
    t.pencolor(fill)
    t.fillcolor(fill)
    t.down()
    t.begin_fill()
    for i, j in mat:
        t.goto(x + i * w, y + j * h)
    t.end_fill()
    t.up()


def drawPath(t, pts, width, outline, fill):
    t.up()
    t.goto(*pts[0])
    t.pencolor(outline)
    t.width(width)
    t.down()
    if fill:
        t.fillcolor(fill)
        t.begin_fill()
    for point in pts:
        t.goto(*point)
    if fill:
        t.end_fill()
    t.up()


def svgPathToCoords(path):
    start = False
    isRelative = True
    path = path.split()

    pts = []
    for e in path:
        if e == 'm' or e == 'c':
            start = True
            isRelative = True
        elif e == 'M' or e == 'C':
            start = True
            isRelative = False
        elif e == 'z' or e == 'Z':
            start = False
            if pts:
                pts.append(pts[0])  # Close path w/straight line
        elif start == True and "," in e:
            x, y = e.split(",")[:2]
            x = float(x)
            y = float(y)
            if isRelative and pts:
                pts.append((pts[-1][0] + x, pts[-1][1] + y))
            else:
                pts.append((x, y))
        # else: print ("Unknown parameter:", e)
    return pts


def lines(f):
    """ Takes file f and returns contents as a list of lines """
    lines = []

    if path.exists(f):
        fp = open(f)
        lines = [line.strip() for line in fp]
        fp.close()

    return lines


def parsePaths(f):
    paths = []
    start = False

    path = [None, None, None, None]
    for line in lines(f):
        if line == "path-start":
            start = True
        elif line == "path-end":
            start = False
            paths.append(tuple(path))
            path = [None, None, None, None]
        else:
            split = line.find(" ")
            attrib = (line[:split], line[split + 1:])
            if attrib[0] == "stroke-width":
                path[1] = float(attrib[1])
            elif attrib[0] == "stroke":
                path[2] = attrib[1]
            elif attrib[0] == "fill":
                if attrib[1] == "none":
                    path[3] = None
                else:
                    path[3] = attrib[1]
            elif attrib[0] == "path":
                path[0] = svgPathToCoords(attrib[1])
    return paths


""" Wales data """
rectData = [(900, 600, 0, 0, "#de2910")]


def drawHK(w):
    t = turtle.Turtle()
    t.screen.setup(900, 600)
    t.screen.setworldcoordinates(0, 600, 900, 0)
    for rect in rectData:
        print(rect)
        drawRect(t, *rect)
    for path in parsePaths("Hong Kong.txt"):
        drawPath(t, *path)
    t.screen.mainloop()