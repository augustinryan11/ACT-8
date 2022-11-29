from pulsesensor import Pulsesensor
import random
from tkinter import *

WIDTH=1500
HEIGHT=800
COLORS = ["red4", "red3", "OrangeRed2", "OrangeRed4", "firebrick3"]
DELAY = 200  # In millisecs
NUMBALLS = 5

class Ball:
    def __init__(self, color, size):
        self.shape = canvas.create_oval(10, 10, size,  size, fill=color,
                                        outline=color, stipple="gray25")
        self.xspeed = random.randrange(-1, 5)
        self.yspeed = random.randrange(-1, 5)

    def move(self):
        canvas.move(self.shape, self.xspeed, self.yspeed)
        pos = canvas.coords(self.shape)
        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.yspeed = -self.yspeed
        if pos[2] >= WIDTH or pos[0] <= 0:
            self.xspeed = -self.xspeed

def poll(p):
    try:
#        bpm = p.BPM
        bpm = random.randint(0, 200)  # Random value for testing.
        if bpm < 1:
#            print("No Heartbeat found")
            pass
        else:
#            print("BPM: %d" % bpm)
            for ball in balls:
                ball.move()
    except Exception as exc:
        print('Exception raised: {}'.format(exc))
        p.stopAsyncBPM()
        root.quit()

    root.after(DELAY, poll, p)  # Call this function again after delay.

if __name__ == '__main__':
    root = Tk()
    root.title("Beating Heart")
    canvas = Canvas(root, bg="brown4", height=HEIGHT, width=WIDTH)
    canvas.pack()
    balls = [Ball(random.choice(COLORS), random.randrange(150, 200))
                for _ in range(NUMBALLS)]

    p = Pulsesensor()
    p.startAsyncBPM()
    poll(p)  # Start polling.
    root.mainloop()