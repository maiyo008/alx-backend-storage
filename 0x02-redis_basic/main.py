#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('exercise').Cache
replay = __import__('exercise').replay

# Create an instance of the Cache class
cache = Cache()

# Call the store method multiple times
cache.store("foo")
cache.store("bar")
cache.store(42)

# Use the replay function to display the history of calls
replay(cache, cache.store)
