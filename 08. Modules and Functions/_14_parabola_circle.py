import math
# with plotting
try:
    import tkinter
except ImportError: # in case we're dealing with python 2
    import Tkinter as tkinter


def parabola(page, size):
    for x in range(-size, size):
        y = x * x / size
        plot(page, x, y)


def circle(page, radious, v, h):
     for x in range(v, v + radious):
         y = h + (math.sqrt(radious ** 2 - ((x - v) ** 2)))
         plot(page, x, y)
         # to rotate and to plot the rest of the circle
         plot(page, x, 2 * h - y) 
         plot(page, 2 * v - x, y)
         plot(page, 2 * v - x, 2 * h - y)


def draw_axes(page):
    canvas.update()
    x_origin = canvas.winfo_width() / 2
    y_origin = canvas.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill='black')
    page.create_line(0, y_origin, 0 , -y_origin, fill='black')

def plot(page, x, y):
    page.create_line(x, -y, x + 1, -y + 1, fill='red')


mainWindow = tkinter.Tk()
mainWindow.title('Parabola')
mainWindow.geometry('640x480')

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

draw_axes(canvas)

parabola(canvas, 100)
parabola(canvas, 200)
parabola(canvas, 300)

circle(canvas, 100, 100, 100)
circle(canvas, 100, 100, -100)
circle(canvas, 100, -100, 100)
circle(canvas, 100, -100, -100)

circle(canvas, 50, 100, 100)
circle(canvas, 50, 100, -100)
circle(canvas, 50, -100, 100)
circle(canvas, 50, -100, -100)

mainWindow.mainloop()