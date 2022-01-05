import random

import pygame
import pygame.draw.circle as circ

# default: (255, 255, 255)
BG_COLOUR = (232, 224, 209)

# default: (52, 137, 227)
LINE_COLOUR = (100, 100, 100)

# default: (0, 0, 0)
AXIS_COLOUR = (0, 0, 0)

WIDTH,HEIGHT) = (800, 400)

SCREEN = pygame.display.set_mode(WIDTH,HEIGHT))

screen.fill(BG_COLOUR)

icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)


def graph(x, b, xvalue):
    equation = ""
    xvalue = xvalue * -1

    if x != 0:
        equation = equation + str(x) + " * "

    equation = equation + str(xvalue) + " ** 2"

    if b != 0:
        equation = equation + " + " + str(b)

    return equation


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

    hwidth = WIDTH / 2
    hheight = HEIGHT / 2
    inbetween = inbetween * -1
    count = WIDTH * -1
    ng_h = HEIGHT * -1

    if x == "random":
        x = random.uniform(0.00000001, 100)

    if h == "random":
        h = random.uniform(count, hwidth)

    if b == "random":
        b = random.uniform(ng_h, hheight)

    pygame.display.set_caption(windowtext(x, h, b))

    while count <= WIDTH + 1:

        if abs(eval(graph(x, b, count))) <= HEIGHT:

            if count < 0:

                pos = (count + hwidth + h, ((eval(graph(x, b, count))) * -1) + hheight)
                circ(screen, line_color, pos, 1)

            else:

                pos = (count + hwidth + h, eval(graph(x, (b * -1), count)) + hheight)
                circ(screen, line_color, pos, 1)

        pygame.display.flip()

        count += 1 * 10 ** inbetween


def drawlines(AXIS_COLOUR):

    count = WIDTH * -1

    hwidth = WIDTH / 2
    hheight = HEIGHT / 2

    while count <= WIDTH + 1:

        circ(screen, AXIS_COLOUR, (hwidth, count), 1)
        circ(screen, AXIS_COLOUR, (count, hheight), 1)

        if count % 20 == 0:
            circ(screen, AXIS_COLOUR, (hwidth, count), 3)
            circ(screen, AXIS_COLOUR, (count, hheight), 3)
        pygame.display.flip()
        count += 1


running = True

do_once = True

while running:

    if do_once is True:

        drawaxes = WIDTH * -1
        pygame.display.flip()
        drawlines(axis_color)
        displaygraph(20 / 10000, 10, 10, 1)

        do_once = False

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
