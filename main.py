import game
import application

Banner = """ Select game which you want to play : 
             1. Rock Paper and Scissor
             2. Quiz
             3. Timer
             4. Exit               """
while True:
    try:
        print(Banner)
        select = int(input("Select number which you want to play:  "))
        if select == 1:
            game.rock_paper_scissor()
        if select == 2:
            game.quiz_game()
        if select == 3:
            application.timer()
        if select == 4:
            print("Thank you !!!!!!")
            break
    except ValueError:
        print("Enter correct value")
