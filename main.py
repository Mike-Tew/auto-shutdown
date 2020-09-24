import os
import subprocess
from datetime import datetime, timedelta
from tkinter import Tk, LabelFrame, Label, Button, Entry

global shutdown_id
global wifi_id
shutdown_id = 1
wifi_id = 1


def shutdown():
    os.system("shutdown /s")


def disable_wifi():
    wifi = subprocess.check_output(
        "netsh interface show interface", stderr=subprocess.STDOUT, shell=True
    )
    lines = wifi.splitlines()
    for i in range(len(lines)):
        if b"Connected" in lines[i]:
            interface = lines[i].split(None, 3)
            interface = interface[3].decode("ASCII")
            subprocess.call(
                f'netsh interface set interface "{interface}" disable',
                stderr=subprocess.STDOUT,
                shell=True,
            )


def set_shutdown_time():
    """Take the user input and execute the shutdown script at the specified time"""

    global shutdown_id
    try:
        minutes = float(shutdown_entry.get())
        root.after_cancel(shutdown_id)

        # Calculating input time and displaying it in the GUI
        execution_time = datetime.now() + timedelta(minutes=minutes)
        display_string = (
            execution_time.strftime("%I:%M %p").lstrip("0").replace(" 0", " ")
        )
        shutdown_display_label.config(text=display_string)

        # Shutdown countdown timer
        shutdown_id = root.after(int(minutes * 60000), shutdown)
    except ValueError:
        pass


def set_internet_time():
    """Take the user input and execute the blocking script at the specified time"""

    global wifi_id
    try:
        minutes = float(internet_entry.get())
        root.after_cancel(wifi_id)

        # Calculating input time and displaying it in th GUI
        execution_time = datetime.now() + timedelta(minutes=minutes)
        display_string = (
            execution_time.strftime("%I:%M %p").lstrip("0").replace(" 0", " ")
        )
        internet_display_label.config(text=display_string)

        # Wifi countdown timer
        wifi_id = root.after(int(minutes * 60000), disable_wifi)
    except ValueError:
        pass


root = Tk()
root.title("Computer Shutdown")

title_label = Label(root, text="AUTO SHUTDOWN", font=("Helvetica 16 bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=[5, 0])

# Computer Timer Frame
shutdown_frame = LabelFrame(root, text="Computer Timer", padx=20, pady=10)
shutdown_frame.grid(row=1, column=0, padx=20)

shutdown_timer_label = Label(shutdown_frame, text="Shutdown in")
shutdown_timer_label.grid(row=0, column=0)

shutdown_entry = Entry(shutdown_frame, width=5)
shutdown_entry.grid(row=0, column=1)

shutdown_minutes_label = Label(shutdown_frame, text="minutes.")
shutdown_minutes_label.grid(row=0, column=2, sticky="w")

shutdown_set_button = Button(
    shutdown_frame, text="SET", padx=10, command=set_shutdown_time
)
shutdown_set_button.grid(row=0, column=3, padx=[10, 0])

shutdown_set_label = Label(shutdown_frame, text="Set for:", font=("Helvetica 12 bold"))
shutdown_set_label.grid(row=1, column=0, columnspan=2, pady=[10, 0])

shutdown_display_label = Label(shutdown_frame, width=7, font=("Helvetica 12"))
shutdown_display_label.grid(row=1, column=2, pady=[10, 0])

# Internet Timer Frame
internet_frame = LabelFrame(root, text="Network Connections Timer", padx=20, pady=10)
internet_frame.grid(row=1, column=1, padx=20)

internet_timer_label = Label(internet_frame, text="Turn off in")
internet_timer_label.grid(row=0, column=0)

internet_entry = Entry(internet_frame, width=5)
internet_entry.grid(row=0, column=1)

internet_minutes_label = Label(internet_frame, text="minutes.")
internet_minutes_label.grid(row=0, column=2, sticky="w")

internet_set_button = Button(
    internet_frame, text="SET", padx=10, command=set_internet_time
)
internet_set_button.grid(row=0, column=3, padx=[10, 0])

internet_set_label = Label(internet_frame, text="Set for:", font=("Helvetica 12 bold"))
internet_set_label.grid(row=1, column=0, columnspan=2, pady=[10, 0])

internet_display_label = Label(internet_frame, width=7, font=("Helvetica 12"))
internet_display_label.grid(row=1, column=2, pady=[10, 0])

# Create Exit Button
exit_button = Button(
    root, width=20, text="Exit", pady=5, font=("Helvetica 12 bold"), command=root.quit
)
exit_button.grid(row=3, column=0, columnspan=2, pady=20)

root.mainloop()
