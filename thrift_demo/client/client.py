#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @author: yewennuan
# @Mail: ywnjohu@gmail.com
# @date: 2019/1/3 3:26 PM

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from thrift_demo.example.format_data import Client, Data

__HOST = 'localhost'
__PORT = 8080

if __name__ == '__main__':
    tsocket = TSocket.TSocket(__HOST, __PORT)
    transport = TTransport.TBufferedTransport(tsocket)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = Client(protocol)

    data = Data('hello,world!')
    transport.open()

    print(client.do_format(data).text)
