from collections import defaultdict

import pygame, sys, random
from pygame.locals import *

pygame.init()

WINDOWWIDTH = 1000
WINDOWHEIGHT = 1000

FPS = 100  # число кадров в секунду
clock = pygame.time.Clock()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 150, 255)
NAVYBLUE = (0, 0, 200)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)

SPEED = 4
VILLAIN_SPEED = 2

PLAYER_TURN = True

center_blocks = []
for x in range(200, 800, 76):
    for y in range(200, 800, 76):
        block = {'rect': pygame.Rect(x, y, 68, 68), 'color': NAVYBLUE}
        center_blocks.append(block)


windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Моя первая игра')

pygame.mouse.set_visible(False)


def rocket_block(x, y, dir):
    return {'rect': pygame.Rect(x, y, 20, 20), 'color': BLACK, 'dir': dir}


stripes = []
for y in range(272, 800, 76):
    line = [[0, y], [WINDOWWIDTH, y]]
    stripes.append(line)
for x in range(272, 800, 76):
    line = [[x, 0], [x, WINDOWHEIGHT]]
    stripes.append(line)
for x in range(50, 200, 50):
    line = [[x, 200], [x, 800]]
    stripes.append(line)
for x in range(850, WINDOWHEIGHT, 50):
    line = [[x, 200], [x, 800]]
    stripes.append(line)
for y in range(50, 200, 50):
    line = [[200, y], [800, y]]
    stripes.append(line)
for y in range(850, WINDOWHEIGHT, 50):
    line = [[200, y], [800, y]]
    stripes.append(line)

villain_blocks = []

position_corner_blocks = [5, 805]
corner_blocks = []
for x in position_corner_blocks:
    for y in position_corner_blocks:
        corner_blocks.append({'rect': pygame.Rect(x, y, 190, 190), 'color': GREEN})

rockets = []

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if PLAYER_TURN:
                for item in center_blocks:
                    if item['rect'].collidepoint(event.pos):
                        item['color'] = BLUE
        if event.type == MOUSEMOTION:
            if PLAYER_TURN:
                for item in center_blocks:
                    if not item['rect'].collidepoint(event.pos):
                        item['color'] = NAVYBLUE
                    if item['rect'].collidepoint(event.pos):
                        item['color'] = BLUE
        if event.type == MOUSEBUTTONUP and event.button == 1:
            if PLAYER_TURN:
                for item in center_blocks:
                    if item['rect'].collidepoint(event.pos):
                        item['color'] = NAVYBLUE
                        rockets.append(rocket_block(item['rect'][0] + 24, item['rect'][1], 'up'))
                        rockets.append(rocket_block(item['rect'][0] + 48, item['rect'][1] + 24, 'right'))
                        rockets.append(rocket_block(item['rect'][0] + 24, item['rect'][1] + 48, 'down'))
                        rockets.append(rocket_block(item['rect'][0], item['rect'][1] + 24, 'left'))

    windowSurface.fill(WHITE)

    for block in center_blocks:
        pygame.draw.rect(windowSurface, block['color'], block['rect'])
    for rocket in rockets:
        pygame.draw.rect(windowSurface, rocket['color'], rocket['rect'])
        if rocket['dir'] == 'up':
            rocket['rect'].top -= SPEED
        if rocket['dir'] == 'right':
            rocket['rect'].left += SPEED
        if rocket['dir'] == 'down':
            rocket['rect'].top += SPEED
        if rocket['dir'] == 'left':
            rocket['rect'].left -= SPEED
        if rocket['rect'].top < 0 or \
                rocket['rect'].left > WINDOWWIDTH or \
                rocket['rect'].top > WINDOWHEIGHT or \
                rocket['rect'].left < 0:
            rockets.remove(rocket)
    for stripe in stripes:
        start, end = stripe
        pygame.draw.line(windowSurface, YELLOW, start, end, 3)
    for corner_block in corner_blocks:
        pygame.draw.rect(windowSurface, corner_block['color'], corner_block['rect'])
    pos = pygame.mouse.get_pos()
    mouse_block_rect = (pos[0] - 1, pos[1] - 1, 6, 6)
    mouse_block = {'rect': mouse_block_rect, 'color': BLACK}
    if pygame.mouse.get_focused():
        pygame.draw.rect(windowSurface, mouse_block['color'], mouse_block['rect'])

    pygame.display.update()
    clock.tick(FPS)

