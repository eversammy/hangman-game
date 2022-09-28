WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r',)
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
    False otherwise
    """
    i = 0
    while i < len(secretWord):
        if secretWord[i] not in lettersGuessed:
            return False
        i += 1
    return True


def getGuessedWord(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    """
    if secretWord[0] in lettersGuessed:
        res = secretWord[0]
    else:
        res = '_ '
    if len(secretWord) == 1:
        return (res)
    else:
        return res + getGuessedWord(secretWord[1:], lettersGuessed)


def getAvailableLetters(lettersGuessed):
    """
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    """
    alpha = string.ascii_lowercase
    lettersLeft = [e for e in alpha if e not in lettersGuessed]
    return ''.join(lettersLeft)


def hangman(secretWord):
    """
    Starts up an interactive game of Hangman.
    """
    brkLine = '- - - - - - - - - - - - -'
    print('Welcome to Hangman game...')
    print('I am thinking of a word that is {} letters long'.format(len(secretWord)))
#   print(secretWord)
    print(brkLine)
    no_of_guesses = 0
    total_guess = 8
    lettersGuessed = []
    while getGuessedWord(secretWord, lettersGuessed) != secretWord:
        if no_of_guesses < total_guess:
            print('You have {} guesses left'.format(total_guess - no_of_guesses))
            print('Available letters: {}'.format(getAvailableLetters(lettersGuessed)))
            input_letter = input('Please guess a letter: ')
            if len(input_letter) != 1:
                print('Please enter one letter')
            elif input_letter in secretWord and input_letter not in lettersGuessed:
                lettersGuessed.append(input_letter)
                print('Good guess: {}'.format(getGuessedWord(secretWord, lettersGuessed)))
                print(brkLine)
            elif input_letter in lettersGuessed:
                print("Oops! You've already guessed that letter: {}".format(getGuessedWord(secretWord, lettersGuessed)))
                print(brkLine)
            elif input_letter not in secretWord:
                lettersGuessed.append(input_letter)
                print('Oops! That letter is not in my word: {}'.format(getGuessedWord(secretWord, lettersGuessed)))
                print(brkLine)
                no_of_guesses += 1
        else:
            return 'Sorry, you ran out of guesses. The word was {}.'.format(secretWord)
    else:
        return "Congratulations, you won!"


secretWord = chooseWord(wordlist)
print(hangman(secretWord))