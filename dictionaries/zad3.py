import string

SENTENCE = ("Once upon a midnight dreary, while I pondered, weak and weary, "
            "Over many a quaint and curious volume of forgotten lore, "
            "While I nodded, nearly napping, suddenly there came a tapping, "
            "As of someone gently rapping, rapping at my chamber door. "
            "This visitor, I muttered, tapping at my chamber door - Only this, and nothing more.")

def remove_punctuation(sentence: str):
    clean_sentence = "".join([char.lower() for char in sentence if char not in string.punctuation])
    return clean_sentence


def count_words(sentence: str):
    split_sentence = sentence.split()
    words_count = {}
    for word in split_sentence:
        if word not in words_count:
            words_count[word] = 1
        else:
            words_count[word] += 1
    return words_count

def main():
    clean_sentence = remove_punctuation(SENTENCE)
    words_count = count_words(clean_sentence)
    for key, value in words_count.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
