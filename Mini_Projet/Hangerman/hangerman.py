def input_word():
    word = input("Enter un mot a deviner: ")
    return word.upper().strip()


def print_result(word, guesses):
    for c in word:
        if c in guesses:
            print(c, end=' ')
        else:
            print("_", end=' ')
    print()


def hangman():
    word = input_word()
    tries = 6
    guesses = ""
    errors = 0

    while errors < tries:
        print(f"\nErreurs: {errors}/{tries}")
        print_result(word, guesses)
        
        l = input("Saisir une lettre: ").upper()
        
        if l in guesses:
            print("Tu as deja propose cette lettre")
            continue
        
        guesses += l
        
        if l in word:
            print(f" {l} est dans le mot")
        else:
            print(f" {l} n'est pas dans le mot")
            errors += 1
        
        if all(c in guesses for c in word):
            print(f"\nBravo! Le mot est: {word}")
            break
    
    if errors == tries:
        print(f"\nGame Over! Le mot etait: {word}")


hangman()