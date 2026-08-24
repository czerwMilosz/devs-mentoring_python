from collections import Counter

TEXT = "apple banana apple orange banana apple"

def most_common_word(text: str) -> str:
    return Counter(text.split()).most_common(1)[0][0]

def most_common_word_v2(text: str) -> str:
    word_counter = {}
    for word in text.split():
        word_counter[word] = word_counter.get(word, 0) + 1
    print(word_counter)
    return max(word_counter, key=word_counter.get)

def most_common_word_v3(text: str) -> str:
    word_counter = {}
    for word in text.split():
        word_counter[word] = word_counter.get(word, 0) + 1
    return max(word_counter, key=lambda x:word_counter[x])

def main():
    print(most_common_word(TEXT))
    print(most_common_word_v2(TEXT))
    print(most_common_word_v3(TEXT))

if __name__ == '__main__':
    main()