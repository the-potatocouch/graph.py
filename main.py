import pygame
import time

background_colour = (255, 255, 255)

line_color = (52, 137, 227)

(width, height) = (400, 400)

screen = pygame.display.set_mode((width, height))

screen.fill(background_colour)


def circ(surface, color, pos, dia):

    pygame.draw.circle(surface, color, pos, dia)


def graph(x, b, xvalue):

    equation = ""

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

        equation = equation + " + " + str(b)

    return equation


def displaygraph(x, h, b, inbetween):

    hwidth = height / 2
    hheight = height / 2

    pygame.display.set_caption(windowtext(x, h, b))

    inbetween = inbetween * -1
    count = width * -1

    while count <= width + 1:

        circ(screen, (0, 0, 0), (hwidth, count), 1)
        circ(screen, (0, 0, 0), (count, hheight), 1)

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


running = True

do_once = True

while running:

    if do_once is True:

        drawaxes = width * -1
        pygame.display.flip()
        displaygraph(2/9, 20, 60, 2)

        do_once = False

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
