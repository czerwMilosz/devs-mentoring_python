def get_user_word():
    while True:
        try:
            word = input("Enter a word: ")
            if word == "" or not word.isalpha():
                raise ValueError
            return word

        except ValueError:
            print("Invalid input")

def check_if_palindrome(word):
    word = word.lower()
    return word == word[::-1]

def main():
    word = get_user_word()
    if check_if_palindrome(word):
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is not a palindrome")

if __name__ == "__main__":
    main()