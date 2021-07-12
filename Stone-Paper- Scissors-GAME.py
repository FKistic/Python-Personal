#Stone, Paer, Scissor game!
import random
while True:
    print("Comp's Turn: Stone(s), Paper(p), Scissors(sc)?: ")
    player=str(input("Player's Turn: Stone(s), Paper(p), Scissors(sc)?: "))
    if player=="s":
        player="Stone"
    elif player=="p":
        player="Paper"
    elif player=="sc":
        player="Scissors"
    comp= random.randint(1, 3)
    if comp==1:
        comp="Stone"
    elif comp==2:
        comp="Paper"
    elif comp==3:
        comp="Scissors"
    def game():
        wins=0
        if comp==player:
            print(f'''Computer chose {comp}, You chose {player}
It's a tie''')
        if comp=="Stone" and player=="Paper":
            print('''Computer chose Stone, You chose Paper
            You Won!''')
            wins+=1
        if comp=="Paper" and player=="Stone":
            print('''Computer chose Paper, You chose Stone
            You Won!''')
            wins+=1
        if comp=="Paper" and player=="Scissors":
            print('''Computer chose Paper, You chose Scissors
            You Won!''')
            wins+=1
        if comp=="Scissors" and player=="Paper":
            print('''Computer chose Scissors, You chose Paper
            You Lost!''')
            wins=0
        if comp=="Stone" and player=="Scissors":
            print('''Computer chose Stone, You chose Scissors
            You Lost!''')
            wins=0
        if comp=="Scissors" and player=="Stone":
            print('''Computer chose Scissors, You chose Stone
            You Won''')
            wins+=1
        print()
        print(f"Your High Score is {wins}")
        with open('HighScore.txt',"w") as high:
            a=high.write(str(wins))
    a=game()
    print()
    print()
    print()


    