from tkinter import *
import time

root = Tk()

c = Canvas(width=1000, height=500, bg='grey80')
c.pack()

kvadrat = c.create_rectangle([5, 200], [105, 300], fill="red")


def funkcia(event):
    y = 0
    while y != 895:
        c.move(kvadrat, 1, 0)
        time.sleep(0.005)
        root.update()
        y += 1


c.tag_bind(kvadrat, '<Button-1>', funkcia)
root.mainloop()
