import pygame as pg
import os, sys

pg.init()
pg.mixer.init()

WIDTH = 500
HEIGHT = 500
FPS = 30


screen = pg.display.set_mode(size=(WIDTH, HEIGHT))
pg.display.set_caption('Strategy')

clock = pg.time.Clock()


# RGB-colors for game.
INDI_RED = (205, 92, 92)
NAWAHOO_WHITE = (255, 222, 173)


running_game = True

while running_game:

    screen.fill(NAWAHOO_WHITE)
    pg.display.flip()

    clock.tick(FPS)
    kkk = pg.Rect(0, 0, 50, 50)
    pg.draw.rect(screen, INDI_RED, kkk)


    for event in pg.event.get():

        if event.type == pg.QUIT:
            sys.exit()

        if event.type == pg.KEYDOWN:
            if pg.key.get_pressed == K_z:
                kkk.move(5, 5)