#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @author: yewennuan
# @Mail: ywnjohu@gmail.com
# @date: 2018/10/8 下午2:38

# 双下划线开头的变量：它在模块中还是当作单下划线看待，但出现在类中作为类属性就不一样了，在运行时该类属性会被“混淆"，不能直接访问，需要在该变量前加上下划线和类名才能访问。

class Foo(object):
    boo = 40
    _boo = 50
    __boo = 60  # _Foo__boo
    def __init__(self):
        self.__booo = 70

    def __test(self):   #_Foo__test
        print "__test"

if __name__ == '__main__':
    print Foo.boo
    print Foo._boo
    print Foo._Foo__boo
    foo = Foo()
    print foo._Foo__booo
    foo._Foo__test()