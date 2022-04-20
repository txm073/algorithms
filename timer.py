from time import perf_counter

def timed(fn):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        value = fn(*args, **kwargs)
        return value, perf_counter() - start
    return wrapper