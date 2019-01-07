#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @author: yewennuan
# @Mail: ywnjohu@gmail.com
# @date: 2019/1/4 2:31 PM

import pytest


@pytest.fixture(scope="session")
def count():
    print 'init count'
    return 10
