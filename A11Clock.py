import pgzrun

def draw():
    screen.fill((200,200,200))
    screen.draw.text('Time 1 ; '+str(time1),(10,10),fontsize=40)
    screen.draw.text('Time 2 ; '+str(time2),topright=(630,10),fontsize=40)

def on_mouse_down(pos,button):
    clock.schedule(count_time_1,1.0)

def count_time_1():
    global time1
    time1+=1

def count_time_2():
    global time2
    time2+=1
    if time2==20:
        clock.unschedule(count_time_2)

WIDTH=640
HEIGHT=480
TITLE='Test Clock'
time1=time2=0
clock.schedule(count_time_1,1.0)
clock.schedule_interval(count_time_2,1.0)

pgzrun.go()
