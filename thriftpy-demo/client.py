#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @author: yewennuan
# @Mail: ywnjohu@gmail.com
# @date: 2019/1/4 3:38 PM
import thriftpy
if __name__ == '__main__':
    pingpong_thrift = thriftpy.load("pingpong.thrift", module_name="pingpong_thrift")

    from thriftpy.rpc import make_client

    client = make_client(pingpong_thrift.PingPong, '127.0.0.1', 6000)
    print client.ping()


