import tkinter as tk
import sys

root = tk.Tk()
root.title('Picker')

pick_label = tk.Label(root, text='Nothing picked.')
pick_label.pack()

blue_button = tk.Button(root, text='Blue', command=lambda: blue())
blue_button.pack()

red_button = tk.Button(root, text='Red', command=lambda: red())
red_button.pack()

green_button = tk.Button(root, text='Green', command=lambda: green())
green_button.pack()

exit_button = tk.Button(root, text='Exit', command=lambda: exit())
exit_button.pack()

def blue():
    pick_label.config(text='Blue was picked!', bg='blue', font=('TkIconFont', 12))
def red():
    pick_label.config(text='Red was picked!', bg='red', font=('TkIconFont', 8))
def green():
    pick_label.config(text='Green was picked!', bg ='green', font=('TkIconFont', 16))
def exit():
    sys.exit()

root.mainloop()