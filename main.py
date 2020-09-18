# Shutdown command
# os.system("shutdown /s /t 1")
from tkinter import Tk, LabelFrame, Label, Button, Entry
from threading import Thread
import os
import sys

print(sys.platform)



root = Tk()
root.title("Computer Shutdown")
# root.geometry("500x300+200+200")

title_label = Label(root, text="AUTO SHUTDOWN", font=("Helvetica 16 bold"))
title_label.grid(row=0, column=0, columnspan=2)

# Computer Frame
shutdown_frame = LabelFrame(root, text="Computer Timer", padx=20, pady=10)
shutdown_frame.grid(row=1, column=0, padx=20)

shutdown_timer_label = Label(shutdown_frame, text="Shutdown in")
shutdown_timer_label.grid(row=0, column=0)

shutdown_entry = Entry(shutdown_frame, width=5)
shutdown_entry.grid(row=0, column=1)

shutdown_minutes_label = Label(shutdown_frame, text="minutes.")
shutdown_minutes_label.grid(row=0, column=2)

shutdown_set_button = Button(shutdown_frame, text="SET", padx=10)
shutdown_set_button.grid(row=0, column=3, padx=[10, 0])

shutdown_set_label = Label(shutdown_frame, text="Set for:", font=("Helvetica 12 bold"))
shutdown_set_label.grid(row=1, column=0, columnspan=2, pady=[10, 0])

# Internet Frame
internet_frame = LabelFrame(root, text="Internet Timer", padx=20, pady=10)
internet_frame.grid(row=1, column=1, padx=20)

internet_timer_label = Label(internet_frame, text="Turn off in")
internet_timer_label.grid(row=0, column=0)

internet_entry = Entry(internet_frame, width=5)
internet_entry.grid(row=0, column=1)

internet_minutes_label = Label(internet_frame, text="minutes.")
internet_minutes_label.grid(row=0, column=2)

internet_set_button = Button(internet_frame, text="SET", padx=10)
internet_set_button.grid(row=0, column=3, padx=[10, 0])

internet_set_label = Label(internet_frame, text="Set for:", font=("Helvetica 12 bold"))
internet_set_label.grid(row=1, column=0, columnspan=2, pady=[10, 0])

# Create exit button
exit_button = Button(root, width=20, text="Exit", pady=10, command=root.quit)
exit_button.grid(row=3, column=0, columnspan=2, pady=20)

root.mainloop()