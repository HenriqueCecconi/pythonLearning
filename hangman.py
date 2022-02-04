import random as rd


def play():
    show_opening_messaging()

    secret_word = load_secret_word()

    letters_guessed = initialize_letters_guessed(secret_word)

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
            print_hanged_man(errors)

        hanged = (errors == 7)
        guessed = ('_' not in letters_guessed)

    if(guessed):
        show_ending_winner()
    else:
        show_ending_loser(secret_word)

    print("End of game")


def show_opening_messaging():
    print("****************************")
    print("Welcome to the hangman game!")
    print("****************************")

def show_ending_winner():
    print("Congratulations! You guessed the secret word")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def show_ending_loser(secret_word):
    print("Too bad, you got hanged!")
    print("The secret word was {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def load_secret_word():
    file_input = open("fruits.txt", "r")
    words = []

    for line in file_input:
        line = line.strip()
        words.append(line)    
    
    file_input.close()

    index_of_selected_word = rd.randrange(0, len(words))
    secret_word = words[index_of_selected_word].upper()
    return secret_word

def initialize_letters_guessed(secret):
    return ["_" for letter in secret]

def print_hanged_man(errors):
    print("  _______     ")
    print(" |/      |    ")

    if(errors == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(errors == 2):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")

    if(errors == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(errors == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(errors == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(errors == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (errors == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    play()