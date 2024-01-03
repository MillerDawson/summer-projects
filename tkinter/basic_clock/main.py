import tkinter as tk
import ttkbootstrap as ttk
from datetime import datetime

# method for clock to update every second
def set_time():
    DELAY = 1000 # local constant
    date =  datetime.now()

    date_label["text"] = date.strftime("%D")
    time_label["text"] = date.strftime("%X")

    date_label.after(DELAY, set_time)
    time_label.after(DELAY, set_time)

# window
window = ttk.Window(themename="darkly")
window.title("Clock")
window.geometry("200x100")

# widgets
date_label = ttk.Label(window,text="day", font="arial 30")
date_label.pack(pady=5, padx=5)

time_label = ttk.Label(window, text="time", font="arial 30")
time_label.pack(pady=5, padx=5)

# calls set_time function
set_time()

# run
if __name__ == "__main__":
    window.mainloop()