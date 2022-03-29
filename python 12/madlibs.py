gameoption = input("Which game would you like to play? (1, 2, 3, q (quit): ")
q = quit
if gameoption == 1:
     madlib1()
elif gameoption == 2:
        madlib2()
elif gameoption == 3: 
            madlib3() 
elif gameoption == q:
    print("quit game")
else:
    print ("invalid option")

noun = input("Enter noun: ")
verb = input("Enter verb: ")
pluralnoun = input("Enter plural noun:")
bodypart = input("Enter body part: ")
adjective = input("Enter an adjective: ")
number = input("Enter a number: ")
place = input("Enter a place: ")
ing = input ("Enter an ing word(verb): ")
job = input ("Enter a job: ")
famousperson = input("Enter a famous person: ")

def madlib1(): print ("This is " + noun + ". They are a normal person except they have a special hobby, \
    which is " + verb + ". Every weekend " + noun + " likes to " + noun + " at " + place + " alongside\
     their many " + pluralnoun + " friends." + " One day " + noun + " went sicko mode while " + adjective + ing + " and broke their " + bodypart + " in " + number + " places!")
   
def madlib2(): 
    print ("One day there was someone called " + noun + "." + noun + " is a " + job + " at " + place + "." + "One day at work, " + noun + " ran into " + famousperson + " and instantly fell in love. " + "They got married and had " + number + " kids, with broken " + bodypart + " and owned " + number + pluralnoun + " and resided in " + adjective + place + "." + " On the weekends they spend the days " + ing + ".")

def madlib3():
    print ("One day " + noun + " was at " + place + " to " + verb + "." + " Suddenly, " + noun + "stubbed \
        their " + bodypart + "and instantly fainted" + noun + " awoke and saw" + number + adjective + pluralnoun + " that were " + ing + "around \
            together. This frightened " + noun + " so, they fainted again.") 


