import random as rdm

def play(): 
    print("*****************************")
    print("Welcome to the guessing game!")
    print("*****************************")

    secret_number = rdm.randrange(1, 101)
    points = 1000

    print("Choose your difficulty level:")
    print("(1)Easy (2)Medium (3)Hard")
    difficulty_level = int(input("Your choice: "))

    if(difficulty_level == 1):
        total_turns = 20
    elif(difficulty_level == 2):
        total_turns = 10
    elif(difficulty_level == 3):
        total_turns = 5
    else:
        print("Insert a valid difficulty level")

    for turn in range(1, total_turns + 1):
        print("This is turn {} of {}".format(turn, total_turns))
        guess = int(input("Insert a guess between 1 and 100: "))
        if(guess < 1 or guess > 100):
            print("Make a guess inside the range!")
            continue
        print("You guessed:", guess)

        guessed_right = (guess==secret_number)
        guessed_higher = (guess>secret_number)
        guessed_lower = (guess<secret_number)

        if(guessed_right):
            print("Congratulations! You guessed right!")
            break
        elif(guessed_higher):
            print("You guessed wrong! Your guess is higher than the secret number!")
        elif(guessed_lower):
            print("You guessed wrong! Your guess is lower than the secret number!")

        lost_points = abs(secret_number - guess)
        points -= lost_points
        
    print("End of game")
    print("Your got {} points!".format(points))