import random
import sys
from Revolver import Revolver

bullets = random.randint(1, 6)
revolver = Revolver(type)
stat = []
dict = {'Revolver1': "Dan Wesson 715", 'Revolver2':"Smith & Wesson.315" , 'Revolver3': 'Remington Model 1858',"Revolver4":"Colt Army Model 1860"}
def revolvertype():
    j = input("Please choose your revolver: 1.Dan Wesson 715, 2.Smith & Wesson.315, 3.Remington Model 1858, "
              "4.Colt Army Model 1860")
    if j == "1":
        revolver.settype(dict['Revolver1'])
    elif j == "2":
        revolver.settype(dict['Revolver2'])
    elif j == "3":
        revolver.settype(dict['Revolver3'])
    elif j == "4":
        revolver.settype(dict["Revolver4"])
    else:
        print("Please choose your revolver.")
        revolvertype()

def gettype():
    revolver.gettype()
    main()

def mainmenu():
    print("Please choose one of these options: \n"
     "1.Pick New Revolver\n"
     "2.Check Your Revolver\n"
     "3.Game Start\n"
     "4.Quit\n")
def toss():
    cointoss = random.randint(1,100)
    if cointoss > 50:
        print("it is head!")
        print("Player 1 goes first.")
        stat.append(1)

    if cointoss <= 50:
        print("it is tail!")
        print("Player 2 goes first.")
        stat.append(1)

def game():
    global bullets
    global bulletslot
    print("Good Luck!")
    while True:
        if len(stat) == 1:
            stat.pop()
            while(bullets>0):
                j = input("press enter to pull the trigger")
                bullets = bullets-1
                stat.append(1)
                if bullets > 0:
                    print("MISS", "\n", "LUCKY YOU..", "\n", "Next!")
                game()
            while(bullets==0):
                print("BOOOM", "\n", "YOU ARE DEAD! HAHAHA!")
                asshole = input(print("Do you want to play another game?(y/n)"))
                if asshole == "y":
                    main()
                if asshole == "n":
                    print("Thank you for playing!")
                    sys.exit()
                try:
                    main()
                except:
                    main()

def main():
    mainmenu()
    j=input("")
    if j=="2":
        gettype()
    elif j=="1":
        revolvertype()
        main()
    elif j=="3":
        print("Who will go first? flip it!")
        toss()
        game()
    elif j == "4":
        print("Oh come on,not lucky enough boy? HAHAHAHA")
        sys.exit()
    else:
        print("Please choose the options.")
        main()
print("Welcome to the Russian Roulette!")
main()


