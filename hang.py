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
    secretLetters = []

#    for letter in secretWord:
#        if letter in secretLetters:
#            secretLetters.append(letter)
#        else:
#            pass

    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            return False

    return True


def getGuessedWord():

    guessed = ''

    return guessed


def getAvailableLetters():
    import string
    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase

    return available


def hangman(secretWord):

    guesses = GUESSES
    lettersGuessed = []
    numberOfDifferentLetters = len(set(secretWord))

    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is', len(secretWord), 'letters long.'
    print 'And this word has', numberOfDifferentLetters, 'different letters.'
    print '--------------'

    while isWordGuessed(secretWord, lettersGuessed) == False and guesses > 0:
        print 'You have ', guesses, 'guesses left.'

        available = getAvailableLetters()
        for letter in available:
            if letter in lettersGuessed:
                available = available.replace(letter, '')

        print 'Available letters', available
        letter = raw_input('Please guess a letter: ')
        if letter in lettersGuessed:

            guessed = getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_'

            print 'Oops! You have already guessed that letter: ', guessed
        elif letter in secretWord:
            lettersGuessed.append(letter)

            guessed = getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_'

            print 'Good Guess: ', guessed
        else:
            guesses -= 1
            lettersGuessed.append(letter)

            guessed = getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_'

            print 'Oops! That letter is not in my word: ',  guessed
        print '------------'

    else:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was ', secretWord, '.'


secretWord = chooseWord(loadWords())
hangman(secretWord)
