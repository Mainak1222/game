import pgzrun
from random import randint
WIDTH = 500
HEIGHT = 500
TITLE = 'game'
r= 255
g =255
b =0
color = (r,g,b)
def draw():
    box= Rect((200,200),(100,100))
    box1= Rect((0,300),(100,100))
    screen.fill((color))
    screen.draw.rect(box,"red")
    screen.draw.filled_rect(box1,"green")
    screen.draw.circle((100,100),50,"cyan")
    screen.draw.filled_circle((300,300),50,"cyan")
