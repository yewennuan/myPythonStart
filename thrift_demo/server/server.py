#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @author: yewennuan
# @Mail: ywnjohu@gmail.com
# @date: 2019/1/3 3:24 PM

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from thrift_demo.example import ttypes, format_data

__HOST = 'localhost'
__PORT = 8080

class FormatDataHandler(object):
    def do_format(self, data):
        return ttypes.Data(data.text.upper())


if __name__ == '__main__':
    handler = FormatDataHandler()

    processor = format_data.Processor(handler)
    transport = TSocket.TServerSocket(__HOST, __PORT)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    rpcServer = TServer.TSimpleServer(processor,transport, tfactory, pfactory)

    print('Starting the rpc server at', __HOST,':', __PORT)
    rpcServer.serve()