import pgzrun
import random

def draw():
    #screen.fill('white')
    #bg.draw()
    screen.blit('DDDD',(0,0))
    screen.draw.text('Rotation Image',(200,20),color='blue')
    screen.draw.text('Rotation Angle : '+str(apple.angle),(50,400),color='blue')
    apple.draw()
    apple1.pos=(50,50)
    apple1.draw()
    apple1.pos=(350,50)
    apple1.draw()

def update():
    apple.angle+=1
    #if(apple.angle==360):
    #    apple.angle=0
        
WIDTH=640
HEIGHT=480
apple=Actor('apple')
apple1=Actor('apple')
bg=Actor('DDDD')
apple.pos=(WIDTH/2,HEIGHT/2)
apple.anchor=(apple.width,apple.height)

pgzrun.go()
