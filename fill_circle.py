import pgzrun

WIDTH=400
HEIGHT=300

def draw():
    screen.clear()
    for n in range(1,5):
        screen.draw.filled_circle((80*n,80),40,(255,255,0))
    Colors=('red','green','blue','white')
    for n in range(4):
        screen.draw.filled_circle((200,200),25*(4-n),Colors[n])

pgzrun.go()
