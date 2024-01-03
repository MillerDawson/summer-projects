import tkinter as tk
import ttkbootstrap as ttk

# window
window = ttk.Window(themename="superhero")
window.title("Clock")
window.geometry("500x500")


# functions
def check_field_validity() -> bool:
    # check if both fields are valid
    try:
        # uses tracking variables for efficiency
        field_1 = int(clicksps_string_var.get())
        field_2 = int(total_string_var.get())

        print(field_1)
        print(field_2)
        return True
    except:
        return False

def start_clicker():
    # if valid then start
    if check_field_validity():
        print("Starting")
        start_button["state"] = "disabled"
        stop_button["state"] = "enabled"
    # make this button go disabled and stop enabled

def stop_clicker():
    # stop clicker
    print("Stopping")
    start_button["state"] = "enabled"
    stop_button["state"] = "disabled"

# ========== widgets ==========
title_label = ttk.Label(window, text="Millers Auto Clicker", font="arial 20 bold")
title_label.pack(pady=10)

# input frames
click_ps_frame = ttk.Frame(master=window)
click_amount_frame = ttk.Frame(master=window)
button_frame = ttk.Frame(master=window)

# tkinter variables
clicksps_string_var = ttk.StringVar(value=0)
total_string_var = ttk.StringVar(value=0)

# clicks per second
clicks_ps_label = ttk.Label(click_ps_frame, text="Num clicks per second",  font="arial 20")
clicks_ps_entry = ttk.Entry(click_ps_frame, textvariable=clicksps_string_var)
clicks_ps_label.pack(side="left", padx=5)
clicks_ps_entry.pack(side="left")
click_ps_frame.pack(pady=10)

# total amount of clicks
total_amount_label = ttk.Label(click_amount_frame, text="Total Clicks (0 = inf)", font="arial 20")
total_amount_entry = ttk.Entry(click_amount_frame, textvariable=total_string_var)
total_amount_label.pack(side="left", padx=5)
total_amount_entry.pack(side="left")
click_amount_frame.pack(pady=10)

# buttons
start_button = ttk.Button(button_frame, text="Start", command=start_clicker)
stop_button = ttk.Button(button_frame, text="Stop", command=stop_clicker, state="disabled")
start_button.pack(side="left", padx=20)
stop_button.pack(side="left")
button_frame.pack(pady=10)

# run
if __name__ == "__main__":
    window.mainloop()