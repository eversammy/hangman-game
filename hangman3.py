def hangman3():     # Returns string, removed string-list functions, increased input length
    """
    A guessing game. User inputs letters (string or space)in attempt to guess a word
    Takes letters, return whether letter in sentence string
    """
    puzzle = 'justice system'
    word = round(len(puzzle) * 1.5) * '_'
    print(f'''Welcome to Hangman Game, What word am i thinking?\nGuess: {word} [clue: word is a legal term]''')
    word_list = list(word)
    cul_guess = []
    attempt = 15
    for i in range(attempt):
        if puzzle != ''.join(word_list).replace('_', ''):
            position = []
            guess = input('>>> ')
            if len(guess) != 1:
                print('provide one(1) letter per guess')
            else:
                cul_guess.append(guess)
                if guess in puzzle:
                    if puzzle.count(guess) > 1:
                        for j in range(len(puzzle)):
                            if puzzle[j] == guess:
                                position.append(j)
                        for k in position:
                            word_list[k] = guess
                        print('True:', ''.join(word_list))
                    else:
                        word_list[puzzle.index(guess)] = guess
                        print('True:', ''.join(word_list))
                else:
                    print('False:', ''.join(word_list))
        else:
            return f'''Good-Job
Guessed Letters: {cul_guess}
Word: {''.join(word_list).replace('_', '')}'''
    else:
        if puzzle == ''.join(word_list):
            return f'''Good-Job
Guessed Letters: {cul_guess}
Word: {''.join(word_list).replace('_', '')}'''
        else:
            return f'''You Failed
Guessed Letters: {cul_guess}
Word: {puzzle}'''


w = hangman3()
print(w)
