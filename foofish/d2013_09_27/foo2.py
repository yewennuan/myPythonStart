#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @author: yewennuan
# @Mail: ywnjohu@gmail.com
# @date: 2018/10/8 上午10:51

# 单下划线开头的变量，Pyhthon规定为内部变量（私有变量），from M import * 时，这种变量并不会导入进来

from foo import *
if __name__ == '__main__':
    print locals()