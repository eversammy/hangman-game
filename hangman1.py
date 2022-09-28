def hangman1():
    """
    A guessing game. User enters letters in attempt to guess a word
    Takes letters, return whether letter in list
    """
    word = ['_', '_', '_', '_', '_']
    puzzle = ['t', 'h', 't', 'h', 'm']
    cul_guess = []
    attempt = 6
    for i in range(attempt):
        if word != puzzle:
            guess = input('>>> ')
            cul_guess.append(guess)
            if guess in puzzle:
                if guess in word:
                    if puzzle.count(guess) == 1:
                        print(True, word)
                        pass
                    else:
                        k_index = puzzle.index(guess, (puzzle.index(guess)+1))
                        word[k_index] = puzzle[k_index]
                        print(True, word)
                else:
                    k_index = puzzle.index(guess)
                    word[k_index] = puzzle[k_index]
                    print(True, word)
            else:
                print(False, word)
        else:
            return f'''
Good-Job
Guessed Letters: {cul_guess}
Word: {word}'''
    else:
        if word == puzzle:
            return f'''
Good-Job
Guessed Letters: {cul_guess}
Word: {word}'''
        else:
            return f'''
You Failed
Guessed Letters: {cul_guess}
Word: {word}'''


w = hangman1()
print(w)
