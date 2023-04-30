from tkinter import *
window= Tk()
window.title("Schedule Meeting ")
window.configure(bg="#37CCD6")

window.geometry("500x500")

def create_new():
    file_name = new_date_entry.get()
    new_file = open(file_name+".txt","a")
    new_file.write(new_entry.get(1.0,END))
    new_file.close()

def search():
    file_n=date_search_entry.get()
    open_file=open(file_n+".txt","r")
    to_do = open_file.read()
    todo_label=Label(window,text=to_do,bg="#37CCD6",font=("Arial Nova Cond","12","bold"))
    todo_label.grid(row=8,column=1,sticky='W',columnspan=4,pady=(20,0))


new_schedule_title = Label(window,text="New Schedule Entry",bg="#37CCD6",font =("Bahschrift","16","bold"))
new_schedule_title.grid(row=1,column=1,rowspan=1)

new_date_label = Label(window,text="Date (yyyy/mm/dd): ",bg="#37CCD6", font=("Arial Nova Cond","12","bold"))
new_date_entry =  Entry(window,width=25)
new_date_label.grid(row=2,column=1,sticky='E',pady=(10,0))
new_date_entry.grid(row=2,column=2,sticky='W',pady=(10,0))


new_entry_label=Label(window,text="Schedule Entry:", bg="#37CCD6",font=("Arial Nova Cond","12","bold"))
new_entry_label.grid(row=3,column=1,sticky='E',pady=(10,0))
new_entry = Text(window,width=30,height=10)
new_entry.grid(row=3,column=2,columnspan=4,sticky='NSEW',pady=(10,0))

new_submit= Button(window,text="Submit",width=10,command=create_new)
new_submit.grid(row=4,column=2,sticky='W',pady=(10,0))

search_label= Label(window,text="Search",bg="#37CCD6",font=("Bahschrift","16","bold"))
search_label.grid(row=5,column=1,rowspan=1,sticky='W',pady=(30,0))


date_search_label = Label(window,text="Date(yyyy/mm/dd):",bg="#37CCD6",font=("Arail Nova Cond","12","bold"))
date_search_entry=Entry(window,width=25)
date_search_label.grid(row=6,column=1,sticky='E',pady=(10,0))
date_search_entry.grid(row=6,column=2,sticky='W',pady=(10,0))

search_button= Button(window,text="Search",width=10,command=search)
search_button.grid(row=7,column=2,sticky='W',pady=(10,0))

window.mainloop()