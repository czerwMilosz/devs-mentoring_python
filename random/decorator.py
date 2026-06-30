import time
import tracemalloc

def timer(func):
    def wrapper(*args, **kwargs):
        print("Start function", func.__name__)
        time_start = time.perf_counter()
        tracemalloc.start()
        try:
            res = func(*args, **kwargs)
            return res
        finally:
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            time_end = time.perf_counter()
            print(f"Czas wykonania: {time_end - time_start}")
            print(f"Zuzycie pamieci (aktualne): {current / 1024:.2f} kB")
            print(f"Maksymalne zuzycie pamieci: {peak / 1024:.2f} kB")
    return wrapper

@timer
def calc(a, b):
    t = "asdasdasdas"
    l = ["0"] * 100_000_000
    print("hello")
    return a + b

def sample_dec(x):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(x):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@sample_dec(x=5)
def wave(a,b):
    print(f"{a + b}")

print(wave(3,4))




print(calc(1, 2))
