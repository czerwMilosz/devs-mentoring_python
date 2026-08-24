import string

# print(string.ascii_uppercase) !!!
def get_alphabet():
    alphabet = ""
    for letter in range(ord("a"), ord("z") + 1):
        alphabet += chr(letter)
    return alphabet

print(get_alphabet())
print(string.ascii_uppercase[::-1])
def get_reverse_alphabet():
    reverse_alphabet = ""
    for letter in range(ord("z"), ord("a") - 1, -1):
        reverse_alphabet += chr(letter)
    return reverse_alphabet

def get_reverse_alphabet_v2():
    return "".join([chr(letter) for letter in range(ord("a"), ord("z") + 1)][::-1])
    # for letter in range(ord("z"), ord("a") - 1, -1):
    #     reverse_alphabet += chr(letter)
    # return reverse_alphabet

print(get_reverse_alphabet_v2())