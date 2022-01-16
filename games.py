import guessing_game
import hangman

print("********************************")
print("Choose the game you want to play")
print("********************************")

print("(1)Guessing Game  (2)Hangman")

game = int(input("Which game to play? "))

if(game == 1):
    print("Playing Guessing Game")
    guessing_game.play()
else:
    print("Playing Hangman")
    hangman.play()