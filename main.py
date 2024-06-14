from tkinter import *
import math
import os
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
CHECKMARK = '✓'
timer = None  # WE CREATED THIS TIMER VARIABLE WITH NONE, then stored the window.after() method in this
            # This is becz window.after_cancel() use krne k liye hmko window.after() ko name wise daalna tha

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)  # READ LINE 14 COMMENTS

    # RESET THE HEADER TO "Timer"
    header.config(text="Timer",fg=GREEN)

    # reset the TIMER_TEXT to 00:00
    canvas.itemconfig(timer_text,text="00:00")

    # Reset CHECKMARKS to 0
    task_completion.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global REPS
    REPS += 1

    if REPS % 8 == 0:
        COUNT_TIME = LONG_BREAK_MIN
        header.config(text="Break", fg=RED)
    elif REPS % 2 == 0:
        COUNT_TIME = SHORT_BREAK_MIN
        header.config(text="Break", fg=PINK)
    else:
        COUNT_TIME = WORK_MIN
        header.config(text="Work", fg=GREEN)

    count_down(COUNT_TIME * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):

    count_minutes = math.floor(count/60)
    count_sec = count%60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_minutes}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000,count_down,count-1)  # This is inbuilt function of tkinter which makes it work after every 1000ms
                                             # we used this in place of while loop because there is already one while loop runninge ( window.mainloop() )
    else:
        start_timer()
        num_checkmarks = int((REPS/2) % 4)
        if  num_checkmarks == 0:
            task_completion.config(text=CHECKMARK*4)
        else:
            task_completion.config(text=CHECKMARK*num_checkmarks)


# ---------------------------- UI SETUP ------------------------------- #


                    # ------ WINDOW ----- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

                    # ------ CANVAS ------- #

# INORDER TO PUT A TOMato image AND PUT THE TIMER OVER IT, WE will use CANVAS

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0) # SPECIFY HEIGHT AND WIDTH OF CANVAS (HERE, BASED ON THE IMG DIMENSION)

script_dir = os.path.dirname(os.path.abspath(__file__)) # DON'T MIND WROTE THIS LINE USING CHAT GPT BECAUSE WANTED TO CONVERT IT IN AN APP
img_path = os.path.join(script_dir, 'Tomato.png')
tomato_img = PhotoImage(file=img_path) # This [ PhotoImage ] reads through a file and stores the image

canvas.create_image(100,112,image=tomato_img) # WE CAN ADD A BUNCH OF THINGS IN THE CANVAS, WITH EVERYTHING ALIGNED ONE OVER THE OTHER
                                        # note == > THE IMAGE HERE SHOULDN'T BE INFORM OF LOCATION,
                                        # iT IS EXPECTING A [ PhotoImage() ] data

#  ISS CANVAS.CREATE+_TEXT KO ek variable me store kiye so that baad me jab edit krna hoto iska use krske
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


                    # -------OTHER WIDGETS ------ #

header = Label(text="Timer",font=(FONT_NAME,50,"bold"),fg=GREEN,bg=YELLOW)
header.grid(column=1,row=0)

start_button = Button(text="Start",font=(FONT_NAME,10,"bold"),command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset",font=(FONT_NAME,10,"bold"),command=reset_timer)
reset_button.grid(column=2,row=2)

task_completion = Label(text="",font=("bold",18),fg=GREEN,bg=YELLOW)
task_completion.grid(row=3,column=1)


window.mainloop()