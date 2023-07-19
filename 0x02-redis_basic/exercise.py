#!/usr/bin/env python3
"""
exercise.py
"""
import redis
import uuid
from functools import wraps
from typing import Union, Callable


def count_calls(method: Callable) -> Callable:
    """
    count_calls decorator
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
         Increments the count for that key every time the method is called
         """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Storing lists
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        name and append ":inputs" and ":outputs"
        to create input and output list keys, respectively.
        """
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        input_data = str(args)
        self._redis.rpush(input_key, input_data)
        output = method(self, *args, **kwargs)
        output_data = str(output)
        self._redis.rpush(output_key, output_data)
        return output
    return wrapper


def replay(cache, func: Callable):
    """
     display the history of calls of a particular function.
    """
    func_name = func.__qualname__
    input_key = f"{func_name}:inputs"
    output_key = f"{func_name}:outputs"
    inputs = cache._redis.lrange(input_key, 0, -1)
    outputs = cache._redis.lrange(output_key, 0, -1)
    num_calls = len(inputs)
    print(f"{func_name} was called {num_calls} times:")
    for input_data, output_data in zip(inputs, outputs):
        input_data_str = input_data.decode("utf-8")
        output_data_str = output_data.decode("utf-8")
        print(f"{func_name}{input_data_str} -> {output_data_str}")


class Cache:
    """
    Write strings to redis
    """
    def __init__(self):
        """
        Store an instance of the Redis client,
        and flush the client
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
         Generate a random key, store the input data
         in Redis using the random key and return the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self,
        key: str,
        fn: Callable = None
    ) -> Union[str, bytes, int, None]:
        """
        Reads from Redis, and recovers original format
        """
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """
        parametrize Cache.get with string
        """
        return self.get(key, fn=lambda d: decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """
        parametrize Cache.get with integer
        """
        return self.get(key, fn=int)
