#!/usr/bin/env python3
"""
exercise.py
"""
import redis
import uuid
from typing import Union, Callable


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
