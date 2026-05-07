from tkinter import*
from tkinter import ttk
from db import Database
from tkinter import messagebox
db=Database('Employee.db')

root=Tk()


name=StringVar()
age=StringVar()
jop=StringVar()
gender=StringVar()
email=StringVar()
mobaile=StringVar()




root.title('Employee Managment System')
root.geometry('1540x850')
root.resizable(False,False)
root.configure(bg='#2c3e50')
#-------frames------------

entries_frame=Frame(root,bg='white',width=360,height=850)
entries_frame.place(x=5,y=5)

#-----------defnations------------

def hide():
 root.geometry('360x815')
      
def show():
 root.geometry('1540x1300+0+0')
    
bthide=Button(entries_frame,text='HIDE',command=hide,bd=1,relief=SOLID)
bthide.place(x=270,y=10)

btshow=Button(entries_frame,text='SHOW',command=show,bd=1,relief=SOLID) 
btshow.place(x=310,y=10)


 


title=Label(entries_frame,text='Employee Company',font=('calibri',18,'bold'),justify='center',bg='grey')
title.place(x=10,y=10)

labl_name=Label(entries_frame,text='Name :',width=10,font=('Tajawal',15))
labl_name.place(x=1,y=80)

txt_name=Entry(entries_frame,width=20,bg='white',justify='center',textvariable=name)
txt_name.place(x=140,y=85,width=160,height=25)

jop_label=Label(entries_frame,text='Jop :',width=10,font=('Tajawal',15))
jop_label.place(x=1,y=140)

txt_jop=Entry(entries_frame,width=20,bg='white',justify='center',textvariable=jop)
txt_jop.place(x=140,y=145,width=170,height=25)



gender_label = Label(entries_frame, text='Gender :', width=10, font=('Tajawal', 15))
gender_label.place(x=1, y=200)

combogender = ttk.Combobox(entries_frame, textvariable=gender, width=18, state='readonly')
combogender['values'] = ('Male', 'Female')
combogender.place(x=140, y=205, width=170, height=25)


label_age=Label(entries_frame,text='Age :',width=10,font=('Tajawal',15))
label_age.place(x=1,y=260)

txt_age=Entry(entries_frame,width=20,bg='white',justify='center',textvariable=age)
txt_age.place(x=140,y=265,width=170,height=25)


label_Email=Label(entries_frame,text='Email :',width=10,font=('Tajawal',15))
label_Email.place(x=1,y=320)

txt_email=Entry(entries_frame,width=20,bg='white',justify='center',textvariable=email)
txt_email.place(x=140,y=320,width=170,height=25)

label_mobaile=Label(entries_frame,text='Mobaile :',width=10,font=('Tajawal',15))
label_mobaile.place(x=1,y=380)

txt_mobail=Entry(entries_frame,width=20,bg='white',justify='center',textvariable=mobaile)
txt_mobail.place(x=140,y=380,width=170,height=25)

labl_adress=Label(entries_frame,text='Adress :',width=10,font=('Tajawal',15))
labl_adress.place(x=1,y=440)

txt_adress=Entry(entries_frame,width=20,bg='white',justify='left')
txt_adress.place(x=140,y=440,width=170,height=25)




#_____________getdata_____________


def getData(event):
    selected_row = tv.focus()
    if not selected_row:
        return

    data = tv.item(selected_row)
    global row
    row = data['values']

    name.set(row[1])
    age.set(row[2])
    jop.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    mobaile.set(row[6])

    txt_adress.delete(0, END)
    txt_adress.insert(0, row[7])

def displayAll():
    
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert('',END,values=row)



def add_employee():
    if name.get()=='' or age.get()=='' or jop.get()=='' or gender.get()=='' or email.get()=='' or mobaile.get()=='' or txt_adress.get()=='':
        messagebox.showerror('Error','Please fill all fields')
        return

    db.insert(
        name.get(),
        age.get(),
        jop.get(),
        email.get(),
        gender.get(),
        mobaile.get(),
        txt_adress.get()
    )
    displayAll()
    clear()
    

    
def clear():
      name.set('')
      age.set('')
      jop.set('')
      gender.set('')
      email.set('')
      mobaile.set('')
      txt_adress.delete(0, END)
      
    
def delete():
    try:
        db.remove(row[0])
        clear()
        displayAll()
    except:
        messagebox.showerror("Error", "Please select a record first")
    
def update():
    try:
        if not row:
            raise Exception()

        db.update(
            row[0],
            name.get(),
            age.get(),
            jop.get(),
            email.get(),
            gender.get(),
            mobaile.get(),
            txt_adress.get()
        )
        displayAll()
        clear()

    except:
        messagebox.showerror("Error", "Select record first")

# --------Bottons Frame--------

btn_frame=Frame(entries_frame,bg='#35F527',relief=SOLID)
btn_frame.place(x=1,y=480,width=360,height=170)

b1_add=Button(btn_frame, text= 'Add Details',bg='red',fg='black',bd=0,font=('Calibri',16),width=13,command=add_employee).place(x=1,y=20)

b2_update=Button(btn_frame, text= 'Update Details'     ,bg='red',fg='black',bd=0,font=('Calibri',16),width=13,command=update).place(x=1,y=90)


b3_Delete=Button(btn_frame, text= 'Delete Details'     ,bg='red',fg='black',bd=0,font=('Calibri',16),width=13,command=delete).place(x=190,y=20)

b4_Delete=Button(btn_frame, text= 'Clear Details'     ,bg='red',fg='black',bd=0,font=('Calibri',16),width=13,command=clear).place(x=190,y=90)



#logo------------
logo=PhotoImage(file='logo.png')
lb1_logo=Label(entries_frame,image=logo)
lb1_logo.place(x=8,y=660,width=333,height=233)





#____________Table Frame______________

tree_Frame=Frame(root,bg='gray')
tree_Frame.place(x=365,y=5,width=1160,height=825)
style=ttk.Style()
style.configure('mystyle.Treeview', font=('calibri', 13), rowheight=50)
style.configure('mystyle.Treeview.Heading',font=('calibri', 13))

tv=ttk.Treeview(tree_Frame,columns=(1,2,3,4,5,6,7,8),style='mystyle.Treeview',height=17)
tv.heading('1',text='ID')
tv.column('1',width=140)

tv.heading('2',text='Name')
tv.column('2',width=150)

tv.heading('3',text='Age')
tv.column('3',width=90)


tv.heading('4',text='Jop')
tv.column('4',width=120)


tv.heading('5',text='Email')
tv.column('5',width=190)


tv.heading('6',text='Gender')
tv.column('6',width=130)



tv.heading('7',text='Mobaile')
tv.column('7',width=150)



tv.heading('8',text='Adress')
tv.column('8',width=190)



tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)



#---------------------Defines-------------------




tv.pack()
displayAll()

root.mainloop()