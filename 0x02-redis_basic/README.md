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
### Task 