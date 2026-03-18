from pydantic import BaseModel, Field
from random import randint

class UserRange(BaseModel):
    start_range: int = Field(gt=0, description="Start of the range")
    end_range: int = Field(gt=0, description="End of the range")

def get_user_range() -> UserRange:
    while True:
        try:
            start_range = int(input("Start range: "))
            end_range = int(input("End range: "))
            if start_range > end_range:
                start_range, end_range = end_range, start_range
            return UserRange(start_range=start_range, end_range=end_range)
        except ValueError as e:
            print(e)

def get_user_number() -> int:
    while True:
        try:
            number = int(input("Guess integer number: "))
            return number
        except ValueError:
            print("Please enter an integer")

def get_random_number_from_range(user_range: UserRange) -> int:
    return randint(user_range.start_range, user_range.end_range)

def get_hint(rand_num: int, user_num: int) -> str:
    if rand_num < user_num:
        return "Number is too big"
    elif rand_num > user_num:
        return "Number is too small"
    else:
        return "You guessed the number!"


def play_game(user_range: UserRange, rand_num: int) -> int:
    user_score = user_range.end_range - user_range.start_range
    while True:
        if user_score == 0:
            print("Game over, you lose!")
            return user_score
        user_num = get_user_number()

        # if user_num == rand_num:
        #     return user_score
        # user_score -= 1

        # return user_score if user_num == rand_num else user_score - 1

        if user_num != rand_num:
            print(get_hint(rand_num, user_num))
            user_score -= 1
        else:
            print(get_hint(rand_num, user_num))
            return user_score

def main():
    user_range = get_user_range()
    rand_num = get_random_number_from_range(user_range)
    game = play_game(user_range, rand_num)
    print(f"Your score: {game}")

if __name__ == "__main__":
    main()
