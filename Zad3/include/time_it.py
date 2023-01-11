from functools import wraps
import time

def time_it(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        total = end - start
        print(f"Function: {func.__name__}, took {total:.4f} seconds")
        return result

    return timeit_wrapper
