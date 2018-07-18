# coding=utf-8
import os
import re

import jieba
import jieba.analyse
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer


def titlelist():
    for file in os.listdir('.'):
        if '.' not in file:
            for f in os.listdir(file):
                yield (file + '--' + f.split('.')[0])  # windows下编码问题添加：.decode('gbk', 'ignore').encode('utf-8'))


def wordslist():
    jieba.add_word(u'林晚荣')
    # stop_word = [unicode(line.rstrip()) for line in open('chinese_stopword.txt')]
    stop_word = [u"，", u"。"]
    print len(stop_word)
    for file in os.listdir('.'):
        if '.' not in file:
            for f in os.listdir(file):
                if 'jp' in f:
                    continue
                with open(file + '//' + f) as t:
                    content = t.read().strip().replace('\n', '').replace(' ', '').replace('\t', '').replace('\r', '')
                    content = re.sub(r'<.+?>', "", content)
                    content = re.sub(r'&nbsp',"",content)
                    seg_list = jieba.cut(content)
                    seg_list_after = []
                    # 去停用词
                    for seg in seg_list:
                        if seg not in stop_word:
                            seg_list_after.append(seg)
                    result = ' '.join(seg_list_after)
                    # wordslist.append(result)
                    yield result


if __name__ == "__main__":



    wordslist = list(wordslist())

    titlelist = list(titlelist())

    vectorizer = CountVectorizer()
    transformer = TfidfTransformer()
    X = vectorizer.fit_transform(wordslist)
    tfidf = transformer.fit_transform(X)

    words = vectorizer.get_feature_names()  # 所有文本的关键字
    weight = tfidf.toarray()

    n = 20  # 前五位
    for (title, w) in zip(titlelist, weight):
        print u'{}:'.format(title)
        # 排序
        loc = np.argsort(-w)
        for i in range(n):
            print u'-{}: {} {}'.format(str(i + 1), words[loc[i]], w[loc[i]])
        print '\n'
