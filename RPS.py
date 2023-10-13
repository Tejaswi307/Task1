import random
play=["Rock","Paper","Scissors"]
computer=play[random.randint(0,2)]
player=False
while player==False:
    player=input("Rock,Paper,Scissors?")
    if player==computer:
        print("Tie!")
    elif player=="Rock":
        if computer=="Paper":
            print("You Lose!",computer,"covers",player)
        else:
            print("You Win!",player,"smashes",computer)
    elif player=="Paper":
        if computer=="Scissors":
            print("You Lose!",computer,"cuts",player)
        else:
            print("You Win!",player,"covers",computer)
    elif player=="Scissors":
        if computer=="Rock":
            print("You Lose..",computer,"smashes",player)
        else:
            print("You Win!",player,"cuts",computer)
    else:
        print("That's not a vaild play. Check the spelling!")
    player=False
    computer=play[random.randint(0,2)]
    
            
