colors = 'red,blue,orange,black,white'

def split_text(text: str):
    split_text = text.split(',')
    return f'''Podzielony tekst: {split_text}
Trzeci wprowadzony kolor: {split_text[2]}'''

print(split_text(colors))