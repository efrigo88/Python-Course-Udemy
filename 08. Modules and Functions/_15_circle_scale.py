import math
# with plotting
try:
    import tkinter
except ImportError: # in case we're dealing with python 2
    import Tkinter as tkinter


# def circle(page, radious, v, h):
#      # changed the scale by multiplying and dividing the functions' parameters
#      scaling = 100
#      for_from = v * scaling
#      for_to = (v + radious) * scaling

#      for x in range(for_from, for_to):
#          x /= scaling  # it's the same as x divided by 100 and re-assigned
#          y = h + (math.sqrt(radious ** 2 - ((x - v) ** 2)))
#          plot(page, x, y)
#          # to rotate and to plot the rest of the circle
#          plot(page, x, 2 * h - y) 
#          plot(page, 2 * v - x, y)
#          plot(page, 2 * v - x, 2 * h - y)


## MINI - CHALLENGE ##
# Modify the circe function so that it allows the colour of the circle to be specified and default to red if a colour is not given.
#  
# a simpler method for drawing circles
def circle(page, radious, v, h, colour='red'):
    page.create_oval(v + radious, h + radious, v - radious, h - radious, outline=colour, width=3)


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

circle(canvas, 100, 100, 100)
circle(canvas, 100, 100, -100)
circle(canvas, 100, -100, 100)
circle(canvas, 100, -100, -100)
circle(canvas, 50, 100, 100, 'yellow')
circle(canvas, 50, 100, -100, 'yellow')
circle(canvas, 50, -100, 100, 'yellow')
circle(canvas, 50, -100, -100, 'yellow')
circle(canvas, 40, 0, 0, 'blue')

mainWindow.mainloop()