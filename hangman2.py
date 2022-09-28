def hangman2():    # Returns string
    """
    A guessing game. User enters letters in attempt to guess a word
    Takes letters, return whether letter in sentence string
    """
    word = '_____'

    def s_l(string_):
        list_ = []
        for item in string_:
            list_.append(item)
        return list_

    def l_s(list_):
        string_ = ''
        for item in list_:
            string_ += item
        return string_
    conv_word = s_l(word)
    puzzle = 'theme'
    conv_puzzle = s_l(puzzle)
    cul_guess = []
    attempt = 6
    for i in range(attempt):
        found = l_s(conv_word)
        if found != puzzle:
            guess = input('>>> ')
            cul_guess.append(guess)
            if guess in conv_puzzle:
                if guess in conv_word:
                    if conv_puzzle.count(guess) == 1:
                        found = l_s(conv_word)
                        print(True, found)
                        pass
                    else:
                        k_index = conv_puzzle.index(guess, (conv_puzzle.index(guess)+1))
                        conv_word[k_index] = conv_puzzle[k_index]
                        found = l_s(conv_word)
                        print(True, found)
                else:
                    k_index = conv_puzzle.index(guess)
                    conv_word[k_index] = conv_puzzle[k_index]
                    found = l_s(conv_word)
                    print(True, found)
            else:
                found = l_s(conv_word)
                print(False, found)
        else:
            return f'''
Good-Job
Guessed Letters: {cul_guess}
Word: {found}'''
    else:
        found = l_s(conv_word)
        if found == puzzle:
            return f'''
Good-Job
Guessed Letters: {cul_guess}
Word: {found}'''
        else:
            return f'''
You Failed
Guessed Letters: {cul_guess}
Word: {found}'''


w = hangman2()
print(w)
