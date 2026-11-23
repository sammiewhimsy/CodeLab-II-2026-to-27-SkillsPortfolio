from tkinter import *
from PIL import ImageTk, Image
stu_manage = Tk()
stu_manage.title('Student Management')
stu_manage.geometry('400x600')

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
divider.place(y=346)

#### second header for the buttons

#### placing home frame
stuma_homeframe.place(x=0,y=0,width=400,height=600)

#############################################

# Students Name
# Students Number
# Total coursework mark
# Exam Mark
# Overall percentage (coursework and examination marks contributing in direct proportion to the marks available i.e. the percentage is based on the potential total of 160 marks).
# Student grade ( ‘A’ for 70%+, ‘B’ for 60%-69%, ‘C’ for 50%-59%, ‘D’ for 40%-49%, ‘F’ for under 40% )

#############################################

switching_frames(stuma_homeframe)
stu_manage.mainloop()