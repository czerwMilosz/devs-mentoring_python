def task_a(n = 10):
    return "*" * n

# print(task_a())

def task_b(n = 4):
    for i in range(1, n + 1):
        print("*" * i)

# print(task_b())

def task_c(n = 3):
    for i in range(n):
        print("*" * n)

# print(task_c())

def task_d(height = 5):
    width = 2 * height - 1 # tworzenie podstawy drzewka i maksymalnej liczby znakow w rzedzie
    for i in range(height):
        stars_count = 2 * i + 1 # zawsze powstaje nieparzysta liczba gwiazdek
        print(("*" * stars_count).center(width)) # w przypadku gdy height = 5 width = 9
# przy i = 0 stars_count = 1, czyli bedzie 1 gwiazdka i 8 pustych znakow (4 po kazdej ze stron gwiazdki)
# przy i = 1 stars_count = 3, czyli 3 gwiazdki i 6 pustych znakow (3 po kazdej ze stron gwiazdki) itd..
# dzieki temu gwiazdki zawsze beda na srodku

print(task_d())