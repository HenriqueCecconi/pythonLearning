print("*****************************")
print("Welcome to the guessing game!")
print("*****************************")

secret_number = 42
total_turns = 3

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
    
print("End of game")