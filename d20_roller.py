import sys
import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage
import random

root = tk.Tk()
root.title('D20 roller')
root.geometry('800x600')

def calculate():
    sides=num_entry_sides.get()
    num=num_entry.get()
    try:
        sides = int(sides)
        num = int(num)
        for i in range(num):
            list_box.insert(tk.END, random.randint(1, sides))
    except:
        my_label['text']="Please only enter numbers"

list_box = tk.Listbox()
list_box.place(relx=0.6, rely=0.5, anchor='center', height=300)
list_box.configure(background='skyblue4', foreground='white', font=('Arial', 15))


image = PhotoImage(file='graphics/Dice/dice.png')
image_label = tk.Button(root, image=image, command=calculate)
image_label.place(relx=0.3, rely=0.2, anchor='center')

my_label = tk.Label(text = 'Press icon to roll \n or "Tab" to quit \n', font=('Arial', 10))
my_label.place(relx=0.3, rely=0.35, anchor='center')    
    
def save_to_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'w') as file:
                list_box_str = str(list_box.get(0, "end"))
                file.write(list_box_str)
            status_label.config(text=f"File saved: {file_path}")
        except Exception as e:
            status_label.config(text=f"Error saving file: {str(e)}")
            
def clear_list_box():
   list_box.delete(0,"end")


image = PhotoImage(file='graphics/Dice/dice.png')
image_label = tk.Button(root, image=image, command=calculate)
image_label.place(relx=0.3, rely=0.2, anchor='center')

save_button = tk.Button(root, text="Save output to file", command = save_to_file)
save_button.place(relx=0.3, rely=0.8, anchor='center')

status_label = tk.Label(root, text="", padx=20, pady=10)
status_label.pack()

Num_label=tk.Label(root, text='Enter how many dice', font = ('Arial',10,'normal'))
Num_label.place(relx=0.3, rely=0.45, anchor='center')

num_entry=tk.Entry(root, font = ('Arial',10,'normal'))
num_entry.place(relx=0.3, rely=0.5, anchor='center')

sides_label=tk.Label(root, text='Enter No. Sides', font = ('Arial',10,'normal'))
sides_label.place(relx=0.3, rely=0.6, anchor='center')

num_entry_sides=tk.Entry(root, font = ('Arial',10,'normal'))
num_entry_sides.place(relx=0.3, rely=0.65, anchor='center')

list_clear=tk.Button(root, text = 'Clear all numbers', command=clear_list_box)
list_clear.place(relx=0.6, rely=0.8, anchor='center')

root.bind("<Tab>", exit)
root.mainloop()
