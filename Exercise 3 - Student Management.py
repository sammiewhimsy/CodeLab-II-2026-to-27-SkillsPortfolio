from tkinter import *
from PIL import ImageTk, Image
stu_manage = Tk()
stu_manage.title('Student Management')
stu_manage.geometry('400x520')

#############################################

def switching_frames(frame):
    frame.tkraise()

#def studentinfo(): # this is for when pressing the button so the text appears in that other frame because i don't know how to execute it
    #with open('studentMarks.txt','r') as THELISTOAT: 
            #allstuinfoyay = THELISTOAT.read()
            #stuinfo_here.config(text=allstuinfoyay)
            #showlistbt.config(state=DISABLED)

def studentinfo():
    with open("studentMarks.txt",'r') as THELISTOAT:
        allstuinfoyay = THELISTOAT.read()
        textwidi.delete("1.0",END)
        textwidi.insert(END,allstuinfoyay)
        #showlistbt.config(state=DISABLED)
        #textwidi.config(state=DISABLED)

def highmarksinfo():
    with open("highestMarks.txt",'r') as thehighmarks:
        highmarkshere = thehighmarks.read()
        #textwidi.config(text="")
        textwidi.delete("1.0",END)
        textwidi.insert(END,highmarkshere)

def lowmarksinfo():
    with open("lowestMarks.txt",'r') as thelowmarks:
        lowmarkshere = thelowmarks.read()
        #textwidi.config(text="")
        textwidi.delete("1.0",END)
        textwidi.insert(END,lowmarkshere)

####################################################################################

#### HOME FRAME ####

stuma_homeframe = Frame(stu_manage,bg="#FFFFFF")

#### header
blueframelol = Frame(stuma_homeframe,bg="#221F4C")
blueframelol.place(width=400,height=40)
title_label = Label(stuma_homeframe,text="Bath Spa University",
                    font=('Tahoma',15),bg="#221F4C",fg="#FFFFFF")
title_label.place(x=8,y=4)

#### bathspa image
img = Image.open("bathspa.jpg")
bsuresize = img.resize((400,300))
bsuimage_yay = ImageTk.PhotoImage(bsuresize)
bsuimagebutlabel = Label(stuma_homeframe,image=bsuimage_yay)
bsuimagebutlabel.pack(pady=40)

#### divider
divider = Frame(stuma_homeframe,bg="#221F4C",width=400,height=2)
divider.place(y=345)

#### second header for the buttons
studentmanagerframe = Frame(stuma_homeframe,bg="#221F4C")
studentmanagerframe.place(width=400,height=40,y=350)
stumana_label = Label(stuma_homeframe,text="| Student Manager",
                      font=('Tahoma',15),bg="#221F4C",fg="#FFFFFF")
stumana_label.place(x=15,y=355)

#### white space + slight gray below second header
homewhiteframe = Frame(stuma_homeframe,bg="#DBDBDB",width=400,height=300)
homewhiteframe.place(y=390)
homegrayframe = Frame(stuma_homeframe,bg="#FFFFFF",width=360,height=300)
homegrayframe.place(x=20,y=390)

#### view all student records button
hbt1 = Button(stuma_homeframe,text="View All Students Records",font=('Roboto',13),
              fg="#FFFFFF",bg="#221F4C",
                command=lambda:[switching_frames(all_stu_records)],padx=48)
hbt1.place(x=50,y=410)
#### quit program button
hbt2 = Button(stuma_homeframe,text="Quit Program.",font=('Roboto',13),
              fg="#FFFFFF",bg="#221F4C",
                        command=stu_manage.destroy,padx=92)
hbt2.place(x=50,y=460)

#### placing home frame
stuma_homeframe.place(x=0,y=0,width=400,height=600)

####################################################################################

#### VIEW ALL STUDENT RECORDS ####

all_stu_records = Frame(bg="#FFFFFF")

#### header
sturecordsheader = Frame(all_stu_records,bg="#221F4C")
sturecordsheader.place(width=400,height=40)
title_label = Label(all_stu_records,text="| All Students Records",
                    font=('Tahoma',15),bg="#221F4C",fg="#FFFFFF")
title_label.place(x=15,y=4)
#### returning button
gobackbutton = Button(all_stu_records,text="Return Home",font=('Tahoma',10),bg="#221F4C",
                      fg="#FFFFFF",command=lambda:switching_frames(stuma_homeframe),padx=15)
gobackbutton.place(x=270,y=6)

#### entry so people could search names
sturecordentryframe = Frame(all_stu_records,bg="#58587B")
sturecordentryframe.place(width=400,height=40,y=40)
putnamelabel = Label(all_stu_records,text="| Search Name :",
                     font=('Tahoma',13),bg="#58587B",fg="#FFFFFF")
putnamelabel.place(x=40,y=45)

def selectedname(studentchoice):
    textwidi.delete("1.0",END)
    if studentchoice == "John Curry":
        with open("JohnCurry.txt",'r') as individualstudent:
                studentinfo = individualstudent.read()
                textwidi.insert("1.0",studentinfo)
    elif studentchoice == "Sam Sturivant":
        with open("SamSturivant.txt",'r') as individualstudent:
                studentinfo = individualstudent.read()
                textwidi.insert("1.0",studentinfo)
    elif studentchoice == "Lee Scott":
            with open("LeeScott.txt",'r') as individualstudent:
                    studentinfo = individualstudent.read()
                    textwidi.insert("1.0",studentinfo)
    elif studentchoice == "Matt Thompson":
            with open("MattThompson.txt",'r') as individualstudent:
                    studentinfo = individualstudent.read()
                    textwidi.insert("1.0",studentinfo)
    elif studentchoice == "Ron Herrema":
            with open("RonHerrema.txt",'r') as individualstudent:
                    studentinfo = individualstudent.read()
                    textwidi.insert("1.0",studentinfo)
    elif studentchoice == "Jake Hobbs":
            with open("JakeHobbs.txt",'r') as individualstudent:
                    studentinfo = individualstudent.read()
                    textwidi.insert("1.0",studentinfo)
    elif studentchoice == "Jo Hyde":
            with open("JoHyde.txt",'r') as individualstudent:
                    studentinfo = individualstudent.read()
                    textwidi.insert("1.0",studentinfo)
    elif studentchoice == "Gareth Southgate":
            with open("GarethSouthgate.txt",'r') as individualstudent:
                    studentinfo = individualstudent.read()
                    textwidi.insert("1.0",studentinfo)
    elif studentchoice == "Alan Shearer":
            with open("AlanShearer.txt",'r') as individualstudent:
                    studentinfo = individualstudent.read()
                    textwidi.insert("1.0",studentinfo)
    elif studentchoice == "Les Ferdinand":
            with open("LesFerdinand.txt",'r') as individualstudent:
                    studentinfo = individualstudent.read()
                    textwidi.insert("1.0",studentinfo)

nameslistchoice = [
    "John Curry",
    "Sam Sturivant",
    "Lee Scott",
    "Matt Thompson",
    "Ron Herrema",
    "Jake Hobbs",
    "Jo Hyde",
    "Gareth Southgate",
    "Alan Shearer",
    "Les Ferdinand"
    ]

choiceclicked = StringVar()
choiceclicked.set(nameslistchoice[0])

nameslistdrop = OptionMenu(all_stu_records,choiceclicked, *nameslistchoice,command=selectedname)
nameslistdrop.config(font=('Tahoma',10),fg="#FFFFFF",bg="#58587B",padx=40)
nameslistdrop.place(x=175,y=44)


#putname = Entry(all_stu_records,font=('Tahoma',13),fg="#000000")
#putname.grid(padx=(175,0),pady=47,columnspan=5)

#### divider
divider = Frame(all_stu_records,bg="#221F4C",width=400,height=2)
divider.place(y=82)

#### BUTTONSSSSUH
    # - so i wanna do like. "Show List" then have the highest to lowest buttons next to it

#### show students info + header
buttonsframeswoohoo = Frame(all_stu_records,bg="#58587B")
buttonsframeswoohoo.place(width=400,height=50,y=84,)
showlistbt = Button(all_stu_records,font=('Tahoma',13),
                    text="Show All Students Records",bg="#221F4C",
                    fg="#FFFFFF",command=studentinfo)
showlistbt.place(x=10,y=90)
highmarksbt = Button(all_stu_records,font=('Tahoma',13),
                    text="↑",bg="#221F4C",padx=10,
                    fg="#FFFFFF",command=highmarksinfo)
highmarksbt.place(x=290,y=90)
lowmarksbt = Button(all_stu_records,font=('Tahoma',13),
                    text="↓",bg="#221F4C",padx=10,
                    fg="#FFFFFF",command=lowmarksinfo)
lowmarksbt.place(x=340,y=90)

#### gray frame
homewhiteframe = Frame(all_stu_records,bg="#DBDBDB",width=400,height=390)
homewhiteframe.place(y=134)
homegrayframe = Frame(all_stu_records,bg="#FFFFFF",width=360,height=390)
homegrayframe.place(x=20,y=134)

#### highest to lowest grade AND lowest to highest grade

#### student information

textwidi = Text(all_stu_records,width=40,height=20,
                bg="#FFFFFF",font=('Tahoma',12),wrap="word",
                fg="#221F4C",borderwidth=0)
textwidi.place(x=20,y=134)
# stuinfo_here = Label(all_stu_records,text="",font=('Tahoma',12),
                     #wraplength=290,justify="left",
                     #bg="#FFFFFF",fg="#221F4C")
# tuinfo_here.place(x=40,y=145)

all_stu_records.place(x=0,y=0,width=400,height=600)

# Students Name
# Students Number
# Total coursework mark
# Exam Mark
# Overall percentage (coursework and examination marks contributing in direct proportion to the marks available i.e. the percentage is based on the potential total of 160 marks).
# Student grade ( ‘A’ for 70%+, ‘B’ for 60%-69%, ‘C’ for 50%-59%, ‘D’ for 40%-49%, ‘F’ for under 40% )

####################################################################################

switching_frames(stuma_homeframe)
stu_manage.mainloop()