# coding=utf-8
import os
import uniout
import jieba

if __name__=="__main__":

    seg_list = jieba.cut("工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作", cut_all=True)
    result = ' '.join(seg_list)
    print "原句：工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作"
    print u"分词后: "+result
    wordslist = []
    titlelist = []
    # 遍历文件夹
    's'.rstrip()
    jieba.add_word(u'林晚荣')
    jieba.add_word(u'肖青xuanzhuan')

    for file in os.listdir('.'):
        if '.' not in file:
            # 遍历文档
            for f in os.listdir(file):
                # 标题
                # windows下编码问题添加：.decode('gbk', 'ignore').encode('utf-8'))
                titlelist.append(file + '--' + f.split('.')[0])
                # 读取文档
                with open(file + '//' + f, 'r') as f:
                    content = f.read().strip().replace('\n', '').replace(' ', '').replace('\t', '').replace('\r', '')
                # 分词
                seg_list = jieba.cut(content, cut_all=True)
                result = ' '.join(seg_list)
                wordslist.append(result)
            print wordslist

