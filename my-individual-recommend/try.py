# coding=utf-8
import itertools
import math
import time
import uuid
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


def datetime_test():
    print 'cal_post_tag start' + datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def itertools_groupby_test():
    for key, group in itertools.groupby('AAABBBCCAAA'):
        print key, list(group)  # 为什么这里要用list()函数呢？


def mydecorator(function):
    def _mydecorator(*args, **kwargs):
        print 1
        res = function(*args, **kwargs)
        print 2
        return res

    return _mydecorator


@mydecorator
def decorator_test(i, k):
    print i, k


def mydecorator1(arg1, arg2):
    def _mydecorator(function):
        def __mydecorator(*args, **kwargs):
            print arg1
            tmp = (arg1, arg2)
            res = function(*tmp, **kwargs)
            print arg2
            return res

        return __mydecorator

    return _mydecorator


@mydecorator1("arg1", "arg2")
def decorator_test1(i, k):
    print i, k


class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print ('class decorator runing')
        self._func()
        print ('class decorator ending')


@Foo
def class_decorator_test():
    print ('bar')


def none_test():
    if None == "divide":
        print 1
    else:
        print 2


def ypw_test1():
    now = int(time.time())
    tmp_apk_name = "youpinwei_%s_%s.apk" % ("channel", now)
    print tmp_apk_name


def exception_test():
    raise Exception("hehe")


def list_limit_test():
    temp = [1, 2, 3, 4, 5, 6]
    print temp[0:5]


def integer_divide():
    print float(1) / 3


def string_blank_test():
    str = ''
    if str:
        print 1
    else:
        print 2


def dict_pop_test():
    a = {"a1": "des"}
    print a
    a.pop("a2")
    print a


def func_debug_test(param1, param2, param3):
    return param1 * param2 * param3


class MagicA(object):
    a = 10


class Fjs(object):
    def __init__(self, name):
        self.name = name

    def hello(self):
        print "said by : ", self.name

    def fjs(self, name):
        if name == self.name:
            print "yes"
        else:
            print "no"


class Wrap_Fjs(object):
    def __init__(self, fjs):
        self._fjs = fjs

    def __getattr__(self, item):
        if item == "hello":
            print "调用hello方法了"
        elif item == "fjs":
            print "调用fjs方法了"
        return getattr(self._fjs, item)


class MyClass():
    def __init__(self):
        self.__superprivate = "Hello"
        self._semiprivate = ", world!"

    def test(self):
        print self._semiprivate
        print self.__superprivate


def class_test():
    class MyClass1():
        def __init__(self):
            self.__superprivate = "Hello"
            self._semiprivate = ", world!"

        def test(self):
            print self._semiprivate
            print self.__superprivate

    test = MyClass1()
    test.test()


def local_proxy_test1():
    from werkzeug.local import LocalStack
    user_stack = LocalStack()
    user_stack.push({'name': 'Bob'})
    user_stack.push({'name': 'John'})

    def get_user():
        # do something to get User object and return it
        return user_stack.pop()

    # 直接调用函数获取user对象
    user = get_user()
    print user['name']
    print user['name']


def local_proxy_test2():
    from werkzeug.local import LocalStack, LocalProxy
    user_stack = LocalStack()
    user_stack.push({'name': 'Bob'})
    user_stack.push({'name': 'John'})

    def get_user():
        # do something to get User object and return it
        return user_stack.pop()

    # 通过LocalProxy使用user对象
    user = LocalProxy(get_user)
    print user['name']
    print user['name']


def time_func():
    date = datetime.strptime('2018-07-01', '%Y-%m-%d')
    print date


def map_tests():
    list = [{"title": "fsdsdf"}, {"title": "sfd"}]
    print [x.get("title", "") for x in list]


def test_kwargs():
    def fun_sss(id, **kwargs):
        print id
        print kwargs.get("abc", "default")

    fun_sss(8)


def uuid_test():
    str1 = str(uuid.uuid4())
    str1 = str1.replace("-", "")
    str1 = str1[0:8]
    print str1


def kwargs_test():
    def fun(id=0, ab="1", **kwargs):
        print id, ab, kwargs['sx']

    tmp_dict = {"sx": "sx", "bx": "bx"}
    fun(2, 'strs', **tmp_dict)


def time_test1():
    cur_time = time.time()
    inta = cur_time - cur_time % 86400
    date1 = datetime.fromtimestamp(inta)
    print date1


def time_test11():
    now = datetime.now()
    now_ts = int(time.mktime(now.timetuple()))
    now_ts = now_ts - now_ts % 86400
    wee_hour = datetime.utcfromtimestamp(now_ts)
    print wee_hour


def time_test222():
    now = datetime.now()
    print now
    now_ts = int(time.mktime(now.timetuple()))
    print now_ts
    print datetime.fromtimestamp(now_ts)
    print datetime.utcfromtimestamp(now_ts)


def test_1232():
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = 25
    print now
    print datetime(year, month, day, 3)


if __name__ == '__main__':
    test_1232()
