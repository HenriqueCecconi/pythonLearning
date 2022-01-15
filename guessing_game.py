print("*****************************")
print("Welcome to the guessing game!")
print("*****************************")

secret_number = 42

guess = int(input("Insert your guess: "))
print("You guessed", guess)

if(secret_number == guess):
    print("You guessed right!")
elif(secret_number>guess):
    print("You guessed wrong! The secret number is higher.")
elif(secret_number<guess):
    print("You guessed wrong! The secret number is lower.")
    

print("End of game")