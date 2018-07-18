# coding=utf-8
import json
from datetime import datetime, timedelta

from elasticsearch import Elasticsearch

if __name__ == '__main__':

    n = 10
    size = 10000
    flag = False
    now = datetime.now()
    if not flag:
        start_time = now - timedelta(days=1)
    else:
        start_time = now - timedelta(days=30)
    time_list = []
    while True:
        delta_time = start_time + timedelta(days=1)
        if delta_time > now:
            break
        time_list.append([start_time.strftime('%Y-%m-%d'), delta_time.strftime('%Y-%m-%d')])
        start_time = delta_time

    es = Elasticsearch()

    # 投币 thread_life
    for time_seg in time_list:
        begin_time = time_seg[0]
        end_time = time_seg[1]
        body = {"query": {"bool": {"must": [{"term": {"operation": "thread_life"}},
                                            {"range": {"@timestamp": {"gte": begin_time, "lt": end_time}}}]}},
                "size": size}
        res = es.search(index="ypw_test", body=body)
        total = res['hits']['total']
        for hit in res['hits']['hits']:
            source = hit["_source"]
            data = json.loads(source["json_data"])
            uid = data.get("account_id", 0)
            pid = data.get("thread_id", 0)

    # 帖子评论 comment_publish
    for time_seg in time_list:
        begin_time = time_seg[0]
        end_time = time_seg[1]
        body = {"query": {"bool": {"must": [{"term": {"operation": "comment_publish"}},
                                            {"range": {"@timestamp": {"gte": begin_time, "lt": end_time}}}]}},
                "size": size}
        res = es.search(index="ypw_test", body=body)
        total = res['hits']['total']
        for hit in res['hits']['hits']:
            source = hit["_source"]
            data = json.loads(source["json_data"])


    # 帖子举报 report
    for time_seg in time_list:
        begin_time = time_seg[0]
        end_time = time_seg[1]
        body = {"query": {"bool": {"must": [{"term": {"operation": "report"}},
                                            {"range": {"@timestamp": {"gte": begin_time, "lt": end_time}}}]}},
                "size": size}
        res = es.search(index="ypw_test", body=body)
        total = res['hits']['total']
        for hit in res['hits']['hits']:
            source = hit["_source"]
            data = json.loads(source["json_data"])
