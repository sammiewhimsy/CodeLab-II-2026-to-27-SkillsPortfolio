# add 3 buttons and it should move to diff frames 

from tkinter import *
def switching_frames(frame):
    frame.tkraise()
mathables = Tk()
mathables.title('Math Quiz')
mathables.geometry('400x400')

# home frame YAY YEAAAAHHHH
homeframe = Frame(mathables,bg="#F5E1FB")
home_label = Label(homeframe,text="Math Quiz!",font=('Roboto',20),bg="#503B58",
                   fg="#FFFFFF",padx=20,pady=10)
home_label.place(x=200,y=20)
homeleftframe = Frame(homeframe,bg="#503B58") # frame in home frame for the left side
# homeleftframe = Frame(homeframe,bg="#503B58",width=180) # just a spare idk
homeleftframe.pack(side=LEFT,fill=Y) # to show the left side of home frame
difficultyeasy = Button(homeleftframe,text="Easy",font=('Roboto',15),fg="#FFFFFF",bg="#503B58",
                        command=lambda:switching_frames(easyframe),width=12)
difficultyeasy.pack(padx=20,pady=20)
difficultymedium = Button(homeleftframe,text="Medium",font=('Roboto',15),fg="#FFFFFF",bg="#503B58",
                          command=lambda:switching_frames(mediumframe),width=12)
difficultymedium.pack(padx=20, pady=20)
difficultyhard = Button(homeleftframe,text="Hard",font=('Roboto',15),fg="#FFFFFF",bg="#503B58",
                        command=lambda:switching_frames(hardframe),width=12)
difficultyhard.pack(padx=20,pady=20)
homeframe.place(x=0,y=0,width=400,height=400) # so the home frame will be shown
# my brain is too fried right now to put comments for the difficulty buttons

# easy questions
easyframe = Frame(mathables,bg="#FFFFFF")
easy_label = Label(easyframe,text="Math Quiz - Easy Difficulty",font=('Roboto',20),
                   fg="#503B58",bg="#FFFFFF",pady=8)
easy_label.pack()
easydivider = Frame(easyframe,bg="#503B58",width=10)
easydivider.pack(fill=X,pady=(0,15))
# questions here
Label(easyframe,text="1) 1+1 equals?",font=('Roboto',15),fg="#503B58",bg="#FFFFFF").pack(anchor=W,padx=15)

returnB = Button(easyframe,text="Return",font=('Roboto',10),fg="#FFFFFF",bg="#503B58",
                command=lambda:switching_frames(homeframe),width=12) # button to return to home frame
returnB.pack(padx=20)
easyframe.place(x=0,y=0,width=400,height=400)

# medium questions
mediumframe = Frame(mathables,bg="#FFFFFF")
med_label = Label(mediumframe,text="Math Quiz - Medium Difficulty",font=('Roboto',20),
                   fg="#503B58",bg="#FFFFFF",pady=8)
med_label.pack()
meddivider = Frame(mediumframe,bg="#503B58",width=10)
meddivider.pack(fill=X,pady=(0,15))
# questions here
Label(mediumframe,text="2) 52 + 15 equals?",font=('Roboto',15),fg="#503B58",bg="#FFFFFF").pack(anchor=W,padx=15)

Label(mediumframe,text="(this is technically not medium but hi!)",font=('Roboto',10),fg="#A785B5",
      bg="#FFFFFF").pack(anchor=W,pady=(2,7),padx=15)
returnB = Button(mediumframe,text="Return",font=('Roboto',10),fg="#FFFFFF",bg="#503B58",
                command=lambda:switching_frames(homeframe),width=12) # button to return to home frame
returnB.pack(padx=20)
mediumframe.place(x=0,y=0,width=400,height=400)

# hard questions
hardframe = Frame(mathables,bg="#FFFFFF")
hard_label = Label(hardframe,text="Math Quiz - Hard Difficulty",font=('Roboto',20),
                   fg="#503B58",bg="#FFFFFF",pady=8)
hard_label.pack()
harddivider = Frame(hardframe,bg="#503B58",width=10)
harddivider.pack(fill=X,pady=(0,15))
# questions here
Label(hardframe,text="3) 3250 + 3517 equals?",font=('Roboto',15),fg="#503B58",bg="#FFFFFF").pack(anchor=W,padx=15)

Label(hardframe,text="(this is technically not hard but hi!)",font=('Roboto',10),fg="#A785B5",
      bg="#FFFFFF").pack(anchor=W,pady=(2,7),padx=15)
returnB = Button(hardframe,text="Return",font=('Roboto',10),fg="#FFFFFF",bg="#503B58",
                command=lambda:switching_frames(homeframe),width=12) # button to return to home frame
returnB.pack(padx=20)
hardframe.place(x=0,y=0,width=400,height=400)

switching_frames(homeframe) # show home frame first
mathables.mainloop()