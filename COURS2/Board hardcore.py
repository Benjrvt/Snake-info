import pyxel
import numpy as np
import time



def update():
    global snake_geometry
    global snake_direction
    global new_snake_head
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    elif pyxel.btnp(pyxel.KEY_LEFT):
        print('←')
        snake_direction=[-1,0]
    elif pyxel.btnp(pyxel.KEY_UP):
        print('↑')
        snake_direction=[0,-1]
    elif pyxel.btnp(pyxel.KEY_RIGHT):
        print('→')
        snake_direction=[1,0]
    elif pyxel.btnp(pyxel.KEY_DOWN):
        print('↓')
        snake_direction=[0,1]



a,b=np.random.randint(0,30),np.random.randint(0,30)
snake_geometry = [[10, 15],[11, 15],[12, 15]]
snake_direction = [1,0]
new_snake_head=[13,15] 


def draw():
    global snake_geometry
    global snake_direction
    global a
    global b
    pyxel.cls(13)
    for i in range(30):
        for j in range(30):
            if (i+j) % 2 == 0:
                pyxel.pset(i, j, 7)
    
    pyxel.pset(a,b,8)
    if new_snake_head[0]>=30:
            pyxel.quit()
    elif new_snake_head[1]>=30:
            pyxel.quit()
    elif new_snake_head[1]<=-1:
            pyxel.quit()
    elif new_snake_head[0]<=-1:
            pyxel.quit()
    if new_snake_head in snake_geometry:
        snake_geometry.pop(0)
    snake_geometry.append(new_snake_head[:])
    if [a,b]==new_snake_head :
        a,b = np.random.randint(1,30),np.random.randint(1,30)
        for i in range(len(snake_geometry)):
            pyxel.pset(snake_geometry[i][0],snake_geometry[i][1],3)
        snake_head=snake_geometry[-1]
        pyxel.pset(snake_head[0],snake_head[1],11)
        new_snake_head[0]=snake_head[0]+snake_direction[0]
        new_snake_head[1]=snake_head[1]+snake_direction[1]
        snake_geometry=snake_geometry[:]
        
    else :
        for i in range(len(snake_geometry)):
            pyxel.pset(snake_geometry[i][0],snake_geometry[i][1],3)
        snake_head=snake_geometry[-1]
        pyxel.pset(snake_head[0],snake_head[1],11)
        new_snake_head[0]=snake_head[0]+snake_direction[0]
        new_snake_head[1]=snake_head[1]+snake_direction[1]
        snake_geometry=snake_geometry[1:]
        
    # if new_snake_head[0]==30:
    #         time.sleep(0.2)
    # elif new_snake_head[1]==30:
    #         time.sleep(0.2)
    # elif new_snake_head[1]==0:
    #         time.sleep(0.2)
    # elif new_snake_head[0]==0:
    #         time.sleep(0.2)
    
      


pyxel.init(30, 30, fps=10)
pyxel.run(update, draw)