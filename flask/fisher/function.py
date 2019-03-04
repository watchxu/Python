#! /usr/bin/python
# -*- coding:utf-8 -*-

def decorator(func):
    def inner(*args, **kwargs):
        print('执行函数之前')
        ret = func(*args, **kwargs)
        print('执行函数之后')
        return ret
    return inner

@decorator
def func(arg):
    print(arg)

func('hhh')