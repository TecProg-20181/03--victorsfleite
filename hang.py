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


def isWordGuessed(secretWord, lettersGuessed):
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False

    return True


def getGuessedWord(secretWord, lettersGuessed):
    guessed = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed += letter
        else:
            guessed += '_'

    return guessed


def getAvailableLetters():
    # 'abcdefghijklmnopqrstuvwxyz'
    return string.ascii_lowercase


def hangman(secretWord):

    guesses = GUESSES
    lettersGuessed = []

    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is', len(secretWord), 'letters long.'
    print 'And this word has', len(set(secretWord)), 'different letters.'
    print '--------------'

    while isWordGuessed(secretWord, lettersGuessed) == False and guesses > 0:
        print 'You have ', guesses, 'guesses left.'

        # put it all in a single method (getAvailableLetters)
        available = getAvailableLetters()
        for letter in available:
            if letter in lettersGuessed:
                available = available.replace(letter, '')
        print 'Available letters', available

        letter = raw_input('Please guess a letter: ')

        # put it all in a single method (getGuessedWord)
        if letter in lettersGuessed:
            print 'Oops! You have already guessed that letter: ', getGuessedWord(
                secretWord, lettersGuessed)

        elif letter in secretWord:
            lettersGuessed.append(letter)

            print 'Good Guess: ', getGuessedWord(secretWord, lettersGuessed)

        else:
            guesses -= 1
            lettersGuessed.append(letter)

            print 'Oops! That letter is not in my word: ',  getGuessedWord(
                secretWord, lettersGuessed)

        print '------------'

    else:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was', secretWord, '.'


secretWord = chooseWord(loadWords())
hangman(secretWord)
