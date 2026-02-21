def get_input_from_user():
    user_input = input('Wprowadz tekst ')
    return user_input

def add_white_space(user_input = get_input_from_user()):
   text_with_whitespace = ' ' * 5 + user_input
   return text_with_whitespace

def strip_whitespace(whitespace_text = add_white_space()):
    return whitespace_text.lstrip()

def print_text(strip_text = strip_whitespace(), whitespace_text = add_white_space()):
    return f'''Tekst z bialymi znakami: {whitespace_text}
Tekst po usunieciu bialych znakow: {strip_text}
'''
print(print_text())