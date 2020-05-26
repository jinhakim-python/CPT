import pygame
import random
pygame.init()

#Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (124, 252, 0)
BLUE = (0, 191, 255)
ORANGE = (255, 140, 0)
RED = (255, 0, 0)
pale_white = (220, 223, 227)
hover_color = (255, 255, 255)
hover_color_exit = (255, 255, 255)

#Positions
positions = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

# Who Starts?
number = random.randint(1, 2)
dict = {1: "X", 2: "O"}
winner = None

# Screen
src_width = 600
src_height = 700
screen = pygame.display.set_mode((src_width, src_height))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BLACK)
title = pygame.font.Font('freesansbold.ttf', 90)
play = pygame.font.Font('freesansbold.ttf', 30)
end = 1.0
start = False
first = False

def ending (positions):
    if positions[0][0] == positions[0][1] == positions[0][2] and positions[0][0] != 0:
        win = positions[0][0]

    if positions[1][0] == positions[1][1] == positions[1][2] and positions[1][0] != 0:
        win = positions[1][0]

    if positions[2][0] == positions[2][1] == positions[2][2] and positions[2][0] != 0:
        win = positions[2][0]

    if positions[0][0] == positions[1][0] == positions[2][0] and positions[0][0] != 0:
        win = positions[0][0]

    if positions[0][1] == positions[1][1] == positions[2][1] and positions[0][1] != 0:
        win = positions[0][1]

    if positions[0][2] == positions[1][2] == positions[2][2] and positions[0][2] != 0:
        win = positions[0][2]

    if positions[0][0] == positions[1][1] == positions[2][2] and positions[0][0] != 0:
        win = positions[0][0]

    if positions[0][2] == positions[1][1] == positions[2][0] and positions[1][1] != 0:
        win = positions[0][2]

    return win



run = True
while run == True:

    caption = title.render('Tic Tac Toe', True, WHITE)
    captionRect = caption.get_rect()
    captionRect.center = (300, 200)
    title_bg = title.render('Tic Tac Toe', True, pale_white)
    titleRect = title_bg.get_rect()
    titleRect.center = (304, 204)

    text = play.render('Play', True, hover_color)
    textRect = text.get_rect()
    textRect.center = (300, 300)
    exit = play.render('Exit', True, hover_color_exit)
    exitRect = exit.get_rect()
    exitRect.center = (300, 350)
    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
    pos = pygame.mouse.get_pos()

    if not start:
        screen.blit(title_bg, titleRect)
        screen.blit(caption, captionRect)
        screen.blit(text, textRect)
        screen.blit(exit, exitRect)
        pygame.display.update()


        if 269 <= pos[0] <= 332 and 336 <= pos[1] <= 360:
            hover_color_exit = RED
            if pressed1 == 1:
                run = False

        if 331 < pos[0] or pos[0] < 268 or 361 < pos[1] or pos[1] < 335:
            hover_color_exit = WHITE

        if 269 <= pos[0] <= 332 and 284 <= pos[1] <= 306:
            hover_color = GREEN
            if pressed1 == 1:
                start = True
                end = 2.0
                hit = 0

        if 331 < pos[0] or pos[0] < 268 or 307 < pos[1] or pos[1] < 283:
            hover_color = WHITE

    if start == True:
        if first == False:
            screen.fill(BLACK)
            first = True

        pygame.display.update(pygame.draw.rect(screen, GREEN, (0, 0, 5, 600)))
        pygame.display.update(pygame.draw.rect(screen, GREEN, (200, 0, 5, 600)))
        pygame.display.update(pygame.draw.rect(screen, GREEN, (400, 0, 5, 600)))
        pygame.display.update(pygame.draw.rect(screen, GREEN, (595, 0, 5, 600)))
        pygame.display.update(pygame.draw.rect(screen, GREEN, (0, 0, 600, 5)))
        pygame.display.update(pygame.draw.rect(screen, GREEN, (0, 200, 600, 5)))
        pygame.display.update(pygame.draw.rect(screen, GREEN, (0, 400, 600, 5)))
        pygame.display.update(pygame.draw.rect(screen, GREEN, (0, 595, 600, 5)))
        pygame.display.update(pygame.draw.rect(screen, GREEN, (100, 600, 5, 700)))
        pygame.display.update(pygame.draw.rect(screen, GREEN, (500, 600, 5, 700)))
        pygame.display.update(pygame.draw.rect(screen, GREEN, (100, 695, 400, 5)))


        if dict[number] == "O":
            pygame.display.update(pygame.draw.rect(screen, BLACK, (150, 620, 300, 70)))
            pygame.display.update(pygame.draw.circle(screen, BLUE, (300, 650), 30, 3))

        if dict[number] == "X":
            pygame.display.update(pygame.draw.rect(screen, BLACK, (150, 620, 300, 70)))
            pygame.display.update(pygame.draw.line(screen, ORANGE, (280, 632), (320, 669), 3))
            pygame.display.update(pygame.draw.line(screen, ORANGE, (320, 632), (280, 669), 3))

        if pressed1 == True and end/4 == 0.75:
            if 0 < pos[0] < 200 and 0 < pos[1] < 200:

                if dict[number] == "X" and positions[0][0] == 0:
                    pygame.display.update(pygame.draw.line(screen, ORANGE, (0, 0), (200, 200), 3))
                    pygame.display.update(pygame.draw.line(screen, ORANGE, (200, 0), (0, 200), 3))
                    number += 1
                    positions[0][0] = 1

                if dict[number] == "O" and positions[0][0] == 0:
                    pygame.display.update(pygame.draw.circle(screen, BLUE, (100, 100), 70, 3))
                    number -= 1
                    positions[0][0] = 2

            if 200 < pos[0] < 400 and 0 < pos[1] < 200:

                if dict[number] == "X" and positions[0][1] == 0:
                    pygame.display.update(pygame.draw.line(screen, ORANGE, (200, 0), (400, 200), 3))
                    pygame.display.update(pygame.draw.line(screen, ORANGE, (400, 0), (200, 200), 3))
                    number += 1
                    positions[0][1] = 1

                if dict[number] == "O" and positions[0][1] == 0:
                    pygame.display.update(pygame.draw.circle(screen, BLUE, (300, 100), 70, 3))
                    number -= 1
                    positions[0][1] = 2

            if 400 < pos[0] < 600 and 0 < pos[1] < 200:
                if dict[number] == "X" and positions[0][2] == 0:
                    pygame.display.update(pygame.draw.line(screen, ORANGE, (400, 0), (600, 200), 3))
                    pygame.display.update(pygame.draw.line(screen, ORANGE, (600, 0), (400, 200), 3))
                    number += 1
                    positions[0][2] = 1

                if dict[number] == "O" and positions[0][2] == 0:
                    pygame.display.update(pygame.draw.circle(screen, BLUE, (500, 100), 70, 3))
                    number -= 1
                    positions[0][2] = 2

            if 0 < pos[0] < 200 and 200 < pos[1] < 400:

                if dict[number] == "X" and positions[1][0] == 0:
                    pygame.display.update(pygame.draw.line(screen, ORANGE, (0, 200), (200, 400), 3))
                    pygame.display.update(pygame.draw.line(screen, ORANGE, (200, 200), (0, 400), 3))
                    number += 1
                    positions[1][0] = 1

                if dict[number] == "O" and positions[1][0] == 0:
                    pygame.display.update(pygame.draw.circle(screen, BLUE, (100, 300), 70, 3))
                    number -= 1
                    positions[1][0] = 2

            if 200 < pos[0] < 400 and 200 < pos[1] < 400:

                if dict[number] == "X" and positions[1][1] == 0:
                    pygame.display.update(pygame.draw.line(screen, ORANGE, (200, 200), (400, 400), 3))
                    pygame.display.update(pygame.draw.line(screen, ORANGE, (400, 200), (200, 400), 3))
                    number += 1
                    positions[1][1] = 1

                if dict[number] == "O" and positions[1][1] == 0:
                    pygame.display.update(pygame.draw.circle(screen, BLUE, (300, 300), 70, 3))
                    number -= 1
                    positions[1][1] = 2

            if 400 < pos[0] < 600 and 200 < pos[1] < 400:
                if dict[number] == "X" and positions[1][2] == 0:
                    pygame.display.update(pygame.draw.line(screen, ORANGE, (400, 200), (600, 400), 3))
                    pygame.display.update(pygame.draw.line(screen, ORANGE, (600, 200), (400, 400), 3))
                    number += 1
                    positions[1][2] = 1

                if dict[number] == "O" and positions[1][2] == 0:
                    pygame.display.update(pygame.draw.circle(screen, BLUE, (500, 300), 70, 3))
                    number -= 1
                    positions[1][2] = 2

            if 0 < pos[0] < 200 and 400 < pos[1] < 600:

                if dict[number] == "X" and positions[2][0] == 0:
                    pygame.display.update(pygame.draw.line(screen, ORANGE, (0, 400), (200, 600), 3))
                    pygame.display.update(pygame.draw.line(screen, ORANGE, (200, 400), (0, 600), 3))
                    number += 1
                    positions[2][0] = 1

                if dict[number] == "O" and positions[2][0] == 0:
                    pygame.display.update(pygame.draw.circle(screen, BLUE, (100, 500), 70, 3))
                    number -= 1
                    positions[2][0] = 2

            if 200 < pos[0] < 400 and 400 < pos[1] < 600:

                if dict[number] == "X" and positions[2][1] == 0:
                    pygame.display.update(pygame.draw.line(screen, ORANGE, (200, 400), (400, 600), 3))
                    pygame.display.update(pygame.draw.line(screen, ORANGE, (400, 400), (200, 600), 3))
                    number += 1
                    positions[2][1] = 1

                if dict[number] == "O" and positions[2][1] == 0:
                    pygame.display.update(pygame.draw.circle(screen, BLUE, (300, 500), 70, 3))
                    number -= 1
                    positions[2][1] = 2

            if 400 < pos[0] < 600 and 400 < pos[1] < 600:
                if dict[number] == "X" and positions[2][2] == 0:
                    pygame.display.update(pygame.draw.line(screen, ORANGE, (400, 400), (600, 600), 3))
                    pygame.display.update(pygame.draw.line(screen, ORANGE, (400, 600), (600, 400), 3))
                    number += 1
                    positions[2][2] = 1

                if dict[number] == "O" and positions[2][2] == 0:
                    pygame.display.update(pygame.draw.circle(screen, BLUE, (500, 500), 70, 3))
                    number -= 1
                    positions[2][2] = 2

        if end != True:
            end = 3.0

        if positions[0][0] == positions[0][1] == positions[0][2] and positions[0][0] != 0:
            pygame.display.update(pygame.draw.line(screen, GREEN, (10, 100), (590, 100), 10))
            end = True


        if positions[1][0] == positions[1][1] == positions[1][2] and positions[1][0] != 0:
            pygame.display.update(pygame.draw.line(screen, GREEN, (10, 300), (590, 300), 10))
            end = True


        if positions[2][0] == positions[2][1] == positions[2][2] and positions[2][0] != 0:
            pygame.display.update(pygame.draw.line(screen, GREEN, (10, 500), (590, 500), 10))
            end = True


        if positions[0][0] == positions[1][0] == positions[2][0] and positions[0][0] != 0:
            pygame.display.update(pygame.draw.line(screen, GREEN, (100, 10), (100, 590), 10))
            end = True


        if positions[0][1] == positions[1][1] == positions[2][1] and positions[0][1] != 0:
            pygame.display.update(pygame.draw.line(screen, GREEN, (300, 10), (300, 590), 10))
            end = True


        if positions[0][2] == positions[1][2] == positions[2][2] and positions[0][2] != 0:
            pygame.display.update(pygame.draw.line(screen, GREEN, (500, 10), (500, 590), 10))
            end = True


        if positions[0][0] == positions[1][1] == positions[2][2] and positions[0][0] != 0:
            pygame.display.update(pygame.draw.line(screen, GREEN, (10, 10), (590, 590), 10))
            end = True


        if positions[0][2] == positions[1][1] == positions[2][0] and positions[1][1] != 0:
            pygame.display.update(pygame.draw.line(screen, GREEN, (590, 10), (10, 590), 10))
            end = True


        if end == True:
            winner = ending(positions)
            if dict[winner] == "O":
                title_bg = title.render(dict[winner] + " Wins", True, BLUE)
            else:
                title_bg = title.render(dict[winner] + " Wins", True, ORANGE)
            titleRect = title_bg.get_rect()
            titleRect.center = (300, 200)
            exit = play.render('Exit', True, hover_color_exit)
            exitRect = exit.get_rect()
            exitRect.center = (300, 350)

            if 269 <= pos[0] <= 332 and 336 <= pos[1] <= 360:
                hover_color_exit = RED
                if pressed1 == 1:
                    run = False

            else:
                hover_color_exit = WHITE

            screen.blit(title_bg, titleRect)
            screen.blit(exit, exitRect)
            pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
quit()