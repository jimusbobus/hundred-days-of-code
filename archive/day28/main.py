# from tkinter import *
# import math
#
# # ---------------------------- CONSTANTS ------------------------------- #
# PINK = "#e2979c"
# RED = "#e7305b"
# GREEN = "#9bdeac"
# YELLOW = "#f7f5dd"
# FONT_NAME = "Courier"
# TICK = "✔"
# # WORK_MIN = 25
# # SHORT_BREAK_MIN = 5
# # LONG_BREAK_MIN = 20
# WORK_MIN = 0.25
# SHORT_BREAK_MIN = 0.1
# LONG_BREAK_MIN = 0.2
#
# tick_array = []
# reps = 0
# timer = None
#
#
# # ---------------------------- TIMER RESET ------------------------------- #
# def reset():
#     global reps, timer
#     reps = 0
#     tick_array.clear()
#     timer_label.config(text="Timer", fg=GREEN)
#     win.after_cancel(timer)
#     canvas.itemconfig(timer_text, text="00:00")
#
#
# # ---------------------------- TIMER MECHANISM ------------------------------- #
#
# def start():
#     global reps
#     reps += 1
#     work_sec = math.floor(WORK_MIN * 60)
#     short_rest_sec = math.floor(SHORT_BREAK_MIN * 60)
#     long_rest_sec = math.floor(LONG_BREAK_MIN * 60)
#     if reps % 8 == 0:
#         timer_label.config(text="Break", fg=RED)
#         countdown(long_rest_sec)
#     elif reps % 2 == 0:
#         timer_label.config(text="Break", fg=PINK)
#         countdown(short_rest_sec)
#     else:
#         timer_label.config(text="Work", fg=GREEN)
#         countdown(work_sec)
#
#
# # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# def countdown(count):
#     global timer
#     canvas.itemconfig(timer_text, text=int_to_timer_string(count))
#     if count > 0:
#         timer = win.after(1000, countdown, count - 1)
#     else:
#         start()
#         if reps % 2 == 0:
#             update_ticks()
#
#
# # ---------------------------- UI SETUP ------------------------------- #
#
#
# def update_ticks():
#     tick_array.append(TICK)
#     ticks_label.config(text=f"{''.join(tick_array)}", bg=YELLOW, fg=GREEN)
#
#
# def int_to_timer_string(total_seconds):
#     # Get hours, minutes, and seconds
#     if total_seconds < 60:
#         minutes = 0
#         seconds = total_seconds
#     else:
#         minutes, seconds = divmod(total_seconds, 60)
#     # hours, minutes = divmod(minutes, 60)
#
#     # Format the string as HH:MM:SS, padding with zeros if necessary
#     # timer_string = f"{hours:02}:{minutes:02}:{seconds:02}"
#     print(f"DEBUG: {minutes}:{seconds}")
#     timer_string = f"{minutes}:{seconds:02}"
#
#     return timer_string
#
#
# win = Tk()
# win.title("Pomodoro")
# # win.minsize(width=250, height=250)
# win.config(padx=100, pady=50, bg=YELLOW)
#
# canvas = Canvas(width=220, height=224, bg=YELLOW, highlightthickness=0)
# image = PhotoImage(file="./tomato.png")
# canvas.create_image(110, 112, image=image)
# canvas.grid(column=1, row=1)
# timer_text = canvas.create_text(110, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
#
# timer_label = Label(text="Timer", font=(FONT_NAME, 48, "bold"), fg=GREEN, bg=YELLOW)
# timer_label.grid(column=1, row=0)
#
# start_button = Button(text="Start", font=(FONT_NAME, 16, "italic"), command=start, bg=YELLOW, highlightthickness=0,
#                       borderwidth=0)
# start_button.grid(column=0, row=3)
#
# reset_button = Button(text="Reset", font=(FONT_NAME, 16, "italic"), command=reset, bg=YELLOW, highlightthickness=0,
#                       borderwidth=0)
# reset_button.grid(column=3, row=3)
#
# ticks_label = Label(text=f"{''.join(tick_array)}", bg=YELLOW, fg=GREEN)
# ticks_label.grid(column=1, row=4)
#
# win.mainloop()
