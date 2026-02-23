from random import randint

def get_user_moves():
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

def get_winner(user_move: str,coin: str):
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

def score_counter(winner: str, score: list):
    if winner == 'player':
        score[0] += 1
    elif winner == 'computer':
        score[1] += 1
    return score


def play_game(rounds: int):
    score = [0,0]
    for i in range(rounds):
        user_move = get_user_moves()
        if user_move == 'stop': #tutaj przerobic to na funkcje
            print('Gra przerwana')
            return score
        coin = flip_coin()
        countdown()
        winner = get_winner(user_move, coin)
        score = score_counter(winner,score)
        print(coin)
        print(f'Gracz: {score[0]} Komputer: {score[1]}')
    return f'Koniec gry!\nGracz: {score[0]} Komputer: {score[1]}'

#dodac jeszcze funkcje z formatem wyswietlania wyniku

def main():
    rounds = get_number_of_rounds()
    print(play_game(rounds))

main()