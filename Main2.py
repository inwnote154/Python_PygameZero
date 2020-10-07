import pgzrun

def draw():
    screen.fill('white')
    screen.draw.text('Change Position and Display',topleft=(150,80),color='blue')
    logo.draw()
    apple.draw()
    apple2.draw()

def update():
    if(logo.x<WIDTH):
        logo.x+=1
    if(logo.y<HEIGHT):
        logo.y+=1

WIDTH=400
HEIGHT=300
logo=Actor('it_logo',(0,0))
apple=Actor('apple')
apple2=Actor('apple')
apple.pos=(WIDTH/2,HEIGHT/2)

pgzrun.go()
