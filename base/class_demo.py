#!/usr/bin/env python3
# coding=utf-8
__author__ = 'johu'


class Base(object):
    __table = '1'

    @property
    def table(self):
        return self.__table

    @table.setter
    def table(self, table):
        self.__table = table


class Impl(Base):
    def __init__(self):
        self.table = 'gaga'


if __name__ == '__main__':
    impl = Impl()
    print(impl.table)
