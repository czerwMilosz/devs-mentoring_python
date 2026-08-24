def while_countdown(start:int = 100, end:int = 50):
    while start >= end:
        print(start)
        start -= 1

# print(while_countdown())

def for_countdown(start:int = 100, end:int = 50):
    for num in range(start, end -1, -1):
        print(num)


print(for_countdown())