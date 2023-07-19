#!/usr/bin/env python3
"""
exercise.py
"""
import redis
import uuid
from typing import Union


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
