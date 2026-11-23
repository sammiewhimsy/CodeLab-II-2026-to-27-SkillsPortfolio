hello hello!!! lots of talking and trying to think of things here...
usually ui is not a problem for me, so i will need to figure out how to do code...

# i put a bunch of #'s to separate stuff for less confusion with how it bothers me okay... okay! thank you!

# EXERCISE 1 - MATH QUIZ
hi i did the gui before even making this... but i have things to change in it so yes...

- # SCRAPS
ok this was cuz i did it wrong ok? ok

E1 = Checkbutton(easyframe,text="1",font=('Roboto',15),fg="#503B58",bg="#FFFFFF")
E2 = Checkbutton(easyframe,text="2",font=('Roboto',15),fg="#503B58",bg="#FFFFFF")
E3 = Checkbutton(easyframe,text="3",font=('Roboto',15),fg="#503B58",bg="#FFFFFF")
E1.pack(anchor=W,padx=15)
E2.pack(anchor=W,padx=15)
E3.pack(anchor=W,padx=15)

M1 = Checkbutton(mediumframe,text="67",font=('Roboto',15),fg="#503B58",bg="#FFFFFF")
M2 = Checkbutton(mediumframe,text="72",font=('Roboto',15),fg="#503B58",bg="#FFFFFF")
M3 = Checkbutton(mediumframe,text="62",font=('Roboto',15),fg="#503B58",bg="#FFFFFF")
M1.pack(anchor=W,padx=15)
M2.pack(anchor=W,padx=15)
M3.pack(anchor=W,padx=15)

H1 = Checkbutton(hardframe,text="6767",font=('Roboto',15),fg="#503B58",bg="#FFFFFF")
H2 = Checkbutton(hardframe,text="6708",font=('Roboto',15),fg="#503B58",bg="#FFFFFF")
H3 = Checkbutton(hardframe,text="6723",font=('Roboto',15),fg="#503B58",bg="#FFFFFF")
H1.pack(anchor=W,padx=15)
H2.pack(anchor=W,padx=15)
H3.pack(anchor=W,padx=15)

# EXERCISE 2 - FUNNY JOKES!
- # THINGS TO DO:
1. make the "show punchline" button work
- # NOTES
so i need to figure out how to:
1. make text change (because i want to have a placeholder text first)
2. add more text for the punchline while making sure it fits in the box i made (stay in the box NOO! stay in the box NOOO!)
    - https://www.geeksforgeeks.org/python/read-a-text-file-using-python-tkinter/ 
    - https://www.geeksforgeeks.org/python/pulling-a-random-word-or-string-from-a-line-in-a-text-file-in-python/ 
    - some angels don't need wings to be angels
- A PERCHANCE...
1. add the "next joke" button after pressing the "tell me a joke" button 
    - not fond of the idea of moving stuff upon pressing buttons
    - HOWEVER... i COULD make use of frames... because i unfortunately don't know any other better method right now it's so sad
- # FIGURING THINGS OUT
1. text loading thing
    - make a function to open and randomize the file's contents

    def show_random_joke():
    with open('randomJokes.txt') as THEJOKESOAT: 
        thejokewoah = THEJOKESOAT.read()

- updating text with buttons : https://stackoverflow.com/questions/73830151/updating-text-in-tkinter-with-a-button-using-a-random-list
2. ok hey it's been awhile i haven't typed here but uhh i'm wondering if i should do something with text previews or appending text or something dude i don't know
- # JUST IN CASE:
def show_random_joke():
    with open('randomJokes.txt','r') as THEJOKESOAT: 
        thejokewoah = THEJOKESOAT.readlines() # read one line of a joke
        jokerandomizer = random.choice(thejokewoah) # to get a random joke
        jokelabelwoah.config(text=jokerandomizer) # to change text in this specific uhh label

telljoke = Button(text="Alexa, tell me a joke!",font=('Tahoma',15),bg="#7DB3B2",padx=15,command=show_random_joke)
- # SCRAPS : 
def show_random_joke():
    with open('randomJokes.txt') as THEJOKESOAT: 
        thejokewoah = THEJOKESOAT.readline().strip()
        jokelabelwoah.config(text=thejokewoah)
        print(random.choice(thejokewoah))


# EXERCISE 3 - STUDENT MANAGEMENT THING