import time
from functools import wraps


def measure_time(func):
    '''
        Calculates the execution time of an synchronous function
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = round(end_time - start_time, 2)
        name = func.__qualname__
        print(name, ":", f'{execution_time}', "seconds")
        return result
    return wrapper


def measure_time_async(func):
    '''
        Calculates the execution time of an asynchronous function
    '''
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        end_time = time.time()
        execution_time = round(end_time - start_time, 2)
        name = func.__qualname__
        print(name, ":", f'{execution_time}', "seconds")
        return result
    return wrapper
