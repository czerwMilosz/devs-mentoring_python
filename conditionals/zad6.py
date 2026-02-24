from random import randint

def get_user_move():
    game_options = {'orzel', 'reszka', 'stop'} #dozwolone ruchy w grze
    while True: # petla dziala dopoki nie zbierzemy 2 poprawnych ruchow
        # czyszcze input zeby uniknac problemow z wielkoscia liter i spacjami
        user_move = input(f'Wybierz orzel, reszka lub stop aby zakonczyc gre: ').strip().lower()

        # sprawdzam czy wpisany ruch jest poprawny, a nastepnie dodawany do listy
        if user_move in game_options:
            return user_move
        else:
            print('Wprowadziles zla wartosc')

def flip_coin():
    coin = randint(0, 1)
    if coin == 0:
        return 'orzel'
    else:
        return 'reszka'

def get_round_winner(user_move: str,coin: str):
    if user_move == coin:
        return 'player'
    else:
        return 'computer'

def get_number_of_rounds():
    # pytam dopoki nie dostane poprawnej liczby rund
    while True:
        try:
            num_of_rounds = int(input('Ile rund chcesz zagrac: '))
            if num_of_rounds <= 0:
                print('Podaj wartosc powyzej 0')
                continue
        except ValueError:
            print('Nieprawidlowa wartosc')
            continue
        return num_of_rounds

def countdown():
    for i in range(3,0,-1):
        print(i)

def update_score(winner: str, score: list):
    if winner == 'player':
        score[0] += 1
    else:
        score[1] += 1
    return score

def format_game_score(user_score: int, computer_score: int):
    return f'Gracz: {user_score} Komputer: {computer_score}'

def get_game_winner(user_score: int, computer_score: int):
    if user_score > computer_score:
        return 'Wygrales!'
    elif user_score < computer_score:
        return 'Komputer wygral!'
    else:
        return 'Remis!'

def play_game(rounds: int):
    score = [0,0]
    for i in range(rounds):
        user_move = get_user_move()
        if user_move == 'stop': #jezeli uzytkownik wybral stop, przerywa gre
            print('Gra przerwana')
            break
        countdown()
        coin = flip_coin()
        winner = get_round_winner(user_move, coin)
        score = update_score(winner,score)
        print(coin)
        print(format_game_score(score[0],score[1]))
    return f'\nKoniec gry!\n{get_game_winner(score[0], score[1])}\n{format_game_score(score[0],score[1])}'



def main():
    rounds = get_number_of_rounds()
    print(play_game(rounds))

main()