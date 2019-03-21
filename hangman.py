# Hangman game

def hangman(word):
    wrong = 0
    stages = ["",
              "__________            ",
              "|                           ",
              "|                 |         ",
              "|                 0        ",
              "|               / | \       ",
              "|              /     \      ",
              "|                           "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("You Lose! It was {}.".format(word))


hangman("cat")
