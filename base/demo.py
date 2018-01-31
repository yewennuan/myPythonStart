def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        print(kw['city'])
    if 'job' in kw:
        # 有job参数
        print(kw['job'])
    print('name:', name, 'age:', age, 'other:', kw)


person(name='gaga', age='jji', city='fa', job='gaga')

print(' and %s %s %s ' % ('1', '2', '3'))