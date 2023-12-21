# Source: https://github.com/Benjrvt/Snake-info

import pyxel
import numpy as np
import time

UP = [0, -1]
LEFT = [-1, 0]
DOWN = [0, 1]
RIGHT = [1, 0]

LIGHT_GREEN = 11
DARK_GREEN = 3
WHITE = 13

WIDTH = HEIGHT = 30

def update():
    global snake_direction

    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    elif pyxel.btnp(pyxel.KEY_LEFT):
        print("←")
        snake_direction = LEFT
    elif pyxel.btnp(pyxel.KEY_UP):
        print("↑")
        snake_direction = UP
    elif pyxel.btnp(pyxel.KEY_RIGHT):
        print("→")
        snake_direction = RIGHT
    elif pyxel.btnp(pyxel.KEY_DOWN):
        print("↓")
        snake_direction = DOWN

def spawn_fruit():
    global fruit_x, fruit_y
    fruit_x, fruit_y = [np.random.randint(0, WIDTH), np.random.randint(0, HEIGHT)]

spawn_fruit()

snake_geometry = [[10, 15], [11, 15], [12, 15]]
snake_direction = [1, 0]
new_snake_head = [13, 15]

def move_and_draw(snake_geometry):         
    for (x, y) in snake_geometry:
            pyxel.pset(x, y, DARK_GREEN)
    snake_head = snake_geometry[-1]
    pyxel.pset(snake_head[0], snake_head[1], LIGHT_GREEN)
    new_snake_head[0] = snake_head[0] + snake_direction[0]
    new_snake_head[1] = snake_head[1] + snake_direction[1]
    return snake_geometry[:]

def draw():
    global snake_geometry
    global snake_direction
    global fruit_x
    global fruit_y
    pyxel.cls(WHITE)
    for i in range(WIDTH):
        for j in range(HEIGHT):
            if (i + j) % 2 == 0:
                pyxel.pset(i, j, 7)

    pyxel.pset(fruit_x, fruit_y, 8)
    if new_snake_head[0] >= WIDTH:
        pyxel.quit()
    elif new_snake_head[1] >= HEIGHT:
        pyxel.quit()
    elif new_snake_head[1] <= -1:
        pyxel.quit()
    elif new_snake_head[0] <= -1:
        pyxel.quit()
    if new_snake_head in snake_geometry:
        snake_geometry.pop(0)
    snake_geometry.append(new_snake_head[:])

    if [fruit_x, fruit_y] == new_snake_head: # eat fruit
        spawn_fruit()
        snake_geometry = move_and_draw(snake_geometry)
    else:
        snake_geometry = snake_geometry[1:] # shrink snake
        snake_geometry = move_and_draw(snake_geometry)

pyxel.init(WIDTH, HEIGHT, fps=10)
pyxel.run(update, draw)
