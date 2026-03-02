def get_mean(numbers = 10): # 10 pierwszych liczb naturalnych 0,1,2,3,..,9
    total = 0
    for i in range(numbers):
        total += i
    return total/numbers

print(get_mean())