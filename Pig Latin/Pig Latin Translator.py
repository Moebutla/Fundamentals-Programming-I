#####
#
#   Pig Latin Translator
#   Author: Mose Butler
#   Version: 1.0.0
#   Date: 12/01/18
#
#####

# ATTENTION: All functions are using doc strings to explain what is happening inside. This is used in place of
# comments inside functions.


# Define Functions
def translate_to_english(word):
    """Will translate string from pig latin to english. Takes individual word as parameter,
    splits word into letter elements to be manipulated into english language."""

    characterList = list(word)
    if characterList[-4] == '-':
        for i in range(4):
            if i == 2:
                originalFirstLetter = characterList.pop()
                characterList.insert(0, originalFirstLetter)
            else:
                characterList.pop(-1)
    else:
        for i in range(3):
            characterList.pop(-1)
    translatedWord = "".join(characterList)
    return translatedWord


def translate_to_piglatin(word):
    """Will translate string from english to pig latin. Takes individual word as parameter,
    splits word into letter elements to be manipulated into Pig Latin language."""
    vowels = 'aeiou'
    characterList = list(word)
    if characterList[0] in vowels:
        characterList.append("yay")

    else:
        firstLetter = characterList.pop(0)
        characterList.append("-")
        characterList.append(firstLetter)
        characterList.append("a")
        characterList.append("y")

    translatedWord = "".join(characterList)
    return translatedWord


def main():
    """Creates menu for user. They choose which conversion to use, or to exit program. Conversion choices ask for a
    sentence to be converted. Breaks sentence into list of words before functions are called. Then combines results of
    functions back into sentence."""
    userCommand = input("Choose an option.\n"
                        "[1] Convert English to Pig Latin.\n"
                        "[2] Convert Pig Latin to English. \n"
                        "[3] Exit Program. \n"
                        "Enter Command: ")
    while userCommand not in '123':
        userCommand = input("\nInvalid Command.\n\n"
                            "[1/2/3]: ")

    translatedSentence = []
    if userCommand == '1':
        sentenceInput = input("Enter sentence you would like to translate:\n")
        wordList = sentenceInput.split(" ")
        for i in wordList:
            translatedSentence.append(translate_to_piglatin(i))
    elif userCommand == '2':
        sentenceInput = input("Enter sentence you would like to translate:\n")
        wordList = sentenceInput.split(" ")
        for i in wordList:
            translatedSentence.append(translate_to_english(i))
    else:
        print("\nProgram Exited.")
        exit()

    translatedSentence = " ".join(translatedSentence)
    print(translatedSentence)
    exit()


# Runs Program
main()

