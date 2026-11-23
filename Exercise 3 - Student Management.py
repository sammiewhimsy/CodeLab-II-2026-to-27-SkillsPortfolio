from tkinter import *
from PIL import ImageTk, Image
stu_manage = Tk()
stu_manage.title('Student Management')
stu_manage.geometry('400x520')

#############################################

def switching_frames(frame):
    frame.tkraise()

#############################################

#### HOME FRAME ####

stuma_homeframe = Frame(stu_manage,bg="#FFFFFF")

#### header
blueframelol = Frame(stuma_homeframe,bg="#221F4C")
blueframelol.place(width=400,height=40)
title_label = Label(stuma_homeframe,text="Bath Spa University",font=('Tahoma',15),bg="#221F4C",fg="#FFFFFF")
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
stumana_label = Label(stuma_homeframe,text="| Student Manager",font=('Tahoma',15),bg="#221F4C",fg="#FFFFFF")
stumana_label.place(x=15,y=355)

#### white space + slight gray below second header
homewhiteframe = Frame(stuma_homeframe,bg="#DBDBDB",width=400,height=300)
homewhiteframe.place(y=390)
homegrayframe = Frame(stuma_homeframe,bg="#FFFFFF",width=360,height=300)
homegrayframe.place(x=20,y=390)

#### HERE COME THE BUTTONS !!!! ####

#### view all student records button
hbt1 = Button(stuma_homeframe,text="View All Students Records.",font=('Roboto',13),fg="#FFFFFF",bg="#221F4C",
                        command=lambda:switching_frames(all_stu_records),padx=45)
hbt1.place(x=50,y=410)
#### quit program button
hbt2 = Button(stuma_homeframe,text="Quit Program.",font=('Roboto',13),fg="#FFFFFF",bg="#221F4C",
                        command=stu_manage.destroy,padx=92)
hbt2.place(x=50,y=460)

#### placing home frame
stuma_homeframe.place(x=0,y=0,width=400,height=600)

#############################################

#### VIEW ALL STUDENT RECORDS ####

all_stu_records = Frame(bg="#FFFFFF")

#### header
sturecordsheader = Frame(all_stu_records,bg="#221F4C")
sturecordsheader.place(width=400,height=40)
title_label = Label(all_stu_records,text="| All Students Records",font=('Tahoma',15),bg="#221F4C",fg="#FFFFFF")
title_label.place(x=15,y=4)

#### entry so people could search names
putname = Entry()

all_stu_records.place(x=0,y=0,width=400,height=600)

# Students Name
# Students Number
# Total coursework mark
# Exam Mark
# Overall percentage (coursework and examination marks contributing in direct proportion to the marks available i.e. the percentage is based on the potential total of 160 marks).
# Student grade ( ‘A’ for 70%+, ‘B’ for 60%-69%, ‘C’ for 50%-59%, ‘D’ for 40%-49%, ‘F’ for under 40% )

#############################################

switching_frames(stuma_homeframe)
stu_manage.mainloop()