#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @author: yewennuan
# @Mail: ywnjohu@gmail.com
# @date: 2019/1/4 3:37 PM

import thriftpy
if __name__ == '__main__':

    pingpong_thrift = thriftpy.load("pingpong.thrift", module_name="pingpong_thrift")

    from thriftpy.rpc import make_server

    class Dispatcher(object):
        def ping(self):
            return "pong"

    server = make_server(pingpong_thrift.PingPong, Dispatcher(), '127.0.0.1', 6000)
    server.serve()