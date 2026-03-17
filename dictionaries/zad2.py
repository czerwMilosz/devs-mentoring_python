DICTIONARY = {'The Sensual World' : 'Kate Bush',
              'Shaday' : 'Ofra Haza',
              'Achtung Baby' : 'U2',
              'Aion' : 'Dead Can Dance',
              'Invisible Touch' : 'Genesis'}

def print_keys(dictionary: dict):
    for key in dictionary.keys():
        print(key)

def get_lower_dict_keys(dictionary: dict):
    return {key.lower(): key for key in dictionary}

def get_album_name(dictionary: dict):
    user_input = input("Enter an album name: ").strip()
    lower_dict = get_lower_dict_keys(dictionary)

    if user_input.lower() in lower_dict:
        original_key = lower_dict[user_input.lower()]
        print(f"Artist of the album {original_key} is {dictionary[original_key]}")
    else:
        print("No data")

def add_album_and_artist(dictionary: dict):
    album_name = input("Enter album name: ").strip().title()
    artist = input("Enter artist name: ").strip().title()
    lower_dict = get_lower_dict_keys(dictionary)

    if album_name.lower() not in lower_dict:
        dictionary[album_name] = artist
        print(f"Album {album_name} by {artist} added to the dictionary")
    else:
        print("Album already exists")

def remove_album(dictionary: dict):
    album_name = input("Enter album name: ").strip().title()
    lower_dict = get_lower_dict_keys(dictionary)
    if album_name.lower() in lower_dict:
        del dictionary[album_name]
        print(f"Album {album_name} removed")
    else:
        print(f"Album {album_name} does not exist in dictionary")

def print_menu():
    print("\n1. Show albums"
          "\n2. Search for an album"
          "\n3. Add an album"
          "\n4. Remove an album"
          "\n5. Exit")

def main():
    while True:
        print_menu()
        user_choice = input("\nEnter a choice: ").strip()
        if user_choice == "1":
            print_keys(DICTIONARY)
        elif user_choice == "2":
            get_album_name(DICTIONARY)
        elif user_choice == "3":
            add_album_and_artist(DICTIONARY)
        elif user_choice == "4":
            remove_album(DICTIONARY)
        elif user_choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()