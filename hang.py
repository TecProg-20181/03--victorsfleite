import random
import string

WORDLIST_FILENAME = 'palavras.txt'
GUESSES_LIMIT = 8


def loadWords():
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print 'Loading word list from file...'

    inFile = open(WORDLIST_FILENAME, 'r', 0)
    line = inFile.readline()
    wordlist = string.split(line)

    print '  ', len(wordlist), 'words loaded.'

    return wordlist


def chooseWord(wordList):
    secretWord = random.choice(wordList)
    while len(set(secretWord)) > GUESSES_LIMIT:
        wordList.remove(secretWord)
        secretWord = random.choice(wordList)

    return secretWord


def isWordGuessed(lettersGuessed):
    return True if SECRETWORD == getGuessedWord(lettersGuessed) else False


def getGuessedWord(lettersGuessed):
    guessed = ''
    for letter in SECRETWORD:
        guessed += letter if letter in lettersGuessed else ' _ '

    return guessed


def getNumberOfGuesses(lettersGuessed):
    if not lettersGuessed:
        return GUESSES_LIMIT

    return GUESSES_LIMIT - len(set(lettersGuessed) - set(SECRETWORD))


def handleGuesses(letter, lettersGuessed):
    if letter in lettersGuessed:
        print 'Oops! You have already guessed that letter:', getGuessedWord(lettersGuessed)

    elif letter in SECRETWORD:
        lettersGuessed.append(letter)
        print 'Good Guess: ', getGuessedWord(lettersGuessed)

    else:
        lettersGuessed.append(letter)
        print 'Oops! That letter is not in my word:', getGuessedWord(lettersGuessed)


def getAvailableLetters(lettersGuessed):
    allLetters = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'

    return allLetters.translate(None, ''.join(lettersGuessed))


def printInitialMessage():
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is', len(SECRETWORD), 'letters long.'
    print 'And this word has', len(set(SECRETWORD)), 'different letters.'
    print '--------------'


def hangman():
    lettersGuessed = []

    printInitialMessage()

    while not isWordGuessed(lettersGuessed) and getNumberOfGuesses(lettersGuessed) > 0:
        print 'You have ', getNumberOfGuesses(lettersGuessed), 'guesses left.'
        print 'Available letters', getAvailableLetters(lettersGuessed)

        letter = raw_input('Please guess a letter: ')

        handleGuesses(letter, lettersGuessed)
        print '------------'

    else:
        if isWordGuessed(lettersGuessed):
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was', SECRETWORD, '.'


if __name__ == '__main__':
    SECRETWORD = chooseWord(loadWords())
    hangman()
