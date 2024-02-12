import random, os, time

words = []
wordList = open("commonWordList.txt","r")
for word in wordList.readlines():
    words.append(word.strip())
wordList.close()

hangmanStages = [
("\n\n\n\n\n\n\n  _______"),
("\n     |\n     |\n     |\n     |\n     |\n     |\n  ___|___"),
("      _______\n     |/    |\n     |\n     |\n     |\n     |\n     |\n  ___|___"),
("      _______\n     |/      |\n     |      (_)\n     |\n     |\n     |\n     |\n  ___|___"),
("      _______\n     |/      |\n     |      (_)\n     |       |\n     |       |\n     |\n     |\n  ___|___"),
("      _______\n     |/      |\n     |      (_)\n     |      \|\n     |       |\n     |\n     |\n  ___|___"),
("      _______\n     |/      |\n     |      (_)\n     |      \|/\n     |       |\n     |\n     |\n  ___|___"),
("      _______\n     |/      |\n     |      (_)\n     |      \|/\n     |       |\n     |      /\n     |\n  ___|___"),
("      _______\n     |/      |\n     |      (_)\n     |      \|/\n     |       |\n     |      / \ \n     |\n  ___|___")
]

sessionFinished = False

def refreshScreen():
    os.system("cls")
    print(hangmanStages[hangmanProgress] + "\n" + guessProgress)

while sessionFinished != True:
    gameFinished = False
    wordToGuess = words[random.randrange(1000)]
    guessProgress = ""
    hangmanProgress = 0
    lettersGuessed = ""
    for letter in wordToGuess:
        guessProgress += "_"
    while gameFinished != True:
        while True:
            refreshScreen()
            if lettersGuessed != "":
                print("\n Letters guessed: " + lettersGuessed)
            guessedLetter = input("Guess a letter: ").lower()
            if guessedLetter.isalpha() and len(guessedLetter) == 1:
                if guessedLetter in lettersGuessed:
                    print("Already Guessed")
                    time.sleep(2)
                    pass
                else:
                    break
            else:
                print("Invalid Input")
                time.sleep(2)
                pass
        newProgress = guessProgress
        i = 0
        for character in wordToGuess:
            if character.lower() == guessedLetter:
                newProgress = newProgress[:i] + character + newProgress[(i+1):]
            i += 1
        if newProgress == guessProgress:
            print("letter bad")
            hangmanProgress += 1
        else:
            guessProgress = newProgress
        lettersGuessed += guessedLetter
        if guessProgress == wordToGuess:
            print("Congratulations you won!")
            gameFinished = True
        elif hangmanProgress == 8:
            refreshScreen()
            print("Man dead\nThe word was " + wordToGuess)
            gameFinished = True
    while True:
        answer = input("Do yo want to play hangman again? (Y/N): ").upper()
        if answer != "Y" and answer != "N":
            print("invaild input")
            pass
        else:
            break
    if answer == "N":
        sessionFinished = True