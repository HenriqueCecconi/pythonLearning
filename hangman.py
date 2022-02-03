def play():
    print("****************************")
    print("Welcome to the hangman game!")
    print("****************************")

    secret_word  = "banana".upper()
    letters_guessed = ["_" for letter in secret_word]

    hanged = False
    guessed = False
    errors = 0
    
    while(not hanged and not guessed):
        print(letters_guessed)
        guess = input("Take a guess: ")
        guess = guess.strip().upper()
        if(guess in secret_word):
            index = 0
            for letter in secret_word:
                if(guess == letter):
                    letters_guessed[index] = letter
                index += 1
        else:
            errors += 1

        hanged = (errors == 6)
        guessed = ('_' not in letters_guessed)

    if(guessed):
        print(letters_guessed)
        print("You win!")
    else:
        print("You lose!")
        print("The secret word was {}".format(secret_word.upper()))

    print("End of game")



if(__name__ == "__main__"):
    play()