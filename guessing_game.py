print("*****************************")
print("Welcome to the guessing game!")
print("*****************************")

secret_number = 42
total_turns = 3
current_turn = 1

for turns in range(current_turn, total_turns + 1):
    print("This is turn {} of {}".format(current_turn, total_turns))
    guess = int(input("Insert your guess: "))
    print("You guessed", guess)

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
    
    
print("End of game")