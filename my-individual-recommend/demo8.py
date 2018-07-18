#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import time
from datetime import datetime, timedelta

from elasticsearch import Elasticsearch
from elasticsearch.connection import RequestsHttpConnection

AUTH_HEADERS = {
    'ELK-AUTH-TOKEN': 'a5455782c32d432bba5a2b6417336a5d'
}

ELASTICSEARCH_INDEX = 'a1_game_statistic-*'


# ELASTICSEARCH_INDEX = 'opsys_appdump-*'

class AuthToken(object):
    """
    TOKEN AUTH BASE CLASS
    """

    def __call__(self, r):
        r.headers.update(AUTH_HEADERS)
        return r


# 通过外网请求


# 通过内网请求
# es = Elasticsearch(host="api-in.elk.x.netease.com", port=9550, connection_class=RequestsHttpConnection, http_auth=AuthToken())


if __name__ == '__main__':
    # print 1
    # time.sleep(5)
    # print 11
    es = Elasticsearch(host="api.elk.x.netease.com", port=9550, http_auth=AuthToken(),
                       connection_class=RequestsHttpConnection)
    body = {"query": {"bool": {"must": [{"term": {"operation": "thread_life"}},
                                        {"range": {"@timestamp": {"gte": datetime.now()-timedelta(days=1)}}}]}},
            "size": 1000, "sort": [{"@timestamp": {"order": "asc"}}]}
    print "error,query body:{}".format(body)
    page = es.search(index=ELASTICSEARCH_INDEX, body=body)
    print("Got %d Hits:" % page['hits']['total'])
