DICTIONARY = {'The Sensual World' : 'Kate Bush',
              'Shaday' : 'Ofra Haza',
              'Achtung Baby' : 'U2',
              'Aion' : 'Dead Can Dance',
              'Invisible Touch' : 'Genesis'}

def print_keys(dictionary: dict):
    for key in dictionary.keys():
        print(key)

def get_valid_key(dictionary: dict):
    user_input = input("Enter a album name: ").strip()
    if user_input in dictionary.keys():
        print(f"Author of the album {user_input} is {dictionary[user_input]}")
    else:
        print("No data")

def main():
    print_keys(DICTIONARY)
    get_valid_key(DICTIONARY)

if __name__ == "__main__":
    main()