#!/usr/bin/env python3
# coding=utf-8
__author__ = 'johu'

from functools import wraps


def singleton(cls):
    instances = {}

    @wraps(cls)
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return getinstance


@singleton
class MyClass(object):
    a = ''

    def __init__(self, a):
        self.a = a


if __name__ == '__main__':
    one = MyClass(1)
    two = MyClass(2)
    print(one == two)
    print(one is two)

    print(id(one), id(two))
    print(one.a)
    print(two.a)
