import decimal
import string

# -- 测试类型的三种方法，推荐第三种
from decimal import Decimal
from fractions import Fraction

seq = 1
print('-----------%s-----------' % seq)
L = [1, 2]
if type(L) == type([]):
    print("L is list")
if type(L) == list:
    print("L is list")
if isinstance(L, list):
    print("L is list")

# -- 数字常量
'''
    1234, -1234, 0, 999999999                    # 整数
    1.23, 1., 3.14e-10, 4E210, 4.0e+210          # 浮点数
    0o177, 0x9ff, 0X9FF, 0b101010                # 八进制、十六进制、二进制数字
    3+4j, 3.0+4.0j, 3J                           # 复数常量，也可以用complex(real, image)来创建
    hex(I), oct(I), bin(I)                       # 将十进制数转化为十六进制、八进制、二进制表示的“字符串”
    int(string, base)                            # 将字符串转化为整数，base为进制数
    2.x中，有两种整数类型：一般整数（32位）和长整数（无穷精度）。可以用l或L结尾，迫使一般整数成为长整数
    float('inf'), float('-inf'), float('nan')    # 无穷大, 无穷小, 非数
'''

seq = 2
print('-----------%s-----------' % seq)
demo2int = 10
demo2hex = hex(demo2int)
demo2oct = oct(demo2int)
demo2bin = bin(demo2int)
print(demo2hex)
print(demo2oct)
print(demo2bin)
if isinstance(demo2int, int):
    print('demo2int is int type')
if isinstance(demo2hex, str):
    print('demo2hex is int string')

print(int(demo2hex, 16))
print(float('inf'))

# -- 数字的表达式操作符
'''
    yield x                                      # 生成器函数发送协议
    lambda args: expression                      # 生成匿名函数
    x if y else z                                # 三元选择表达式
    x and y, x or y, not x                       # 逻辑与、逻辑或、逻辑非        1 and 2 是 2
    x in y, x not in y                           # 成员对象测试
    x is y, x is not y                           # 对象实体测试（根据id判断） 此处所说的对象应该特指复合类型的对象(如类、list等)，对于字符串、整数等类型，变量的id是随值的改变而改变的
    x<y, x<=y, x>y, x>=y, x==y, x!=y             # 大小比较，集合子集或超集值相等性操作符
    1 < a < 3                                    # Python中允许连续比较
    x|y, x&y, x^y                                # 位或、位与、位异或            1 & 2 是 01 & 10 = 0
    x<<y, x>>y                                   # 位操作：x左移、右移y位
    +, -, *, /, //, %, **                        # 真除法、floor除法：返回不大于真除法结果的整数值、取余、幂运算
    -x, +x, ~x                                   # 一元减法、识别、按位求补（取反）
    x[i], x[i:j:k]                               # 索引、分片、调用
    int(3.14), float(3)                          # 强制类型转换
'''

seq = 3
print('-----------%s-----------' % seq)


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)


for n in odd():
    pass

f = lambda x: x * x
print(f(5))

demo3int = 1

demo3list = demo3list1 = [1, 2, 3]
demo3list2 = [1, 2, 3]

demo3str = demo3str1 = 'johu'
demo3str2 = 'johu'

if demo3int > 3:
    print('>3')
else:
    print('<=3')

print(1 and 0)
print(1 or 0)
print(not 0)
print(demo3list is demo3list1)
print(demo3list is demo3list2)
print(id(demo3list))
print(id(demo3list1))
print(id(demo3list2))
print(demo3str is demo3str1)
print(demo3str is demo3str2)
print(id(demo3str))
print(id(demo3str1))
print(id(demo3str2))

demo3int1 = 2
if 1 < demo3int1 < 3:
    print('1<demo3int1<3')

print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

demo3listtmp = [1, 2, 3, 4, 5, 6]
print(demo3listtmp[1:2:3])
print(demo3listtmp[::3])

demo3int2 = 1
demo3int3 = 1024
print(demo3int2.bit_length())
print(demo3int3.bit_length())

# -- 数字相关的模块
'''
 # math模块
    # Decimal模块：小数模块
        import decimal
        from decimal import Decimal
        Decimal("0.01") + Decimal("0.02")        # 返回Decimal("0.03")
        decimal.getcontext().prec = 4            # 设置全局精度为4 即小数点后边4位
    # Fraction模块：分数模块
        from fractions import Fraction
        x = Fraction(4, 6)                       # 分数类型 4/6
        x = Fraction("0.25")                     # 分数类型 1/4 接收字符串类型的参数
'''
seq = 4
print('-----------%s-----------' % seq)
decimal.getcontext().prec = 4
print(Decimal('0.01') + Decimal("0.02"))

print(Fraction(4, 6))
print(Fraction("0.25"))

# demo
"""
   set是一个无序不重复元素集, 基本功能包括关系测试和消除重复元素。
   set支持union(联合), intersection(交), difference(差)和symmetric difference(对称差集)等数学运算。
   set支持x in set, len(set), for x in set。
   set不记录元素位置或者插入点, 因此不支持indexing, slicing, 或其它类序列的操作
"""
seq = 5
print('-----------%s-----------' % seq)
s = {3, 5, 9, 10}  # 创建一个数值集合，返回{3, 5, 9, 10}
t = set("Hello")  # 创建一个唯一字符的集合返回{}
print(t | s)
print(t.union(s))  # t 和 s的并集
print(t & s)
print(t.intersection(s))  # t 和 s的交集
print(t.difference(s))  # 求差集（项在t中, 但不在s中）
print(t ^ s)
t.symmetric_difference(s)  # 对称差集（项在t或s中, 但不会同时出现在二者中）
t.add('x')
t.remove('H')  # 增加/删除一个item
s.update([10, 37, 42])  # 利用[......]更新s集合
print(s)

# -- 集合frozenset，不可变对象
'''
     set是可变对象，即不存在hash值，不能作为字典的键值。同样的还有list等(tuple是可以作为字典key的)
    frozenset是不可变对象，即存在hash值，可作为字典的键值
    frozenset对象没有add、remove等方法，但有union/intersection/difference等方法
'''

seq = 6
print('-----------%s-----------' % seq)
a = {1, 2, 3}
b = set()
# b.add(a)  # error: set是不可哈希类型
b.add(frozenset(a))  # ok，将set变为frozenset，可哈希

seq = 7
print('-----------%s-----------' % seq)
# -- 布尔类型bool
print(type(True))  # 返回<class 'bool'>
print(isinstance(False, int))  # bool类型属于整型，所以返回True
print(True == 1)
print(True is 1)  # 输出(True, False)

s7 = 'johu'
print(s7 * 3)
print('a {1} {0} parrot'.format('kind', 'red'))
print(',.'.join(['a', 'b', 'c']))

s71 = 'stringobject'

print(s71.ljust(1))
print(list(map(ord, 'spam')))

# 类似于java System.out.println(2>3?1:2)
print(1 if 2 > 3 else 2)

# else语句会在循环结束后执行，除非在循环中执行了break，同样的还有for语句
a = 0
while a < 5:
    print("dd")
    a = a + 1
    break
else:
    print("else")

for teama, teamb in zip(["Packers", "49ers"], ["Ravens", "Patriots"]):
    print(teama + " vs. " + teamb)

for index, team in enumerate(["Packers", "49ers", "Ravens", "Patriots"]):
    print(index, team)  # 输出0, Packers \n 1, 49ers \n ......

for (a, b) in [(1, 2), (3, 4)]:  # 最简单的赋值
    print(a, b)
for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]:  # 自动解包赋值
    print(a, b, c)
for ((a, b), c) in [((1, 2), 3), ("XY", 6)]:  # 自动解包 a = X, b = Y, c = 6
    print(a, b, c)
for (a, *b) in [(1, 2, 3), (4, 5, 6)]:
    print(a, b)

M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

G = (sum(row) for row in M)  # 使用小括号可以创建所需结果的生成器generator object
next(G), next(G), next(G)  # 输出(6, 15, 24)
G = {sum(row) for row in M}  # G = {6, 15, 24} 解析语法还可以生成集合和字典
G = {i: sum(M[i]) for i in range(3)}  # G = {0: 6, 1: 15, 2: 24}


def func():
    """
    function document
    """
    print()


class Employee(object):
    """
    class document
    """
    print()


print(func.__doc__)  # 输出函数文档字符串
print(Employee.__doc__)  # 输出类的文档字符串

# -- 命名惯例:
"""
以单一下划线开头的变量名(_X)不会被from module import*等语句导入
前后有两个下划线的变量名(__X__)是系统定义的变量名，对解释器有特殊意义
以两个下划线开头但不以下划线结尾的变量名(__X)是类的本地(私有)变量
"""

# -- 获取列表的子表的方法:
x = [1, 2, 3, 4, 5, 6]
print(x[:3])  # 前3个[1,2,3]
print(x[1:5])  # 中间4个[2,3,4,5]
print(x[-3:])  # 最后3个[4,5,6]
print(x[::2])  # 奇数项[1,3,5]
print(x[1::2])  # 偶数项[2,4,6]

# -- 手动迭代：iter和next
L = [1, 2]
I = iter(L)  # I为L的迭代器
next(I)  # 返回1
next(I)  # 返回2
#I.next()  # Error:StopIteration

# -- Python中的可迭代对象
"""
1.range迭代器
2.map、zip和filter迭代器
3.字典视图迭代器：D.keys()), D.items()等
4.文件类型
"""


def maker(N):
    def action(X):
        return X ** N

    return action


f = maker(2)  # pass 2 to N
f(3)  # 9, pass 3 to X

start = 100


def tester(start):
    def nested(label):
        nonlocal start  # 指定start为tester函数内的local变量 而不是global变量start
        print(label, start)
        start += 3

    return nested


f1 = tester(start)
#函数属性
tester.xxx = 2
print(f1(2))


#-- 类的伪私有属性:使用__attr
class C1(object):
    def __init__(self, name):
        self.__name = name          # 此时类的__name属性为伪私有属性 原理 它会自动变成self._C1__name = name
    def __str__(self):
        return 'self.name = %s' % self.__name
I = C1('tom')
print(I)                            # 返回 self.name = tom
I.__name = 'jeey'                   # 这里无法访问 __name为伪私有属性
I._C1__name = 'jeey'                # 这里可以修改成功 self.name = jeey
print(I._C1__name)
print(I.__name)
