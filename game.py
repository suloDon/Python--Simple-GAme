import random


def rock_paper_scissor():
    while True:
        option = ["ROCK", "PAPER", "SCISSOR"]
        computer = random.choice(option)
        game = True
        while game:
            You = input("Choose from the given options \n" + str(option)).upper()
            if You == option[0] or You == option[1] or You == option[2]:
                pass
            else:
                print("Choose correct options")
                continue
            if You == "ROCK" and computer == "PAPER":
                print("Computer: ", computer)
                print("You: ", You)
                print("You lose")
            elif You == "ROCK" and computer == "SCISSOR":
                print("Computer: ", computer)
                print("You: ", You)
                print("You won")
            elif You == "ROCK" and computer == "ROCK":
                print("Computer: ", computer)
                print("You: ", You)
                print("Draw")

            if You == "PAPER" and computer == "PAPER":
                print("Computer: ", computer)
                print("You: ", You)
                print("Draw")
            elif You == "PAPER" and computer == "SCISSOR":
                print("Computer: ", computer)
                print("You: ", You)
                print("You lose")
            elif You == "PAPER" and computer == "ROCK":
                print("Computer: ", computer)
                print("You: ", You)
                print("won")

            if You == "SCISSOR" and computer == "PAPER":
                print("Computer: ", computer)
                print("You: ", You)
                print("You won")
            elif You == "SCISSOR" and computer == "SCISSOR":
                print("Computer: ", computer)
                print("You: ", You)
                print("draw")
            elif You == "SCISSOR" and computer == "ROCK":
                print("Computer: ", computer)
                print("You: ", You)
                print("Lose")

            play_again = input("Do You want to play again ? Press Y to play again and others to quit:  ").lower()
            if play_again == "y":
                continue
            else:
                print("THank You")
                break

        break


def check_answer(answer, guess):
    if answer == guess:
        print("Correct Answer")
        return 1
    else:
        print("Incorrect answer")
        print("..................................")
        return 0


def solver(correct_guesses, guesses):
    print("Correct Answers: ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ")
    for i in guesses:
        print(i, end=" ")
    print()
    print("You Scored:" + str(correct_guesses) + "<>" + "out of :",len(questions))


questions = {"Who Created You ?": "A",
             "Where are you from ?": "A",
             "How are You ?": "C"}
options = [["A.Father and mother", "B.Alean", "C.Robot", "D.Dianosour"]
           , ["A.Earth", "B.Jupitar", "C.sun", "D.moon"]
           , ["A.Fine", "B.Sad", "C.Lonly", "D.kathmandu"]]


def quiz_game():
    while True:
        guesses = []
        question_num = 1
        correct_guess = 0
        for key in questions:
            print(key)
            for i in options[question_num-1]:
                print(i)
            guess = input("guess The correct answer ").upper()
            correct_guess += check_answer(questions.get(key), guess)
            print("...........................................")
            guesses.append(guess)
            question_num += 1
        solver(correct_guess,guesses)
        ask = input("Do you want to play again ?"
                    "Press Y if yes and other to exit").upper()
        if ask == "Y":
            continue
        else:
            break









