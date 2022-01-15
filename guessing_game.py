print("*****************************")
print("Welcome to the guessing game!")
print("*****************************")

secret_number = 42

guess = int(input("Insert your guess: "))
print("You guessed", guess)

guessed_right = (guess==secret_number)
guessed_higher = (guess>secret_number)
guessed_lower = (guess<secret_number)

if(guessed_right):
    print("You guessed right!")
elif(guessed_higher):
    print("You guessed wrong! Your guess is higher than the secret number!")
elif(guessed_lower):
    print("You guessed wrong! Your guess is lower than the secret number!")
    

print("End of game")