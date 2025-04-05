import random
from art import * #library I used to implement ASCII art
import pygame 
import time 
import sys

#different word lists for some variety
listOfFruits = ["banana","apple","cherry","orange","coconut","lemon","lime","kiwi","grape","peach","plum"]
listOfMammals = ["rhino","leapord","buffalo","bear","wolf","sheep","hippo","panda","mouse","camel","monkey"]
listOfCountries = ["Spain","Croatia","Ghana","Senegal","Namibia","Scotland","Mexico","Brazil","Cuba","China","India"]

#the WAV files we'll play 
correctArchadeSound = "sounds\CorrectGuess.wav"
repeatedGuessSound = "sounds\AlreadyGuessedThatLetter.wav"
playerWinsSound = "sounds\Win.wav"
wrongAnswerWAV = "sounds\Wrong.wav"
repeatedGuessWAV = "sounds\AlreadyGuessedThatLetter.wav"
youLoseWAV = "sounds\Lose.wav"

def chooseWord():
    """
    A function that chooses a random word from a randomword list, and provides a hint based on the list it comes from

        Returns: randomWord (string): a random choice from one of the word lists
    """

    whichList = random.randint(1,3)
    match whichList:
        case 1:
            wordList = listOfFruits
            randomWord = random.choice(listOfFruits)
            print("\nEnter a letter to guess if it is part of the word.\nHint: This item is edible! ")
        case 2:
            wordList = listOfMammals
            randomWord = random.choice(listOfMammals)
            print("\nEnter a letter to guess if it is part of the word.\nHint: This word is a mammal! ")
        case 3:
            wordList = listOfCountries
            randomWord = random.choice(listOfCountries)
            print("\nEnter a letter to guess if it is part of the word.\nHint: This word is a country! ")
    return randomWord

def displayBlank(wordChosen):
    """
    A function that creates and displays sequence of underscores for the player to fill, based on the word chosen

        Args: wordChosen (string): the word previously chosen at random from a list

        Returns: blankWord (string): a sequence of underscores corresponding with the amount of letters in the word
    """
    blankWord = "_" * len(wordChosen)
    print(text2art(blankWord, font="block",chr_ignore=True))
    return blankWord

def guessLetter(letter,incompleteWord,correctWord):
    """
    A function that updates a word after the player has guessed a letter

        Args: letter (string): the letter guessed

              incompleteWord (string): the word with underscores in the unguessed indexes e.g. "_ppl_" for "apple"

              correctWord (string): the word the player has to guess
        
        Returns: a tuple containing the updated word after a guess and a boolean 
                 stating whether or not the word was updated after the player guessed e.g ("a____",True)
              
    """
    updated = False
    updatedWordAsList = list(incompleteWord)
    for character in range(len(correctWord)):
        if correctWord[character]!= letter:
            pass
        else:
            updatedWordAsList[character] = letter
            updated =  True

    return ("".join(updatedWordAsList),updated)

def play(randomWord,blankWord): 
    """
    A function that allows the player to guess a letter with up to 7 incorrect guesses

    """
    wrongAttemptsAllowed = 7
    lettersCompleted = 0
    solved = False
    lettersAlreadyGuessed = []

    while solved == False:

        correctGuess = False
        letterChosen = input("Guess a letter! ").lower()
        wordWithPlayerGuess = guessLetter(letterChosen,blankWord,randomWord)[0]
        correctGuess = guessLetter(letterChosen,blankWord,randomWord)[1]
        
        if correctGuess == True:
            if letterChosen in lettersAlreadyGuessed:
                repeatedGuessSound = pygame.mixer.Sound(repeatedGuessWAV)
                repeatedGuessSound.play()
                print(f"\nYou already guessed that letter. Try again. You have {wrongAttemptsAllowed} attempts left")
                continue
            else:
                lettersAlreadyGuessed.append(letterChosen)

            lettersCompleted += randomWord.count(letterChosen)
            correctGuessSound = pygame.mixer.Sound(correctArchadeSound)
            correctGuessSound.play()
            if wrongAttemptsAllowed!= 0 and lettersCompleted!= len(randomWord):
                match wrongAttemptsAllowed:
                    case 1:
                        print(f"CORRECT. You have 1 attempt left")
                    case _:
                        print(f"CORRECT. You have {wrongAttemptsAllowed} attempts left")
            elif lettersCompleted == len(randomWord):
                youWinSound = pygame.mixer.Sound(playerWinsSound)
                print(text2art(wordWithPlayerGuess, font="block",chr_ignore=True))
                time.sleep(1)
                print(text2art("YOU WIN !", font="block",chr_ignore=True))
                youWinSound.play()
                time.sleep(3)
                solved = True
                sys.exit()
                
        
        else:
            wrongAttemptsAllowed -= 1
            if wrongAttemptsAllowed==0:
                # # print()
                # time.sleep(1)
                gameOverSound1 = pygame.mixer.Sound(youLoseWAV)
                gameOverSound1.play()
                print("You are out of attempts")
                print(text2art("GAMEOVER", font="block",chr_ignore=True))
                time.sleep(3)
                sys.exit()    

            incorrectGuessSound = pygame.mixer.Sound(wrongAnswerWAV)
            incorrectGuessSound.play()
            print(f"INCORRECT. You have {wrongAttemptsAllowed} attempts left")

        print(text2art(wordWithPlayerGuess, font="block",chr_ignore=True))
        blankWord = wordWithPlayerGuess
    

def main():
    pygame.init()
    pygame.mixer.init()

    wordToGuess = chooseWord().lower()
    emptyWord = displayBlank(wordToGuess)
    play(wordToGuess,emptyWord)



if __name__ == "__main__":
    main()

"""
Things to implement:
-accounting for inputting the same incorrect letter
-print instructions before game starts
-use a bigger, bolder font

-incorrect repeated guess, don't subtract attempts
-reveal the word when the game is over after a loss
"""