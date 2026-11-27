from tkinter import *
funnykoke = Tk() # i made a typo when trying to type "joke" but i thought it was funny so i will keep it
funnykoke.title('Joke Central')
funnykoke.geometry('400x430')
funnykoke.config(bg="#FFFFFF")
import random

# functions idk

with open('randomJokes.txt','r') as THEJOKESOAT: 
    thejokers = [joke.strip().split("|",1) for joke in THEJOKESOAT if "|" in joke and joke.strip()]

def show_first_joke():
    with open('randomJokes.txt','r') as THEJOKESOAT: 
        first_joke_woah = THEJOKESOAT.readlines()
        first_random_joke = random.choice(first_joke_woah)
        joketextbox.insert(END,first_random_joke)
        # jokelabelwoah.config(text=first_random_joke)
        telljoke.config(state=DISABLED) # so the button won't function after clicking

shown_joke = ""

def more_jokes():
    global shown_joke
    if not thejokers:
        return

    thejoke,thepunchline = random.choice(thejokers)
    shown_joke = thepunchline.strip()

def punchline():
    if shown_joke:
        joketextbox.insert(END,"\n{shown_joke}")


# def next_joke():
#     with open('randomJokes.txt','r') as THEJOKESOAT: 
#         thejokewoah = THEJOKESOAT.readlines() # read one line of a joke
#         jokerandomizer = random.choice(thejokewoah) # to get a random joke
#         jokelabelwoah.config(text=jokerandomizer) # to change text in this specific uhh label

#### SPARES JUST IN CASE I AM SCARED
# def show_first_joke():
#     with open('randomJokes.txt','r') as THEJOKESOAT: 
#         first_joke_woah = THEJOKESOAT.readlines()
#         first_random_joke = random.choice(first_joke_woah)
#         jokelabelwoah.config(text=first_random_joke)
#         telljoke.config(state=DISABLED) # so the button won't function after clicking
# def next_joke():
#     with open('randomJokes.txt','r') as THEJOKESOAT: 
#         thejokewoah = THEJOKESOAT.readlines() # read one line of a joke
#         jokerandomizer = random.choice(thejokewoah) # to get a random joke
#         jokelabelwoah.config(text=jokerandomizer) # to change text in this specific uhh label

# uhhhhhhhhhhhhhhhhhhhhhhhhh header
blueframelol = Frame(bg="#7DB3B2")
blueframelol.place(width=400,height=70)
title_label = Label(funnykoke,text="Welcome to JOKE CENTRAL!!!",font=('Tahoma',20),bg="#7DB3B2")
title_label.place(x=20,y=15)

divider = Frame(bg="#7DB3B2",width=400,height=2)
divider.place(x=0,y=83)

telljoke = Button(text="Alexa, tell me a joke!",font=('Tahoma',15),bg="#7DB3B2",padx=15,
                  command=show_first_joke)
telljoke.place(x=83,y=106)

# lowk this should appear after pressing the button !!!!!!!!!!! or have placeholder text, at least

#################################################
#################################################

jokesboxoutlime = Frame(bg="#7DB3B2") # there's probably a better way to add borders but idk
jokesboxoutlime.place(width=350,height=130,x=26,y=165) # typo butsure
mainjokeshere = Frame(bg="#FFFFFF")
mainjokeshere.place(width=340,height=120,x=31,y=170)

joketextbox = Text(funnykoke,height=4,width=33,font=('Tahoma',12),border=0)
joketextbox.place(x=48,y=195)

# jokelabelwoah = Label(text="",font=('Tahoma',12),wraplength=290,bg="#FFFFFF",justify="left")
# jokelabelwoah.place(x=55,y=195)
# joke displayed here ^

nextjokebutton = Button(text="Next Joke!",font=('Tahoma',10),bg="#7DB3B2",padx=10)
                        #command=next_joke)
nextjokebutton.place(x=217,y=310) # 65 66 67 68:kyaaaaa 69
showpunchlinebutton = Button(text="Show Punchline!",font=('Tahoma',10),bg="#7DB3B2",padx=2,
                             command=punchline)
showpunchlinebutton.place(x=100,y=310)

#### SPARES
# jokesboxoutlime = Frame(bg="#7DB3B2") # there's probably a better way to add borders but idk
# jokesboxoutlime.place(width=350,height=130,x=26,y=165) # typo butsure
# mainjokeshere = Frame(bg="#FFFFFF")
# mainjokeshere.place(width=340,height=120,x=31,y=170)

# jokelabelwoah = Label(text="",font=('Tahoma',12),wraplength=290,bg="#FFFFFF",justify="left")
# jokelabelwoah.place(x=55,y=195)
# # joke displayed here ^

# nextjokebutton = Button(text="Next Joke!",font=('Tahoma',10),bg="#7DB3B2",padx=10,command=next_joke)
# nextjokebutton.place(x=217,y=310) # 65 66 67 68:kyaaaaa 69
# showpunchlinebutton = Button(text="Show Punchline!",font=('Tahoma',10),bg="#7DB3B2",padx=2)
# showpunchlinebutton.place(x=100,y=310)

divider = Frame(bg="#7DB3B2",width=400,height=2)
divider.place(x=0,y=360)

quitbutton = Button(text="Close Program.",font=('Tahoma',10),bg="#7DB3B2",padx=2,command=funnykoke.destroy)
quitbutton.place(x=150,y=375)

funnykoke.mainloop()