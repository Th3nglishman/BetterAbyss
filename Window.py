import sys
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import Loader
import Control

root = None
init_height = -1
init_width = -1
game_button = None
fetch_button = None
text_field = None
image_field = None

# TODO figure out how to trigger an event when the window size is changed

def set_up_root():
    global root, init_width, init_height

    root = Tk()
    root.title("BetterBridge")

    sys.path.append('.')

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    if Control.TEST:
        print(screen_width)
        print(screen_height)

    root.configure(background="white")

    root.minsize(screen_width // 6, screen_height // 2)
    root.maxsize(screen_width // 3, screen_height // 2)

    init_width = screen_width // 6
    init_height = screen_height // 2
    root.geometry("{}x{}+{}+{}".format(init_width, init_height,
                                       screen_width - (screen_width // 5), screen_height // 10))

def set_up_window():
    global root, init_width, init_height, game_button, fetch_button, image_field, text_field
    baby_image = Image.open("C:\\Users\\johnn\\PycharmProjects\\RiotInterface\\Josh_baby.gif")
    baby_image = baby_image.resize((init_width, init_height // 2))
    test = ImageTk.PhotoImage(baby_image)
    image_field = tkinter.Label(image=test)
    image_field.image = test
    image_field.place(x=0, y=90)

    Control.setup_api()
    a = Loader.crawl()

    game_button = Button(master=root, background="pink", justify="center", command=game_button_pressed, text="Game")
    fetch_data_button = Button(master=root, background="white", justify="center", command=fetch_data, text="fetch wiki data")
    game_button.pack()
    fetch_data_button.pack()

    text_field = Label(root, text="Nothing will work unless you do.", justify=CENTER, width=init_width // 7, wraplength=(init_width * 2) // 3)
    text_field.place(x=0, y=init_height * 5 // 6)






def game_button_pressed():
    global text_field
    result = Control.call_api()
    text_field.configure(text=result)
    if Control.TEST:
        print("Button Pressed")

def fetch_data():
    b = Control.TEST
    Control.TEST = True
    Loader.get_webpage_html()
    Loader.crawl()
    Control.TEST = b

def step_event():
    global root, game_button, fetch_button, image_field, text_field



    root.after(1, step_event)


def run():
    global root
    root.after(1, step_event)
    root.mainloop()

def main():
    Loader.crawl()
    set_up_root()
    set_up_window()
    run()

if __name__ == "__main__":
    main()