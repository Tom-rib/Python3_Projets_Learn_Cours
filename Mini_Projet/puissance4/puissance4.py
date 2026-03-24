def player_col_input(player):
    while True:
        col = input(f"Joueur{player},Ou veux tu jouer (1 et 7) ? ")
        if len(col) == 1 and col in "1234567":
            break
    print("Mauvaise entrée, recommencez")


    print("Colonne",col)
    return int(col)



def print_game(game):
    i = len(game)
    for line in game:
        #print(line)
        for col in line:
            if col is None:
                print(' . ', end='')
            elif col == 0:
                print(' X', end='')

            elif col == 1:
                print(' O ', end='')
            else:
                print(col, end='')
            i -= 1
        print('|')
    print("===========")
    print("  1  2  3  ")

    print('\n')



def update_game(game,player,col):
    for line in reversed(game):
        if line[col-1] is None:
            line[col-1] = player
            break

1


def puissance_4():
    player = 0
    game = [
        [None,None,None,None,None,None,None],
        [None, None,None,None,None,None,None],
        [None, None,None,None,None,None,None],
        [None, None,None,None,None,None,None],
        [None, None,None,None,None,None,None]
    ]


    while True:
        col = player_col_input(player+1)
        update_game(game,player,col)
        print_game(game)
        #if has_someone_won():
        #   break
        player = (player+1) % 2




if __name__ == "__main__":
    puissance_4()       