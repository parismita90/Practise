"""
Program for a bookstore.
Developed by : Parismita with help from Ardit(Udemy)
"""

from tkinter import *
import backend

def get_selected_row(event):
    global selected_tuple
    check=len(listb.curselection())
    if check>0:
        index=listb.curselection()[0]
        selected_tuple=listb.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
        #print(selected_tuple[0])

def view_command():
    listb.delete(0,END)
    for rows in backend.view():
        listb.insert(END,rows)

def search_command():
    listb.delete(0,END)
    for rows1 in backend.search(e1_value.get(),e2_value.get(),e3_value.get(),e4_value.get()):
        listb.insert(END,rows1)

def entry_command():
    backend.insert(e1_value.get(),e2_value.get(),e3_value.get(),e4_value.get())
    listb.delete(0,END)
    listb.insert(END,(e1_value.get(),e2_value.get(),e3_value.get(),e4_value.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],e1_value.get(),e2_value.get(),e3_value.get(),e4_value.get())
window=Tk()
window.title("Bookstore")


b1=Button(window,text="View All", width=12, command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search Entry", width=12, command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add Entry",width=12, command=entry_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update Selected",width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete Selected",width=12,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=7,column=3)

e12=Label(window,text="Title")
e12.grid(row=0,column=0)
e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

e22=Label(window,text="Author")
e22.grid(row=0,column=2)
e2_value=StringVar()
e2=Entry(window,textvariable=e2_value)
e2.grid(row=0,column=3)

e32=Label(window,text="Year")
e32.grid(row=1,column=0)
e3_value=StringVar()
e3=Entry(window,textvariable=e3_value)
e3.grid(row=1,column=1)

e42=Label(window,text="ISBN")
e42.grid(row=1,column=2)
e4_value=StringVar()
e4=Entry(window,textvariable=e4_value)
e4.grid(row=1,column=3)

listb=Listbox(window,height=6,width=35)
listb.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

listb.configure(yscrollcommand=sb1.set)
sb1.configure(command=listb.yview)

listb.bind('<<ListboxSelect>>',get_selected_row)

window.mainloop()