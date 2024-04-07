# graphics.py

from graphics import *

class Window:
    global window_width
    global window_height
    def __init__(self):
        self.make_window()

    def make_window(self):
        win = GraphWin("Main Frame", 500, 500)
        win.setBackground('black')
        click = win.getMouse()
        win.plot(click.getX(), click.getY(), 'white')
        click = win.getMouse()
        win.plot(click.getX(), click.getY(), 'white')
        click = win.getMouse()
        win.plot(click.getX(), click.getY(), 'white')
        click = win.getMouse()
        win.plot(click.getX(), click.getY(), 'white')
        click = win.getMouse()
        win.plot(click.getX(), click.getY(), 'white')
        click = win.getMouse()
        win.plot(click.getX(), click.getY(), 'white')



    def draw(self):
        win.setWidth()
