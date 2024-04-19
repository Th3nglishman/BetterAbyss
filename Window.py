import sys
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import Loader
import Main

root = None
init_height = -1
init_width = -1
run_button = None
fetch_data_button = None

# TODO figure out how to trigger an event when the window size is changed

def set_up_root():
    global root, init_width, init_height

    root = Tk()
    root.title("BetterAbyss")

    sys.path.append('.')

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

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
    global root, init_width, init_height, run_button
    # text = Label(root, text="Nothing will work unless you do.")
    # text.pack()
    # text2 = Label(root, text="- Maya Angelou")
    # text2.pack()
    baby_image = Image.open("C:\\Users\\johnn\\PycharmProjects\\RiotInterface\\Josh_baby.gif")
    baby_image = baby_image.resize((init_width, init_height // 2))
    test = ImageTk.PhotoImage(baby_image)
    label1 = tkinter.Label(image=test)
    label1.image = test
    label1.place(x=0, y=90)
    Main.main()


def game_button_pressed():
    # TODO run code to check champs
    Main.call_api()
    print("Button Pressed")

def fetch_data():
    Loader.get_webpage_html()
    Loader.crawl()

def step_event():
    global root
    root.after(1, step_event)


def run():
    global root, fetch_data_button

    game_button = Button(master=root, background="pink", justify="center", command=game_button_pressed, text="Game")
    fetch_data_button = Button(master=root, background="white", justify="center", command=fetch_data, text="fetch wiki data")
    game_button.pack()
    fetch_data_button.pack()

    root.after(1, step_event)
    root.mainloop()

def main():
    set_up_root()
    set_up_window()
    run()

if __name__ == "__main__":
    main()