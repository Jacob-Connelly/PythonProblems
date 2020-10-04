game = True;

while game:
    while game:
        count = 1;
        print("Round {}".format(count))
        print("Please input Rock, Paper, or Scissors")
        p1 = input("Player 1:")
        p2 = input("Player 2:")

        if p1 == p2:
            print("tie")
        elif (p1 == "Rock" and p2 == "Paper") or (p2 == "Rock" and p1 == "Paper"):
            if p1 == "Paper":
                print("Player 1 wins!")
                break
            else:
                print("Player 2 wins!")
                break
        elif (p1 == "Scissors" and p2 == "Paper") or (p1 == "Paper" and p2 == "Scissors"):
            if p1 == "Scissors":
                print("Player 1 wins!")
                break
            else:
                print("Player 2 wins!")
                break
        else:
            if p1 == "Rock":
                print("Player 1 wins!")
                break
            else:
                print("Player 2 wins!")
                break
        count += 1

    play = input("Would you like to play again(y/n)?")
    if play == "y":
        print("New Game Started")
    else:
        print("Game Ended")
        break