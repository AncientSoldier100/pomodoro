from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
reps = 0
# ---------------------------- TIMER RESET ------------------------------- #


def timer_reset():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_one.config(text="Timer", fg=GREEN)
    label_two.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start(repetitions=0):
    global reps
    reps += 1

    work_sec = int(WORK_MIN * 60)
    short_break_sec = int(SHORT_BREAK_MIN * 60)
    long_break_sec = int(LONG_BREAK_MIN * 60)

    if reps % 8 == 0:
        countdown(long_break_sec)
        label_one.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        label_one.config(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        label_one.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    global reps
    global timer
    count_min = count//60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start()
        marks = "✔️"*(reps//2)
        label_two.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

label_one = Label(text="Timer", font=(
    FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
label_one.grid(row=0, column=1)

label_two = Label(fg=GREEN, bg=YELLOW)
label_two.grid(row=3, column=1)

button_one = Button(text="Start", command=start)
button_one.grid(row=2, column=0)

button_two = Button(text="Reset", command=timer_reset)
button_two.grid(row=2, column=12)

window.mainloop()
