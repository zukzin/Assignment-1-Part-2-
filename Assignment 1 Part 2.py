from tkinter import *
from tkinter import ttk

#colors
co0="#ffffff"
co1="#000000"
co2="#4456F0"

window = Tk()
window.title("My Phone Book")
window.configure(background=co0)
window.resizable(width=FALSE, height=FALSE)

#frames
frame_up = Frame(window, width=500, height=50, bg=co2)
frame_up.grid(row=0, column=0, padx=0, pady=1)

frame_down = Frame(window, width=500, height=150, bg=co0)
frame_down.grid(row=1, column=0, padx=0, pady=1)

frame_table = Frame(window, width=500, height=100, bg=co0)
frame_table.grid(row=2, column=0, columnspan=2, padx=1, sticky=NW)

#functions
def show():
    global tree

    listheader = ['Name','Gender','Telephone','Email']

    demo_list = [[zethu, 'zet@gmail.com', 'F', 7547968547]]

    tree = ttk.Treeview(frame_table, selectmode="extended", columns="listheader", show="headings")

    vsb = ttk.Scrollbar(frame_table, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frame_table, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    show()

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    #tree head
    tree.heading(0, text='Name', anchor=NW)
    tree.heading(1, text='Gender', anchor=NW)
    tree.heading(2, text='Telephone', anchor=NW)
    tree.heading(3, text='Email', anchor=NW)

    #tree column
    tree.column(0, text='Name', anchor=NW)
    tree.column(1, text='Email', anchor=NE)
    tree.column(2, text='Gender', anchor=SW)
    tree.colomn(3, text='Telephone', anchor=SE)

    for item in demo_list:
        tree.insert('', 'end', values=item)

#frame_up widgets
app_name = Label(frame_up, text="My Phone Book", height = 1, font=('Arial 16 bold'), bg=co2, fg=co0)
app_name.place(x=5, y=5)
 

#frame_down widgets
l_name = Label(frame_down, text="Name*", width=20, height=1, font=('Calibri 10'), bg=co0, anchor=NW)
l_name.place(x=12, y=20)
e_name = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief="solid")
e_name.place(x=60, y=20)

l_gender = Label(frame_down, text="Gender*", width=20, height=1, font=('Calibri 10'), bg=co0, anchor=NW)
l_gender.place(x=10, y=50)
c_gender = ttk.Combobox(frame_down, width=27)
c_gender['values'] = ['', 'F', 'M', 'He/She']
c_gender.place(x=80, y=50)

l_telephone = Label(frame_down, text="Telephone*", width=20, height=1, font=('Calibri 10'), bg=co0, anchor=NW)
l_telephone.place(x=10, y=80)
e_telephone = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief="solid")
e_telephone.place(x=80, y=80)

l_email = Label(frame_down, text="Email*", width=20, height=1, font=('Calibri 10'), bg=co0, anchor=NW)
l_email.place(x=10, y=110)
e_email = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief="solid")
e_email.place(x=80, y=110)


b_search = Button(frame_down, text="Search", width=6, height=1, bg=co2, fg=co0, font=('Calibri 8 bold'))
b_search.place(x=290, y=20)
e_search = Entry(frame_down, width=21, justify='left', font=('Calibri 10'), highlightthickness=1, relief="solid")
e_search.place(x=347, y=20)

b_view = Button(frame_down, text="View", width=8, height=1, bg=co2, fg=co0, font=('Calibri 8 bold'))
b_view.place(x=290, y=50)

b_add = Button(frame_down, text="Add", width=8, height=1, bg=co2, fg=co0, font=('Calibri 8 bold'))
b_add.place(x=400, y=50)

b_update = Button(frame_down, text="Update", width=8, height=1, bg=co2, fg=co0, font=('Calibri 8 bold'))
b_update.place(x=400, y=80)

b_delete = Button(frame_down, text="Delete", width=8, height=1, bg=co2, fg=co0, font=('Calibri 8 bold'))
b_delete.place(x=400, y=110)


window.mainloop()
