def play():
    print("****************************")
    print("Welcome to the hangman game!")
    print("****************************")

    secret_word  = "banana"
    hanged = False
    guessed = False
    
    while(not hanged and not guessed):
        guess = input("Take a guess: ")
        guess = guess.strip()
        index = 0
        for letter in secret_word:
            if(guess.upper() == letter.upper()):
                print("Found the letter {} in the position {}".format(letter, index))
            index += 1

    print("End of game")



if(__name__ == "__main__"):
    play()