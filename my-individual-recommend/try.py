# coding=utf-8
import math
import time
from datetime import datetime, timedelta
from collections import defaultdict


def fun1():
    item_list = [1, 2, 3]
    for item in item_list:
        item = 2
    print item_list
    list_id = []
    list_id.append(1)
    list_id.append(2)
    name = "data" + datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + ".txt"
    file = open(name, 'w')
    file.write(str(list_id))
    file.close()


def fun2():
    return (datetime.now() - datetime(2018, 6, 1)).days


def cal_post_timeliness_score(post_publish_time):
    if not post_publish_time:
        return 0
    now = datetime.now()
    days = (now - post_publish_time).days
    a = 0.5
    timeliness_score = 1 / math.log(a * days + 10, 10)
    return timeliness_score


def post_quality_score_fun(x):
    ai = 15
    bi = 5
    ci = 0.02
    return ci / (1 + math.exp(-(x - ai) / bi))


def cal_post_quality_score(browse_count=0, comment_count=0, support_count=0):
    return post_quality_score_fun(browse_count) + post_quality_score_fun(comment_count) + post_quality_score_fun(
        support_count)


def add_list_try():
    score = 2
    user_tag_list = [("英雄", 10), ("人马", 8), ("非人学院", 6), ("联盟", 4), ("和平", 2), ("嘻嘻", 2)]
    add_tag_list = ["女警", "人马", "悟空", "天马"]

    add_tag(user_tag_list, add_tag_list)


def add_tag(user_tag_score_list, add_tag_list, score=2):
    for i, item in enumerate(user_tag_score_list):
        if item[0] in add_tag_list:
            user_tag_score_list[i] = (item[0], item[1] + score)
            add_tag_list.remove(item[0])

    add_tag_score_list = [(x, score) for x in add_tag_list]
    index = 0
    for i, item in enumerate(user_tag_score_list):
        index = i
        if item[1] <= score:
            break
    for item in add_tag_score_list:
        user_tag_score_list.insert(index, item)
    return user_tag_score_list


def time_test():
    now1 = datetime.now()
    now2 = datetime.now()
    now1_str = now1.strftime('%Y-%m-%d')
    now2_str = now2.strftime('%Y-%m-%d')
    now1_format = datetime.strptime(now1_str, '%Y-%m-%d')
    now2_format = datetime.strptime(now2_str, '%Y-%m-%d')
    print 1


def time_test2():
    now = datetime.now()
    print time.mktime(now.timetuple())


def time_test3():
    now = datetime.now()
    start_time = now - timedelta(days=30)
    for i in range(0, 30):
        start_time = start_time + timedelta(days=1)
    print start_time == now


def dict_test():
    a_dict = defaultdict(list)
    a_dict[1].append(1)

    print a_dict[1]


def dict_test1(new_dict):
    new_dict[1] = 2


def int_test(a):
    a = 2


def sort_test():
    positive_result_dict = {}
    positive_result_list = sorted(positive_result_dict.items(), key=lambda x: x[1], reverse=True)
    print positive_result_list


def str_test():
    str = "呵呵"
    list_test = ["呵呵"] + ["理发店分"] * 0
    k = 2
    print  str * k
    print list_test


def round_test():
    print(int(round(1.1)))
    print(int(round(1.5)))
    print(int(round(1.6)))


def list_test():
    list1 = range(1, 50000)
    list2 = range(5000, 8000)
    time1 = time.time()
    list1 = list(set(list1).difference(set(list2)))
    time2 = time.time()
    print time2 - time1
    print len(list1)


def fun_1():
    positive_result_dict = {"hehe": 1, "ccc": 3, "ddd": 2}
    positive_result_list = sorted(positive_result_dict.items(), key=lambda x: x[1], reverse=True)
    print positive_result_list


def chinese_word():
    s = "中文"
    print s


def sort_test1():
    list1 = [["呵呵", 2], ["GG", 6], ["ff", 4], ["ddd", 4]]
    list2 = sorted(list1, key=lambda a: a[1], reverse=True)
    print list2


def encoder():
    title1 = '西瓜'
    title1 = unicode(title1, 'utf-8')
    title2 = '\u897f\u74dc'
    title2 = title2.decode('unicode_escape')
    print title2 == title1


def comma_test():
    str = ' '
    str1 = '嘎嘎'
    str2 = '呵呵,叽叽'
    str3 = '呵呵，叽叽,bb'
    str3 = str3.replace("，", ",")
    print str.split()


def sleep_test():
    time.sleep(10)
    print 1


if __name__ == '__main__':
    sleep_test()
