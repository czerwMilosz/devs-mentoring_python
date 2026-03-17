import string

SENTENCE = "Hello, world! This is just a simple test. This is awesome simple test!"
sentence = SENTENCE.strip()

def remove_punctuation(sentence: str) -> str:
    for char in sentence:
        if char in string.punctuation:
            sentence = sentence.replace(char, "")
    return sentence


def str_to_tuple(sentence: str) -> tuple:
    tuple_sentence = tuple(sentence.strip().split())
    return tuple_sentence

t_sentence = str_to_tuple(remove_punctuation(sentence))
print(t_sentence)
print(f"Tuple length: {len(t_sentence)}")

print(f"First word: {t_sentence[0]}")
print(f"Fourth word: {t_sentence[3]}")

def tuple_to_set(tuple_sentence: tuple) -> set:
    set_sentence = set(tuple_sentence)
    return set_sentence

set_sentence = tuple_to_set(t_sentence)
print(set_sentence)
print(f"Set length: {len(set_sentence)}")
print(f"First word: {list(set_sentence)[0]}")
print(f"Fourth word: {list(set_sentence)[3]}")

def compare_set_elements(set_sentence: set):
    return list(set_sentence)[0] == list(set_sentence)[3]

print(compare_set_elements(set_sentence))