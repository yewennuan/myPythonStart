#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @author: yewennuan
# @Mail: ywnjohu@gmail.com
# @date: 2018/10/8 上午10:51

# 但是如果你非要把这些变量导入进来也是可以的，使用import时，明确导入具体的变量时就行了

from foo import *
from foo import _bar
from foo import __bar
if __name__ == '__main__':
    print locals()