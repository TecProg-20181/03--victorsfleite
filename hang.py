import random
import string
import sys
import logging

WORDLIST_FILENAME = 'palavras.txt'
MAX_GUESSES = 8


class Game():
    letters = {}
    words = {}
    remainingGuesses = MAX_GUESSES

    def __init__(self):
        self.letters = Letters()
        self.words = Words()

        self.printInitialMessage()

        while self.canContinuePlaying():
            self.play()
        else:
            self.finish()

    def printInitialMessage(self):
        print 'Welcome to the game, Hangman!'
        print 'I am thinking of a word that is', len(self.words.getSecretWord()), 'letters long.'
        print 'And this word has', len(set(self.words.getSecretWord())), 'different letters.'
        print '--------------'

    def canContinuePlaying(self):
        isWordGuessed = self.words.isWordGuessed(self.letters.getLettersGuessed())
        return not isWordGuessed and self.remainingGuesses > 0

    def play(self):
        print 'You have ', self.remainingGuesses, 'guesses left.'
        print 'Available letters', self.letters.getAvailableLetters()

        self.letters.handleGuesses(self.words)

        self.remainingGuesses = self.letters.getRemainingGuesses(self.words.getSecretWord())

    def finish(self):
        if self.words.isWordGuessed(self.letters.getLettersGuessed()):
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was', self.words.getSecretWord(), '.'


class Words():
    SECRET_WORD = ''
    wordlist = []

    def __init__(self):
        """
        Depending on the size of the word list, this function may
        take a while to finish.
        """
        try:
            inFile = open(WORDLIST_FILENAME, 'r', 0)
        except IOError:
            print 'Impossible to open the file!'
            print 'The file', WORDLIST_FILENAME, 'doesn\'t exist!'
            sys.exit(0)

        print 'Loading word list from file...'

        line = inFile.readline()

        if not line:
            print 'Impossible to read from file!'
            print 'The file', WORDLIST_FILENAME, 'doesn\'t have any words!'
            sys.exit(0)

        self.wordlist = string.split(line)

        print '  ', len(self.wordlist), 'words loaded.'

        self.SECRET_WORD = self.chooseWord()

        if not self.SECRET_WORD:
            print 'No word chosen!'
            sys.exit(0)

    def chooseWord(self):
        words = self.wordlist

        secretWord = random.choice(words)
        while len(set(secretWord)) > MAX_GUESSES:
            words.remove(secretWord)
            secretWord = random.choice(words)

        return secretWord  # validate

    def getSecretWord(self):
        return self.SECRET_WORD

    def isWordGuessed(self, lettersGuessed):
        # validate param
        return True if self.getSecretWord() == self.getGuessedWord(lettersGuessed) else False  # validate method return

    def getGuessedWord(self, lettersGuessed):
        # validate param
        guessed = ''
        for letter in self.getSecretWord():
            guessed += letter if letter in lettersGuessed else ' _ '

        return guessed


class Letters():
    lettersGuessed = []

    def getLettersGuessed(self):
        return self.lettersGuessed

    def getInputLetter(self):
        return raw_input('Please guess a letter: ')

    def getAvailableLetters(self):
        allLetters = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'

        return allLetters.translate(None, ''.join(self.lettersGuessed))

    def handleGuesses(self, words):
        # validate params
        # validate method return on callings
        letter = self.getInputLetter()
        assert letter == None, 'error jeremias'

        if letter in self.lettersGuessed:
            print 'Oops! You have already guessed that letter:', words.getGuessedWord(self.lettersGuessed)

        elif letter in words.getSecretWord():
            self.lettersGuessed.append(letter)
            print 'Good Guess: ', words.getGuessedWord(self.lettersGuessed)

        else:
            self.lettersGuessed.append(letter)
            print 'Oops! That letter is not in my word:', words.getGuessedWord(self.lettersGuessed)

        print '------------'

    def getRemainingGuesses(self, secretWord):
        # validate param
        if not self.lettersGuessed:
            return MAX_GUESSES

        return MAX_GUESSES - len(set(self.lettersGuessed) - set(secretWord))  # validate method return


if __name__ == '__main__':
    Game()
