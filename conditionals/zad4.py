def get_user_moves():
    player_moves = []
    game_options = {'kamien', 'papier', 'nozyce'} #dozwolone ruchy w grze
    player_number = 1
    while len(player_moves) < 2: # petla dziala dopoki nie zbierzemy 2 poprawnych ruchow
        # czyszcze input zeby uniknac problemow z wielkoscia liter i spacjami
        user_input = input(f'Gracz {player_number}, wybierz kamien, papier lub nozyce: ').strip().lower()

        # sprawdzam czy wpisany ruch jest poprawny, a nastepnie dodawany do listy
        if user_input in  game_options:
            player_moves.append(user_input)
            player_number += 1
        else:
            print('Wprowadziles zla wartosc')
    return player_moves # zwracam ruchy obu graczy


def get_round_outcome(player_moves:list):
    player1_move, player2_move = player_moves[0], player_moves[1] # wyciagam ruchy z listy
    if player1_move == player2_move: # remis jesli ruchy sa takie same
        return 'draw'
    # przypadki kiedy wygrywa gracz 1
    elif player1_move == 'papier' and player2_move == 'kamien':
        return 'player1'
    elif player1_move == 'nozyce' and player2_move == 'papier':
        return 'player1'
    elif player1_move == 'kamien' and player2_move == 'nozyce':
        return 'player1'
    else:
        return 'player2' # w pozostalych przypadkach wygrywa gracz 2

def get_number_of_rounds():
    # pytam dopoki nie dostane poprawnej liczby rund
    while True:
        try:
            user_input = int(input('Ile rund chcesz zagrac: '))
            if user_input <= 0:
                print('Podaj wartosc powyzej 0')
                continue
        except ValueError:
            print('Nieprawidlowa wartosc')
            continue
        return user_input

# ta funkcja buduje string z wynikiem
def format_game_score(player1:int, player2:int, draw_count:int):
    return(f'Gracz 1: {player1}\nGracz 2: {player2}\nRemis: {draw_count}\n')

def play_game(round_count: int):
    player1_score = 0
    player2_score = 0
    draw_count = 0
    # petla wykona sie tyle razy ile rund wybral uzytkownik
    for i in range(1, round_count + 1):
        user_input = get_user_moves()
        round_outcome = get_round_outcome(user_input)
        print(f'\nRunda {i}')

    # na podstawie wyniku rundy aktualizuje punkty
        if round_outcome == 'draw':
            draw_count += 1
            print('Remis')
            print(format_game_score(player1_score, player2_score, draw_count))

        elif round_outcome == 'player1':
            player1_score += 1
            print('Punkt dla Gracz 1')
            print(format_game_score(player1_score, player2_score, draw_count))

        elif round_outcome == 'player2':
            player2_score += 1
            print('Punkt dla Gracz 2')
            print(format_game_score(player1_score, player2_score, draw_count))

    return [player1_score, player2_score, draw_count]

def get_game_winner(score:list):
    player1_score = score[0]
    player2_score = score[1]
    draw_score = score[2]

    # sprawdzam kto ma wiecej punktow
    if player1_score > player2_score:
        return f'Gracz 1 wygrywa!\nWynik:\n{format_game_score(player1_score, player2_score, draw_score)}'
    elif player2_score > player1_score:
        return f'Gracz 2 wygrywa!\nWynik:\n{format_game_score(player1_score, player2_score, draw_score)}'
    else:
        return f'Remis!\nWynik:\n{format_game_score(player1_score, player2_score, draw_score)}'

def main():
   round_count = get_number_of_rounds()
   game_score = play_game(round_count)
   print(get_game_winner(game_score))

main()

