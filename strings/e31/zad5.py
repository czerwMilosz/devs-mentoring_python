def get_input_from_user():
    user_input = input('Wprowadz tekst ')
    return user_input

def add_white_space(text, spaces = 5):
   text_with_whitespace = ' ' * spaces + text
   return text_with_whitespace

def format_text(whitespace_text, strip_text):
    return f'''Tekst z bialymi znakami: {whitespace_text}
Tekst po usunieciu bialych znakow: {strip_text}
'''

def main():
    user_input = get_input_from_user()
    whitespace_text = add_white_space(user_input)
    strip_text = whitespace_text.lstrip()
    print(format_text(whitespace_text, strip_text))

main()