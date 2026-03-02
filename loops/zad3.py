def for_countdown(start:int = 0, end:int = 100, step:int = 5):
    for i in range(start, end + 1, step):
        print(i)


print(for_countdown())