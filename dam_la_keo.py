from random import randint
ban = input ()
computer = randint(0,2)
if computer == 0 :
    computer = "dam"
if computer == 1 :
    computer = "la"
if computer == 2 :
    computer = "keo"
print ("---")
print ("ban: " + ban)
print ("computer: " + computer)
print ("---")
if  ban == computer:
    print ("draw")
else:
    if ban == "keo":
        if computer == "dam" :
            print ("lose")
        if computer == "la":
            print ("win")
    elif ban == "la":
        if computer == "dam" :
            print ("win")
        if computer == "keo":
            print ("lose")
    elif ban == "dam":
        if computer == "la" :
            print ("lose")
        if computer == "keo":
            print ("win")
    else:
         print ("nhap sai")