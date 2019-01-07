#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @author: yewennuan
# @Mail: ywnjohu@gmail.com
# @date: 2019/1/4 10:36 AM
import pytest


def test_answer():
    print 'fadfadfa'
    assert 1 + 2 == 3


class TestSample:

    def test_answer(self, count):
        print('get count %s' % count)
        assert count == 10
