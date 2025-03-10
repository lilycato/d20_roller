import sys
import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage
from tkinter import messagebox
import random
import json

root = tk.Tk()
root.title('D20 roller')
root.geometry('800x600')

def calculate():
    sides=num_entry_sides.get()
    num=num_entry.get()
    total = 0
    try:
        sides = int(sides)
        num = int(num)
        for i in range(num):
            generated = random.randint(1, sides)
            list_box.insert(tk.END, generated)
            total += generated
        my_label['text']="Result:" + " " + str(total)
    except:
        messagebox.showerror('Invalid Input', 'Please enter numbers only')

list_box = tk.Listbox()
list_box.place(relx=0.6, rely=0.5, anchor='center', height=300)
list_box.configure(background='skyblue4', foreground='white', font=('Arial', 15))


image = PhotoImage(file='graphics/Dice/dice.png')
image_label = tk.Button(root, image=image, command=calculate)
image_label.place(relx=0.3, rely=0.2, anchor='center')
root.iconphoto(True, image)

my_label = tk.Label(text = 'Press icon to roll \n or "Tab" to quit \n', font=('Arial', 10))
my_label.place(relx=0.3, rely=0.35, anchor='center')    
    
def save_to_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'w') as file:
                list_box_str = str(list_box.get(0, "end"))
                file.write(list_box_str)
            messagebox.showinfo('File Saved to:', file_path)
        except Exception as e:
            messagebox.showerror('Error', 'An error has occured while saving.')
            
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

def init_tracker_window():
    init_w = tk.Tk()
    init_w.title('Initiative Tracker')
    init_w.geometry('500x500')
    tracker_dict = {}

    monster_name=tk.Label(init_w, text='Enter name', font = ('Arial',10,'normal'))
    monster_name.place(relx=0.2, rely=0.1, anchor='center')

    name_entry=tk.Entry(init_w, font = ('Arial',10,'normal'))
    name_entry.place(relx=0.2, rely=0.15, anchor='center')
    
    initiative_label=tk.Label(init_w, text='Enter Initiative', font = ('Arial',10,'normal'))
    initiative_label.place(relx=0.2, rely=0.2, anchor='center')

    init_entry=tk.Entry(init_w, font = ('Arial',10,'normal'))
    init_entry.place(relx=0.2, rely=0.25, anchor='center')
  
    name = tk.Listbox(init_w)
    name.place(relx=0.55, rely=0.4, anchor='center', height=300, width=100)
    name.configure(background='skyblue4', foreground='white', font=('Arial', 10))
    name_label=tk.Label(init_w, text='Name:', font = ('Arial',10,'normal'))
    name_label.place(relx=0.55, rely=0.065, anchor='center')
    
    initiative = tk.Listbox(init_w)
    initiative.place(relx=0.8, rely=0.4, anchor='center', height=300, width=100)
    initiative.configure(background='skyblue4', foreground='white', font=('Arial', 10))
    init_entry_label=tk.Label(init_w, text='Initiative:', font = ('Arial',10,'normal'))
    init_entry_label.place(relx=0.8, rely=0.065, anchor='center')
    
    current_status=tk.Label(init_w, text='', fg='red', font = ('Arial',10,'normal'))
    current_status.place(relx=0.5, rely=0.85, anchor='center')
    
 
    def add_to_tracker():
        current_status['text']="Adding monsters.."
        initiative.delete(0,"end")
        name.delete(0,"end")
        name_entered = name_entry.get()
        
        try:
            initiative_count = int(init_entry.get())
        except:
            messagebox.showerror('Invalid Input', 'Please enter numbers only')
            
        tracker_dict[name_entered] = initiative_count
        sorted_tracker_dict=dict(sorted(tracker_dict.items(), key=lambda item: item[1]))
        
        name_keys = list(sorted_tracker_dict.keys())
        init_values = list(sorted_tracker_dict.values())
        
        for keys in reversed(name_keys):    
            name.insert(tk.END, keys)
            
        for values in reversed(init_values):    
            initiative.insert(tk.END, values)
    
    def clear_tracker():
        initiative.delete(0,"end")
        name.delete(0,"end")
        name_entry.delete(0,"end")
        init_entry.delete(0,"end")
        tracker_dict.clear()
        
    def del_selection():
        for selected in name.curselection():
            name.delete(selected)
            initiative.delete(selected)
                             
    button_add2tracker = tk.Button(init_w, text='Add to tracker', command=add_to_tracker)
    button_add2tracker.place(relx=0.2, rely=0.5, anchor='center')
    
    clear_tracker_btn = tk.Button(init_w, text='Clear tracker', command=clear_tracker)
    clear_tracker_btn.place(relx=0.2, rely=0.4, anchor='center')
    
    del_btn = tk.Button(init_w, text='Delete', command=del_selection)
    del_btn.place(relx=0.2, rely=0.6, anchor='center')
    
    init_w.mainloop()
    
open_new=tk.Button(root, text = 'Initiative Tracker', command=init_tracker_window)
open_new.place(relx=0.6, rely=0.125, anchor='center')
    
def open_new_window():
    popup = tk.Tk()
    popup.title('Hit chance calculator')
    popup.geometry('500x500')

    AC_label=tk.Label(popup, text='Enter monster AC', font = ('Arial',10,'normal'))
    AC_label.place(relx=0.2, rely=0.1, anchor='center')

    AC_entry=tk.Entry(popup, font = ('Arial',10,'normal'))
    AC_entry.place(relx=0.2, rely=0.15, anchor='center')
    
    as_label=tk.Label(popup, text='Enter Ability plus Item Mod', font = ('Arial',10,'normal'))
    as_label.place(relx=0.2, rely=0.2, anchor='center')

    as_entry=tk.Entry(popup, font = ('Arial',10,'normal'))
    as_entry.place(relx=0.2, rely=0.25, anchor='center')
    
    prof_label=tk.Label(popup, text='Set Prof Bonus', font = ('Arial',10,'normal'))
    prof_label.place(relx=0.2, rely=0.315, anchor='center')

    prof_entry=tk.Scale(popup, from_=1, to=6, orient='horizontal')
    prof_entry.place(relx=0.2, rely=0.4, anchor='center')

    
    output_chance = tk.Listbox(popup)
    output_chance.place(relx=0.55, rely=0.4, anchor='center', height=300, width=100)
    output_chance.configure(background='skyblue4', foreground='white', font=('Arial', 10))
    output_chance_label=tk.Label(popup, text='Chance to hit%:', font = ('Arial',10,'normal'))
    output_chance_label.place(relx=0.55, rely=0.065, anchor='center')
    
    output_ac = tk.Listbox(popup)
    output_ac.place(relx=0.8, rely=0.4, anchor='center', height=300, width=100)
    output_ac.configure(background='skyblue4', foreground='white', font=('Arial', 10))
    output_ac_label=tk.Label(popup, text='Monster AC:', font = ('Arial',10,'normal'))
    output_ac_label.place(relx=0.8, rely=0.065, anchor='center')
    
    current_roll=tk.Label(popup, text='', fg='red', font = ('Arial',10,'normal'))
    current_roll.place(relx=0.5, rely=0.85, anchor='center')
    
    
    def to_hit():
        current_roll['text']="Calculating normally.."
        output_ac.delete(0,"end")
        output_chance.delete(0,"end")
        try:
            AC = int(AC_entry.get())
            prof_bonus=int(prof_entry.get())
            AS=int(as_entry.get())
        except:
            messagebox.showerror('Invalid Input', 'Please enter numbers only')
        total_bonus=prof_bonus+AS
        if total_bonus > AC:
            total_bonus =  AC
        for i in range(0, AC):    
            P = ((21 - (AC-total_bonus))/20 ) * 100
            prob_hit = max(min(P, 95), 5)
            output_chance.insert(tk.END, prob_hit)
            output_ac.insert(tk.END, AC)
            AC-=1
    
    def to_hit_with_adv():
        current_roll['text']="Calculating with Adv.."
        output_ac.delete(0,"end")
        output_chance.delete(0,"end")
        try:
            AC = int(AC_entry.get())
            prof_bonus=int(prof_entry.get())
            AS=int(as_entry.get())
        except:
            messagebox.showerror('Invalid Input', 'Please enter numbers only')
        total_bonus=prof_bonus+AS
        if total_bonus > AC:
            total_bonus = AC
        for i in range(0, AC): 
            P = (1 - (((AC-total_bonus-1)**2)/400)) * 100
            if AC-total_bonus-1 <=-2:
                P = 99.75
            prob_hit = max(min(P, 99.75), 10)
            output_chance.insert(tk.END, prob_hit)
            output_ac.insert(tk.END, AC)
            AC-=1
        
    def to_hit_with_dis():
        current_roll['text']="Calculating with Dis.Adv.."
        output_ac.delete(0,"end")
        output_chance.delete(0,"end")
        try:
            AC = int(AC_entry.get())
            prof_bonus=int(prof_entry.get())
            AS=int(as_entry.get())
        except:
            messagebox.showerror('Invalid Input', 'Please enter numbers only')
        total_bonus=prof_bonus+AS
        if total_bonus > AC:
            total_bonus = AC    
        for i in range(0, AC): 
            P = ((((21+total_bonus-AC)**2)/400)) * 100
            if 21+total_bonus-AC<=-2:
                P = 0.25
            prob_hit = max(min(P, 90.25), 0.25)
            output_chance.insert(tk.END, prob_hit)
            output_ac.insert(tk.END, AC)
            AC-=1
            
    def save_output_text():
        output_ac_list=[]
        output_chance_list=[]
                    
        for item in output_ac.get(0, "end"):
            output_ac_list.append("AC:" + str(item))
                        
        for items in output_chance.get(0, "end"):
            output_chance_list.append(str(items) + "%")
            
        file_path = filedialog.asksaveasfilename(defaultextension=json, filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    dict={}
                    for key,value in zip(output_ac_list, output_chance_list):
                        dict[key]=value
                    file.write(json.dumps(dict, indent=4))
                messagebox.showinfo('File Saved to:', file_path)
            except Exception as e:
                messagebox.showerror('Error', 'An error has occured while saving.')
        
        
    button2 = tk.Button(popup, text='Calculate (No Adv)', command=to_hit)
    button2.place(relx=0.2, rely=0.5, anchor='center')

    button2 = tk.Button(popup, text='Calculate (With Adv)', command=to_hit_with_adv)
    button2.place(relx=0.2, rely=0.6, anchor='center')
    
    button3 = tk.Button(popup, text='Calculate (With Dis.Adv)', command=to_hit_with_dis)
    button3.place(relx=0.2, rely=0.7, anchor='center')
    
    button4 = tk.Button(popup, text='Save table to JSON', command=save_output_text)
    button4.place(relx=0.65, rely=0.75, anchor='center')
    
    popup.mainloop()

open_new=tk.Button(root, text = 'Hit chance calculator', command=open_new_window)
open_new.place(relx=0.6, rely=0.2, anchor='center')

root.bind("<Tab>", exit)
root.mainloop()
