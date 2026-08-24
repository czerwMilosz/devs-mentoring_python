TEXT = "apple banana apple orange banana apple"

def most_common_word(text: str) -> str:
    words = text.split()
    counter = {}
    for word in words:
        counter[word] = counter.get(word, 0) + 1
    return max(counter, key=counter.get)

def main():
    most_common = most_common_word(TEXT)
    print(most_common)

if __name__ == "__main__":
    main()
