from tkinter import *
from mydb import Database
from tkinter import messagebox

class NLPapp:
    def __init__(self):
        # craeting db object
        self.dbo=Database()

        # login ka gui load karna
        self.root = Tk()
        self.root.title("NLPapp")
        self.root.iconbitmap("resources/favicon.ico")
        self.root.geometry("300x600")
        self.root.configure(bg="#214946")

        self.login_gui()
        self.root.mainloop()

    def login_gui(self):
        self.clear()
        heading = Label(self.root,text="NLPapp",bg="#214946",fg="white")
        heading.pack(pady=(30,30))
        heading.configure(font=("verdana",24,"bold"))

        label1=Label(self.root,text="Enter Email")
        label1.pack(pady=(10,10))

        self.email_input=Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=4)

        label2 = Label(self.root, text="Enter Password")
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=50,show="*")
        self.password_input.pack(pady=(5, 10), ipady=4)

        login_btn=Button(self.root,text="Login",width=30,height=2,command=self.perform_login)
        login_btn.pack(pady=(10,10))

        label3 = Label(self.root, text="Not a Member")
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text="Register Now",command=self.register_gui)
        redirect_btn.pack(pady=(10, 10))

    def register_gui(self):
        self.clear()
        heading = Label(self.root, text="NLPapp", bg="#214946", fg="white")
        heading.pack(pady=(30, 30))
        heading.configure(font=("verdana", 24, "bold"))
        label0 = Label(self.root, text="Enter Name")
        label0.pack(pady=(10, 10))

        self.name_input = Entry(self.root, width=50)
        self.name_input.pack(pady=(5, 10), ipady=4)

        label1 = Label(self.root, text="Enter Email")
        label1.pack(pady=(10, 10))

        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text="Enter Password")
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=50, show="*")
        self.password_input.pack(pady=(5, 10), ipady=4)

        register_btn = Button(self.root, text="Register", width=30, height=2, command=self.perform_registration)
        register_btn.pack(pady=(10, 10))

        label3 = Label(self.root, text="All ready a Member")
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text="Login Now", command=self.login_gui)
        redirect_btn.pack(pady=(10, 10))

    def clear(self):
        # clear the existing
        for i in self.root.pack_slaves():
            i.destroy()

    def perform_registration(self):
        # fetch the data from gui
        name=self.name_input.get()
        email=self.email_input.get()
        password=self.password_input.get()

        response = self.dbo.add_data(name,email,password)

        if response:
            messagebox.showinfo("Success","Registration Successful. You can login Now")
        else:
            messagebox.showerror("Error","Email Already Exists ")

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.search(email,password)
        if response:
            messagebox.showinfo("Success","Login Successful")
            self.home_gui()
        else:
            messagebox.showerror("Error","Invalid Login ")

    def home_gui(self):
        self.clear()
        heading = Label(self.root, text="NLPapp", bg="#214946", fg="white")
        heading.pack(pady=(30, 30))
        heading.configure(font=("verdana", 24, "bold"))

        sentiment_btn = Button(self.root, text="Sentiment", width=30, height=4, command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10, 10))

        ner_btn = Button(self.root, text="Name Entity Recognition", width=30, height=4, command=self.perform_registration)
        ner_btn.pack(pady=(10, 10))

        emotion_btn = Button(self.root, text="Emotion Prediction", width=30, height=4, command=self.perform_registration)
        emotion_btn.pack(pady=(10, 10))

        logout_btn = Button(self.root, text="Login Now", command=self.login_gui)
        logout_btn.pack(pady=(10, 10))

    def sentiment_gui(self):
        self.clear()
        heading = Label(self.root, text="NLPapp", bg="#214946", fg="white")
        heading.pack(pady=(30, 30))
        heading.configure(font=("verdana", 24, "bold"))

        heading2 = Label(self.root, text="Sentiment Analysis", bg="#214946", fg="white")
        heading2.pack(pady=(10, 20))
        heading2.configure(font=("verdana", 24))

        label1 = Label(self.root, text="Enter the Text")
        label1.pack(pady=(10, 10))

        self.sentiment_input = Entry(self.root, width=50)
        self.sentiment_input.pack(pady=(5, 10), ipady=4)

        sentiment_btn = Button(self.root, text="Analyse Sentiment", command=self.login_gui)
        sentiment_btn.pack(pady=(10, 10))

        self.sentiment_result = Label(self.root, text="",bg="#214946",fg="white")
        self.sentiment_result.pack(pady=(10, 10))
        self.sentiment_result.configure(font=("verdana", 16))

        goback_btn = Button(self.root, text="Go back", command=self.home_gui)
        goback_btn.pack(pady=(10, 10))




nlp = NLPapp()
