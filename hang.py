import random
import string

WORDLIST_FILENAME = "palavras.txt"
GUESSES = 8


def loadWords():
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)

    print "  ", len(wordlist), "words loaded."

    return wordlist


def chooseWord(wordList):
    secretWord = random.choice(wordList)
    while len(secretWord) > GUESSES:
        wordList.remove(secretWord)
        secretWord = random.choice(wordList)

    return secretWord


def isWordGuessed(lettersGuessed):
    return True if SECRETWORD == getGuessedWord(lettersGuessed) else False


def getGuessedWord(lettersGuessed):
    guessed = ''
    for letter in SECRETWORD:
        guessed += letter if letter in lettersGuessed else '_'

    return guessed


def handleGuesses(letter, lettersGuessed):
    if letter in lettersGuessed:
        print 'Oops! You have already guessed that letter:', getGuessedWord(
            lettersGuessed)

    elif letter in SECRETWORD:
        lettersGuessed.append(letter)
        print 'Good Guess: ', getGuessedWord(lettersGuessed)

    else:
        lettersGuessed.append(letter)
        print 'Oops! That letter is not in my word:', getGuessedWord(
            lettersGuessed)


def getAvailableLetters():
    # 'abcdefghijklmnopqrstuvwxyz'
    return string.ascii_lowercase


def hangman():
    print SECRETWORD

    guesses = GUESSES
    lettersGuessed = []

    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is', len(SECRETWORD), 'letters long.'
    print 'And this word has', len(set(SECRETWORD)), 'different letters.'
    print '--------------'

    while isWordGuessed(lettersGuessed) == False and guesses > 0:
        print 'You have ', GUESSES, 'guesses left.'

        # put it all in a single method (getAvailableLetters)
        available = getAvailableLetters()
        for letter in available:
            if letter in lettersGuessed:
                available = available.replace(letter, '')
        print 'Available letters', available

        letter = raw_input('Please guess a letter: ')

        # put it all in a single method (handleGuesses)
        handleGuesses(letter, lettersGuessed)
        print '------------'

    else:
        if isWordGuessed(lettersGuessed) == True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was', SECRETWORD, '.'


SECRETWORD = chooseWord(loadWords())
hangman()
