import random
from art import * #library I used to implement ASCII art

#different word lists for some variety
listOfFruits = ["banana","apple","cherry","orange","coconut","lemon","lime","kiwi","grape","peach","plum"]
listOfMammals = ["rhino","leapord","buffalo","bear","wolf","sheep","hippo","panda","mouse","camel","monkey"]
listOfCountries = ["Spain","Croatia","Ghana","Senegal","Namibia","Scotland","Mexico","Brazil","Cuba","China","India"]

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


def main():
    wordToGuess = chooseWord()
    displayBlank(wordToGuess)
    


if __name__ == "__main__":
    main()