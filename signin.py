from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
from home import HomePage
import pymysql

# def home_page():
#     login_window.destroy()
#     import home

def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='' :
        messagebox.showerror('Error', 'All fields are required!')
    else:
        try:
            con = pymysql.connect(host='localhost',user='root',password='Shruti098%')
            mycursor = con.cursor()
        except:
            messagebox.showerror(('Error', 'Connection is not established!'))
            return
        print ('connection ban gya')
        query = 'use userdata'
        mycursor.execute(query)
        query = 'select * from data where username=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror("Error","Invalid username or password")
        else:
            messagebox.showinfo('Welcome','Login is Successfull !!😊')
            # home_page()
            login_window.withdraw()
            home_page = HomePage(login_window)
            home_page.run()


# FUNCTIONALITY
def signup_page():
    login_window.destroy()
    import signup
def on_entry(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)
def on_entry1(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)
def hide():
    openeye.config(file='images/closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)
def show():
    openeye.config(file='images/openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)


# GUI PART
login_window = Tk()
login_window.geometry('994x664')
login_window.resizable(0, 0)
login_window.title('Login Page')

# background~
bgImage = ImageTk.PhotoImage(file='images/bg.jpg')
bgLabel = Label(login_window, image=bgImage)
bgLabel.place(x=0, y=0)
# bgLabel.grid(row=0,column=0)
# bgLabel.place(x=0,y=0)

# heading
heading = Label(login_window, text="USER LOGIN", font=(
    'Microsoft Yahei UI Light', 23, 'bold'), bg='white', fg='#00043C')
heading.place(x=605, y=120)

# username
usernameEntry = Entry(login_window, width=25, font=(
    'Microsoft Yahei UI Light', 11, 'bold'), bd=0, bg='white', fg='#00043C')
usernameEntry.place(x=580, y=200)
usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>', on_entry)

# PASSWORD
passwordEntry = Entry(login_window, width=25, font=(
    'Microsoft Yahei UI Light', 11, 'bold'), bd=0, bg='white', fg='#00043C')
passwordEntry.place(x=580, y=260)
passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>', on_entry1)

# UNDERLINE
frame1 = Frame(login_window, bg='#00043C', width=250, height=2)
frame1.place(x=580, y=222)

frame2 = Frame(login_window, bg='#00043C', width=250, height=2)
frame2.place(x=580, y=282)

openeye = PhotoImage(file='openeye.png')
closeye = PhotoImage(file='closeye.png')

eyeButton = Button(login_window, image=openeye, bd=0, bg='white',
                   activebackground='white', cursor='hand2', command=hide)
eyeButton.place(x=800, y=255)

# forget password
forgetButton = Button(login_window, text='Forgot Password ?', font=('Microsoft Yahei UI Light',
                      9, 'bold'), bd=0, bg='white', fg='#00043C', activebackground='#FFA3AC', cursor='hand2')
forgetButton.place(x=700, y=290)

# login button   #ffa3ac
loginButton = Button(login_window, text='Login', font=('Open Sans', 16, 'bold'), bg='#FFA3AC',
                     fg='white', activeforeground='#FFA3AC', activebackground='#00043C', cursor='hand2', bd=0, width=19, command=login_user)
loginButton.place(x=580, y=370)

orLabel = Label(login_window, text='-------------- OR ---------------',
                font=('Open Sans', 16), bg='white', fg='#00043C')
orLabel.place(x=580, y=420)

############

# signup button
signupLabel = Label(login_window, text='Dont have an Account?', font=(
    'Open Sans', 10, 'bold'), bg='white', fg='#00043C')
signupLabel.place(x=635, y=470)

# new account button
newaccountButton = Button(login_window, text='Create New Account', font=('Open Sans', 9, 'bold underline'),
                          bg='white', fg='#00043C', activeforeground='white', activebackground='#FFA3AC', cursor='hand2', bd=0, command=signup_page)
newaccountButton.place(x=650, y=500)

login_window.mainloop()
