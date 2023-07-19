# 0x02. Redis basic
----
![meme](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/1/40eab4627f1bea7dfe5e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230719%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230719T143712Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=426730ed0a9eadc60ebecebca76ba0d5e261c7f694df981c139421f185e80c22)

## Resources
**Read or watch:**

* [Redis commands](https://redis.io/commands/)
* [Redis python client](https://redis-py.readthedocs.io/en/stable/)
* [How to Use Redis With Python](https://realpython.com/python-redis/)
* [Redis Crash Course Tutorial](https://www.youtube.com/watch?v=Hbt56gFj998)

## Learning Objectives
* Learn how to use redis for basic operations
* Learn how to use redis as a simple cache

## Install Redis on Ubuntu 18.04
```
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```

## Tasks
### Task 0. Writing strings to Redis
<Details>
Create a Cache class. In the __init__ method, store an instance of the Redis client as a private variable named _redis (using redis.Redis()) and flush the instance using flushdb.

Create a store method that takes a data argument and returns a string. The method should generate a random key (e.g. using uuid), store the input data in Redis using the random key and return the key.

Type-annotate store correctly. Remember that data can be a str, bytes, int or float.

```
root@2c462bd13a86:~/alx-backend-storage/0x02-redis_basic# chmod u+x main.py
root@2c462bd13a86:~/alx-backend-storage/0x02-redis_basic# python3 main.py 
a6b2ff5f-3ffc-4cf0-877f-d12ddb6258e3
b'hello'
```
</Details>

### Task 1. Reading from Redis and recovering original type
<Details>
Redis only allows to store string, bytes and numbers (and lists thereof). Whatever you store as single elements, it will be returned as a byte string. Hence if you store "a" as a UTF-8 string, it will be returned as b"a" when retrieved from the server.

In this exercise we will create a get method that take a key string argument and an optional Callable argument named fn. This callable will be used to convert the data back to the desired format.

Remember to conserve the original Redis.get behavior if the key does not exist.

Also, implement 2 new methods: get_str and get_int that will automatically parametrize Cache.get with the correct conversion function.

The following code should not raise:

```
cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
```

Sample output
```
root@2c462bd13a86:~/alx-backend-storage/0x02-redis_basic# python3 test.py
root@2c462bd13a86:~/alx-backend-storage/0x02-redis_basic# 
```
</Details>

### Task 2. Incrementing values
<Details>
Familiarize yourself with the INCR command and its python equivalent.

In this task, we will implement a system to count how many times methods of the Cache class are called.

Above Cache define a count_calls decorator that takes a single method Callable argument and returns a Callable.

As a key, use the qualified name of method using the __qualname__ dunder method.

Create and return function that increments the count for that key every time the method is called and returns the value returned by the original method.

Remember that the first argument of the wrapped function will be self which is the instance itself, which lets you access the Redis instance.

Protip: when defining a decorator it is useful to use functool.wraps to conserve the original function’s name, docstring, etc. Make sure you use it as described [here.](https://docs.python.org/3.7/library/functools.html#functools.wraps)

Decorate Cache.store with count_calls.

Sample output
```
root@2c462bd13a86:~/alx-backend-storage/0x02-redis_basic# ./main.py
b'1'
b'3'
root@2c462bd13a86:~/alx-backend-storage/0x02-redis_basic# 
root@2c462bd13a86:~/alx-backend-storage/0x02-redis_basic# 
```
</Details>