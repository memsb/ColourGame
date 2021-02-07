import tkinter
import random

colours = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0
time_left = 30


def start_game(event):
    if time_left == 30:
        countdown()

    next_colour()


def next_colour():
    global score
    global time_left

    if time_left > 0:
        e.focus_set()

        if e.get().lower() == colours[1].lower():
            score += 1

        e.delete(0, tkinter.END)

        random.shuffle(colours)
        label.config(fg=str(colours[1]), text=str(colours[0]))
        scoreLabel.config(text="Score: " + str(score))


def countdown():
    global time_left

    if time_left > 0:
        time_left -= 1
        timeLabel.config(text="Time left: " + str(time_left))
        timeLabel.after(1000, countdown)


root = tkinter.Tk()
root.title("Colour Game")
root.geometry("375x200")

instructions = tkinter.Label(root, text="Type in the colour of the words, and not the word text!",
                             font=('Helvetica', 12))
instructions.pack()

scoreLabel = tkinter.Label(root, text="Press enter to start", font=('Helvetica', 12))
scoreLabel.pack()

timeLabel = tkinter.Label(root, text="Time left: " + str(time_left), font=('Helvetica', 12))
timeLabel.pack()

label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

e = tkinter.Entry(root)
root.bind('<Return>', start_game)
e.pack()
e.focus_set()

root.mainloop()
