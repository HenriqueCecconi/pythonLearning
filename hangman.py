def play():
    print("****************************")
    print("Welcome to the hangman game!")
    print("****************************")

    secret_word  = "banana"
    letters_guessed = ["_", "_", "_", "_", "_", "_"]

    hanged = False
    guessed = False
    
    while(not hanged and not guessed):
        print(letters_guessed)
        guess = input("Take a guess: ")
        guess = guess.strip()
        index = 0
        for letter in secret_word:
            if(guess.upper() == letter.upper()):
                letters_guessed[index] = letter
            index += 1

    print("End of game")



if(__name__ == "__main__"):
    play()