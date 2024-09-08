import tkinter
import tkinter.messagebox
from tkcalendar import DateEntry

win=tkinter.Tk()
win.title("To Do List")
win.geometry("380x350")
win.configure(bg="light green")

def add_task():
    task=entry_task.get()
    date=date_entry.get()
   
    
    if date and task !="":
         listbox_tasks.insert(tkinter.END,task+"  "+date)
         entry_task.delete(0,tkinter.END)
    else:   
         tkinter.messagebox.showwarning(title="Warning",message="Enter the task and date")
        
def delete_task():
    
    try:
         task_index=listbox_tasks.curselection()[0]
         listbox_tasks.delete(task_index)
    except:
         tkinter.messagebox.showwarning(title="Warning",message="Select the task")

def mark_task():
    
    try:
        mark_index=listbox_tasks.curselection()[0]
        tkinter.messagebox.showinfo(title="message",message="Task completed")
        listbox_tasks.delete(mark_index)
    except:
        tkinter.messagebox.showwarning(title="Warning",message="Select the task")
        

label=tkinter.Label(win,text="TO DO LIST",width=60,bg="light yellow",fg="orange")
label.pack()
   
frame_tasks=tkinter.Frame(win)
frame_tasks.pack()

listbox_tasks=tkinter.Listbox(frame_tasks,height=10,width=60,bg="Light blue")
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks=tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT,fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

frame_entry=tkinter.Frame(win,bg="light grey")
frame_entry.pack()


entry_task=tkinter.Entry(frame_entry,width=50)
entry_task.pack(side=tkinter.LEFT)

date_entry = DateEntry(frame_entry, width=10, background='darkblue',foreground='white', borderwidth=3)
date_entry.pack(side=tkinter.RIGHT,pady=20)

add_button=tkinter.Button(win,text="Add task",width=60,bg="light green",fg="dark blue",command=add_task)
add_button.pack()

mark_button=tkinter.Button(win,text="completed",width=60,bg="light green",fg="dark blue",command= mark_task)
mark_button.pack()


delete_button=tkinter.Button(win,text="Delete task",width=60,bg="light green",fg="dark blue",command=delete_task)
delete_button.pack()

Exit = tkinter.Button(win,text = "Exit",width=60,bg="light green",fg="dark blue",command = exit)
Exit.pack()

win.mainloop()
