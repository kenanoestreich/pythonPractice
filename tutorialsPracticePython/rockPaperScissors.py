"""This file asks two players for their choice in RoShamBo
and returns the winner before asking if they'd like to play 
again"""

while True :
    choice_enum = {'Rock': 1, 'Scissors': 2, 'Paper': 3}
    choice1 = input("Player 1, Enter 'Rock', 'Paper', or 'Scissors': ")
    choice2 = input("Player 2, Enter 'Rock', 'Paper', or 'Scissors': ")
    a = choice_enum.get(choice1)
    b = choice_enum.get(choice2)
    diff = a - b

    if diff in [-1, 2] :
        print("Player 1 wins!")
        if input("If you want to play another game, type 'Yes': ") == "Yes" :
            continue 
        else :
            print("Game Over")
            break
    elif diff in [-2, 1] :
        print("Player 2 wins!")
        if input("If you want to play another game, type 'Yes': ") == "Yes" :
            continue
        else : 
            print("Game Over")
            break
    else : 
        print("Draw. Another Round!\n")
        





