import pyxel
import time

t=time.time()

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw():
    global t
    t_new = time.time()
    dt = t_new - t
    t = t_new
    fps = 1.0 / dt
    fps = int(round(fps))
    pyxel.cls(0)
    color = pyxel.frame_count % 16
    pyxel.text(56, 54, "Hello, Snake!", color)
    pyxel.text(0, 0, f"fps: {fps}", 7)


pyxel.init(160, 120)
pyxel.run(update, draw)

