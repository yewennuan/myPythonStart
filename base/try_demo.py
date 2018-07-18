import os
from __builtin__ import help

from base.sqlaichemy_demo import fun
print '2'
from base import sqlaichemy_demo


def fun1():
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    print(list(enumerate(seasons)))


def fun2():
    a = [1, 2, 3]
    a[len(a):] = [5, 6]
    a.pop()
    print '-' * 49


def fun3():
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    for q, a in zip(questions, answers):
        print 'What is your {0}?  It is {1}.'.format(q,a)

def fun4():
    for i in reversed(xrange(1,10,2)):
        print i

def fun5():
    for i in xrange(10,1,-2):
        print i


def fun6():
    knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    for i in enumerate(knights):
        print i

    for i in knights:
        print i

def fun7():
    print __name__

def fun8():
     print os.getcwd()
     print dir(os)
     print help(os)


if __name__ == '__main__':
    fun8()
