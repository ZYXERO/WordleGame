
import random

def give_instructions():
    print('''\n Wordle is a word guessing game.
    You have 5 attempts
    (CP) means the letter is in the word and in the correct position.
    (WP) means that the letter is in the word but not in the correct position.
    (NT) means the letter is not there in the word itself.

    Best of Luck! ''')


attempt = 5
words = ["this", "that", "help", "lake", "pink", "cats"]

hidden_word = random.choice(words)

def check_word(guess):
    if hidden_word == guess:
        print("Congrats! You did it!")
        return True
    else:
        result = ""
        for x,y in zip(guess, hidden_word):
            if x==y:
                result = result + "(C)"
            elif x in hidden_word:
                result = result + "(WP)"
            else:
                result = result + "(NT)"
        print(result)
        return False

def main():
    attempt = 5
    while attempt>0:
        guess = input("Enter a four letter word: ")
        if check_word(guess):
            break
        else:
            attempt -= 1 #Attempt reduces by 1
            print (f"You have {attempt} attempts remaining.")
    else:
        print("GAME OVER")  

main()

check_word("Five")
