#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @author: yewennuan
# @Mail: ywnjohu@gmail.com
# @date: 2019/1/7 11:25 AM

from flask import Flask
from flask_thriftclient import ThriftClient
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from thrift.transport import TSocket
from thrift.transport import TTransport

from example import format_data
from flask_thrift_demo.example.ttypes import Data

app = Flask(__name__)
app.config["THRIFTCLIENT_TRANSPORT"] = "tcp://localhost:9090"

__HOST = 'localhost'
__PORT = 9090


class FormatDataHandler(object):
    def do_format(self, data):
        return Data(data.text.upper())


handler = FormatDataHandler()

processor = format_data.Processor(handler)
transport = TSocket.TServerSocket(__HOST, __PORT)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

rpcServer = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print 1
rpcServer.serve()
print 2
thriftclient = ThriftClient(format_data.Client, app)


@app.route("/")
def home():
    data = Data("1Re")
    result = thriftclient.client.do_format(data)
    return result.text


if __name__ == '__main__':
    app.run()
