with open("test.txt", "r", encoding='utf-8') as f:
    for i, line in enumerate(f, start=1):
        if i == 4:
            print(line.strip())