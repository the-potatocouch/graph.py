import pygame
import random


#default: (255, 255, 255)
background_colour = (232, 224, 209)

#default: (52, 137, 227)
line_color = (100, 100, 100)

#default: (0, 0, 0)
axis_color = (0, 0, 0)

(width, height) = (800, 400)

screen = pygame.display.set_mode((width, height))

screen.fill(background_colour)

icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)


def circ(surface, color, pos, dia):

    pygame.draw.circle(surface, color, pos, dia)


def graph(x, b, xvalue):

    equation = ""

    xvalue = xvalue * -1

    if x != 0:

        equation = equation + str(x) + " * "

    equation = equation + str(xvalue) + " ** 2"

    if b != 0:

        equation = equation + " + " + str(b)

    return(equation)


def windowtext(x, h, b):

    equation = ""

    equation = "y = "

    if x != 0:

        equation = equation + str(x)

    if h != 0:

        if h <= 0:

            equation = equation + "(x + " + str(abs(h)) + ")²"

        elif h >= 0:

            equation = equation + "(x - " + str(abs(h)) + ")²"

    if h == 0:

        equation = equation + "x²"

    if b != 0:

        equation = equation + " + " + str(abs(b))

    equation = equation + " | PotatoCouch's graph visualiser"
    return equation


def displaygraph(x, h, b, inbetween):

    hwidth = width / 2
    hheight = height / 2
    inbetween = inbetween * -1
    count = width * -1
    ng_h = height * -1

    if x == "random":
        x = random.uniform(0.00000001, 100)

    if h == "random":
        h = random.uniform(count, hwidth)

    if b == "random":
        b = random.uniform(ng_h, hheight)

    pygame.display.set_caption(windowtext(x, h, b))

    while count <= width + 1:

        if abs(eval(graph(x, b, count))) <= height:

            if count < 0:

                pos = (count + hwidth + h,
                       ((eval(graph(x, b, count))) * -1) + hheight)
                circ(screen, line_color, pos, 1)

            else:

                pos = (count + hwidth + h,
                       eval(graph(x, (b * -1), count)) + hheight)
                circ(screen, line_color, pos, 1)

        pygame.display.flip()

        count += 1 * 10 ** inbetween


def drawlines(axiscolor):

    count = width * -1

    hwidth = width / 2
    hheight = height / 2

    while count <= width + 1:

        circ(screen, axiscolor, (hwidth, count), 1)
        circ(screen, axiscolor, (count, hheight), 1)

        if count % 20 == 0:
            circ(screen, axiscolor, (hwidth, count), 3)
            circ(screen, axiscolor, (count, hheight), 3)
        pygame.display.flip()
        count += 1


running = True

do_once = True

while running:

    if do_once is True:

        drawaxes = width * -1
        pygame.display.flip()
        drawlines(axis_color)
        displaygraph("random", "random", "random", 1)

        do_once = False

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
