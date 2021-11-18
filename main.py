import pygame


background_colour = (255, 255, 255)

(width, height) = (400, 400)

screen = pygame.display.set_mode((width, height))

screen.fill(background_colour)


def circ(surface, color, pos, dia):

    pygame.draw.circle(surface, color, pos, dia)


def graph(x, h, b, xvalue):

    equation = ""

    if x != 0:

        equation = equation + str(x) + " * "

    if h != 0:

        if h <= 0:

            equation = equation + \
                "(" + str(xvalue) + " + " + str(abs(h)) + ")**2"

        elif h >= 0:

            equation = equation + \
                "(" + str(xvalue) + " - " + str(abs(h)) + ")**2"

    if h == 0 or h == 1:

        equation = equation + str(xvalue) + "**2"

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


def displaygraph(x, h, b):

    hwidth = height / 2
    hheight = height / 2

    pygame.display.set_caption(windowtext(x, h, b))

    count = -401

    while count <= 401:

        if abs(eval(graph(x, h, b, count))) <= height:

            if count < 1:

                pos = (count + hwidth - h,
                       ((eval(graph(x, h, b, count))) * -1) + hheight)
                circ(screen, (52, 137, 227), pos, 3)

            else:

                pos = (count + hwidth - h, eval(graph(x, h, b, count)) + hheight)
                circ(screen, (52, 137, 227), pos, 3)

        circ(screen, (0, 0, 0), (hwidth, count), 1)
        circ(screen, (0, 0, 0), (count, hheight), 1)

        count += 1


running = True


while running:

    displaygraph(2/9, 20, 60)

    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
