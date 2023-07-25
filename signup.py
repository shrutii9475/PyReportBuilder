from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import sys
import subprocess
import pymysql


def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmpasswordEntry.delete(0,END)
    check.set(0)

def connect_database():
    
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or confirmpasswordEntry.get()=='' :
        messagebox.showerror('Error', 'All fields are required!')
    elif passwordEntry.get()!= confirmpasswordEntry.get():
        messagebox.showerror('Error','Password Mismatch')
    elif check.get() == 0:
        messagebox.showerror('Error','Please Accept Terms and Conditions!')
    else:
        try:
            con = pymysql.connect(host='localhost',user='root',password='Shruti098%')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error','Database connectivity issue. !')
            return

        # create database
        try: 
            query = 'create database userdata'
            mycursor.execute(query)
            query = 'use userdata'
            mycursor.execute(query)
            query='create table data (id int auto_increment primary key not null, email varchar(50), username varchar(100), password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')
            query='select * from data where username=%s'
            mycursor.execute(query,(usernameEntry.get()))
            row=mycursor.fetchone()
            if row!=None:
                messagebox.showerror('Error','Username Exists!')
            else:
                query='insert into data(email,username,password) values(%s,%s,%s)'
                mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Registration Successfull')
                clear()
                signup_window.destroy()
                import signin


    print("connected to_database!!!")

# def on_password_entry():
#     hide()

def hide():
    openeye.config(file='images/closeye.png')
    confirmpasswordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='images/openeye.png')
    confirmpasswordEntry.config(show='')
    eyeButton.config(command=hide)

def login_page():
    subprocess.Popen([sys.executable, 'signin.py'])
    sys.exit(0)
    # signup_window.destroy()
    # signup_window.exit(0)
    # import signin

signup_window = Tk()
signup_window.title('PyReportBuilder-Signup Page')
signup_window.resizable(0, 0)


background = ImageTk.PhotoImage(file='images/bg.jpg')

bgLabel = Label(signup_window, image=background)
bgLabel.grid()

frame = Frame(signup_window, width=50, height=20, bg='white')
frame.place(x=554, y=100)

#
heading = Label(frame, text='CREATE AN ACCOUNT', font=(
    'Microsoft Yahei UI Light', 18, 'bold'), bg='white', fg='#00043C')
heading.grid(row=0, column=0, padx=10, pady=10)

#
emaillable = Label(frame, text='Email', font=(
    'Microsoft Yahei UI Light', 10, 'bold'), bg='white', fg='#00043C')
emaillable.grid(row=1, column=0, sticky='w', padx=25, pady=(10, 0))

emailEntry = Entry(frame, font=(
    'Microsoft Yahei UI Light',10, 'bold'), bg='#FFA3AC', fg='#00043C', width=30)
emailEntry.grid(row=2, column=0, sticky='w', padx=25)

#
usernameLable = Label(frame, text='User Name', font=(
    'Microsoft Yahei UI Light', 10, 'bold'), bg='white', fg='#00043C')
usernameLable.grid(row=3, column=0, sticky='w', padx=25, pady=(10, 0))

usernameEntry = Entry(frame, font=(
    'Microsoft Yahei UI Light', 10, 'bold'), bg='#FFA3AC', fg='#00043C', width=30)
usernameEntry.grid(row=4, column=0, sticky='w', padx=25)

#
passwordLable = Label(frame, text='Password', font=(
    'Microsoft Yahei UI Light', 10, 'bold'), bg='white', fg='#00043C')
passwordLable.grid(row=5, column=0, sticky='w', padx=25, pady=(10, 0))

passwordEntry = Entry(frame, font=(
    'Microsoft Yahei UI Light', 10, 'bold'), bg='#FFA3AC', fg='#00043C', width=30, show='*')
passwordEntry.grid(row=6, column=0, sticky='w', padx=25)

#
confirmpasswordLable = Label(frame, text='Confirm Password', font=(
    'Microsoft Yahei UI Light', 10, 'bold'), bg='white', fg='#00043C')
confirmpasswordLable.grid(row=7, column=0, sticky='w', padx=25, pady=(10, 0))

confirmpasswordEntry = Entry(frame, font=(
    'Microsoft Yahei UI Light', 10, 'bold'), bg='#FFA3AC', fg='#00043C', width=30, show = '*')
confirmpasswordEntry.grid(row=8, column=0, sticky='w', padx=25)
confirmpasswordEntry.bind('<FocusIn>', hide)

check = IntVar()

#
openeye = PhotoImage(file='images/openeye.png')
# closeye = PhotoImage(file='images/closeye.png')

eyeButton = Button(signup_window, image=openeye, bd=0, bg='white',
                   activebackground='white', cursor='hand2', command=hide)
# eyeButton.place(x=800, y=255)
eyeButton.place(x=790, y=340)

#
tnc = Checkbutton(frame, text='I agree to the Terms and Conditions', font=(
    'Microsoft Yahei UI Light', 8, 'bold'), bg='white', fg='#00043C', activebackground='white', activeforeground='#00043C', variable=check)
tnc.grid(row=9, column=0, sticky='w', padx=10, pady=15)

#
signupButton = Button(frame, text='Sign UP', font=('Open Sans', 16, 'bold'), 
    bd=0, bg='#FFA3AC', fg='white', activebackground='#00043C', activeforeground='#FFA3AC', width=19, cursor = 'hand2',command=connect_database)
signupButton.grid(row=10, column=0)

#
alreadyaccount = Label(frame, text='Already have an Account?', font=(
    'Open Sans', 9, 'bold'), bg='white', fg='#00043C')
alreadyaccount.grid(row=11, column=0, sticky='w', padx=25, pady=(18, 0))

#
loginButton = Button(frame, text='Log In', font=('Open Sans', 9, 'bold underline'), 
    bd=0, cursor='hand2', bg='white', fg='#00043C', activebackground='#FFA3AC', activeforeground='#00043C', command=login_page)
loginButton.place(x=200, y=400)

signup_window.mainloop()
