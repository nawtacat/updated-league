import random
import math
import time
import pygame
import os
import sys

# initialize the pygame
pygame.init()
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# Create the screen
screen = pygame.display.set_mode((900, 500))
pygame.display.set_caption("Champions League")
icon = pygame.image.load(os.path.join('icon.png'))
pygame.display.set_icon(icon)
green = (0,255,0)
blue = (0,0,255)
font = pygame.font.Font('upheavtt.ttf', 32)
text = font.render('Money:', True, green, blue)
textRect = text.get_rect()

display_surface = pygame.display.set_mode((900, 500))
background = pygame.transform.scale(pygame.image.load(os.path.join('background_football.jpg')), (900, 500))

REAL = pygame.image.load(os.path.join('teams', 'real1.png'))
BARCELONA = pygame.image.load(os.path.join('teams', 'barca1.png'))
JUVENTUS = pygame.image.load(os.path.join('teams', 'juventus1.png'))
LIVERPOOL = pygame.image.load(os.path.join('teams', 'liverpool1.png'))
CHELSEA = pygame.image.load(os.path.join('teams', 'chelsea1.png'))
BAYERN = pygame.image.load(os.path.join('teams', 'bayern1.png'))
CITY = pygame.image.load(os.path.join('teams', 'mnc1.png'))
PSG = pygame.image.load(os.path.join('teams', 'psg1.png'))


def main():
    running = True

    while running:
        teams = ["PSG", "Barcelona", "Manchester City", "Bayern Munich", "Real Mardid", "Chelsea", "Liverpool", "Juventus"]
        nomore = teams
        group = []
        x1 = random.randint(0, 7)
        group.append(nomore[x1])
        del nomore[x1]
        x2 = random.randint(0, 6)
        group.append(nomore[x2])
        del nomore[x2]
        x3 = random.randint(0, 5)
        group.append(nomore[x3])
        del nomore[x3]
        x4 = random.randint(0, 4)
        group.append(nomore[x4])
        del nomore[x4]

        # We Just Divided "NUMBERS" Into two Random Groups

        nomore1 = nomore
        group1 = group
        some1 = []
        some2 = []

        x5 = random.randint(0, 3)
        some1.append(nomore1[x5])
        del nomore1[x5]
        x6 = random.randint(0, 2)
        some1.append(nomore1[x6])
        del nomore1[x6]

        x7 = random.randint(0, 3)
        some2.append(group1[x7])
        del group1[x7]
        x8 = random.randint(0, 2)
        some2.append(group1[x8])
        del group1[x8]

        pair1 = group1
        pair2 = nomore1
        pair3 = some1
        pair4 = some2


        # teams[0] = pygame.image.load(os.path.join('psg1.png'))

        logos = {
            teams[0]: PSG,
            teams[1]: BARCELONA
        }
        money = 100000
        main_font = pygame.font.SysFont("upheavtt.ttf", 50)
        WIN.blit(background, (0, 0))
        WIN.blit(PSG, (10, 10))
        WIN.blit(BAYERN, (120, 10))
        WIN.blit(CITY, (230, 10))
        WIN.blit(BARCELONA, (340, 10))
        WIN.blit(REAL, (450, 10))
        WIN.blit(CHELSEA, (560, 10))
        WIN.blit(LIVERPOOL, (670, 10))
        WIN.blit(JUVENTUS, (780, 10))
        money_label = main_font.render(f"MONEY: {money}", 1, (255,255,255))
        WIN.blit(money_label, (10, 440))
        for event in pygame.event.get():
            # if event object type is QUIT
            # then quitting the pygame
            # and program both.
            if event.type == pygame.QUIT:
                # deactivates the pygame library
                pygame.quit()

                # quit the program.
                quit()
            pygame.display.update()


if __name__ == "__main__":
    main()
