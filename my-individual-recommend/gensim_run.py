# coding=utf-8
from gensim import corpora, models, similarities
from gensim.models import tfidfmodel


class MyCorpus(object):
    def __iter__(self):
        for line in open('/Users/johu/Desktop/mycorpus.txt'):
            # 假设一行一个文档，文档通过空格来分别单词
            yield dictionary.doc2bow(line.lower().split())


if __name__ == "__main__":

    documents = ["Human machine interface for lab abc computer applications",
                 "A survey of user opinion of computer system response time",
                 "The EPS user interface management system",
                 "System and human system engineering testing of EPS",
                 "Relation of user perceived response time to error measurement",
                 "The generation of random binary unordered trees",
                 "The intersection graph of paths in trees",
                 "Graph minors IV Widths of trees and well quasi ordering",
                 "Graph minors A survey"]
    # 去除字符中得空格等
    stoplist = set('for a of the and to in'.split())
    texts = [[word for word in document.lower().split() if word not in stoplist]
             for document in documents]

    # 将只出现一次的单词移除
    from collections import defaultdict

    frequency = defaultdict(int)
    for text in texts:
        for token in text:
            frequency[token] += 1

    texts = [[token for token in text if frequency[token] > 1]
             for text in texts]

    from pprint import pprint  # 更好的输出格式

    pprint("---texts")
    pprint(texts)

    # ------ 将字段映射成id
    dictionary = corpora.Dictionary(texts)
    dictionary.save('/tmp/deerwester.dict')  # 保存以备之后使用
    print("---dictionary")
    print(dictionary)
    print("---dictionary.token2id")
    print(dictionary.token2id)

    new_doc = "Human computer interaction"
    new_vec = dictionary.doc2bow(new_doc.lower().split())
    print("---new_vec")
    print(new_vec)  # 单词"interaction"并没有在词袋中，我们将它舍弃

    corpus = [dictionary.doc2bow(text) for text in texts]
    corpora.MmCorpus.serialize('/tmp/deerwester.mm', corpus)  # store to disk, for later use
    print("---corpus")
    print(corpus)

    corpus_memory_friendly = MyCorpus()  # doesn't load the corpus into memory!
    print("---corpus_memory_friendly")
    print(corpus_memory_friendly)

    print("---print(vector)")
    for vector in corpus_memory_friendly:  # load one vector into memory at a time
        print(vector)

    # 获取token的统计信息
    dictionary = corpora.Dictionary(line.lower().split() for line in open('/Users/johu/Desktop/mycorpus.txt'))
    # 去掉停止字符和那些只出现一次的单词
    stop_ids = [dictionary.token2id[stopword] for stopword in stoplist
                if stopword in dictionary.token2id]
    once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq == 1]
    dictionary.filter_tokens(stop_ids + once_ids)  # 移除停止词和出现一次的词
    dictionary.compactify()  # 在移除无用的词后消除id序列的间隔
    print("---dictionary")
    print(dictionary)

    # 创建一个有两个文档的示例语料库
    corpus = [[(1, 0.5)], []]  # 是其中一个文档为空，来看看它的魔力
    corpora.MmCorpus.serialize('/tmp/corpus.mm', corpus)
    corpora.SvmLightCorpus.serialize('/tmp/corpus.svmlight', corpus)
    corpora.BleiCorpus.serialize('/tmp/corpus.lda-c', corpus)
    corpora.LowCorpus.serialize('/tmp/corpus.low', corpus)
    corpus = corpora.MmCorpus('/tmp/corpus.mm')
    print("---corpus")
    print(corpus)

    print("---list(corpus)")
    print(list(corpus))
    print("for doc in corpus:")
    for doc in corpus:
        print(doc)
    corpora.BleiCorpus.serialize('/tmp/corpus.lda-c', corpus)

    dictionary = corpora.Dictionary.load('/tmp/deerwester.dict')
    corpus = corpora.MmCorpus('/tmp/deerwester.mm')
    print("---corpus")
    print(corpus)
    tfidf = models.TfidfModel(corpus)  # 步骤1，初始化一个模型
    doc_bow = [(0, 1), (1, 1)]
    print("---tfidf[doc_bow]")  # 步骤2，使用模型来转换向量
    print(tfidf[doc_bow])  # 步骤2，使用模型来转换向量
    corpus_tfidf = tfidf[corpus]
    print("for doc in corpus_tfidf:")
    for doc in corpus_tfidf:
        print(doc)
    lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=2)  # 初始化一个LSI变换
    corpus_lsi = lsi[corpus_tfidf]  # 在原来的语料库上创建两个包装，bow->tfidf->fold-in-lsi
    lsi.print_topics(2)
    print("---for doc in corpus_lsi")
    for doc in corpus_lsi:  # bow->tfidf和tfidf->lsi变换都会在这里快速执行
        print(doc)

    lsi.save('/tmp/model.lsi')  # same for tfidf, lda, ...
    lsi = models.LsiModel.load('/tmp/model.lsi')

    dictionary = corpora.Dictionary.load('/tmp/deerwester.dict')
    corpus = corpora.MmCorpus('/tmp/deerwester.mm')

    print("---corpus")
    print(corpus)
    lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=2)
    doc = "Human computer interaction"
    vec_bow = dictionary.doc2bow(doc.lower().split())
    vec_lsi = lsi[vec_bow]  # convert the query to LSI space
    print("---vec_lsi")
    print(vec_lsi)
    index = similarities.MatrixSimilarity(lsi[corpus])  # 转换语料库到LSI空间并索引它
    index.save('/tmp/deerwester.index')
    index = similarities.MatrixSimilarity.load('/tmp/deerwester.index')
    sims = index[vec_lsi]  # perform a similarity query against the corpus

    print("list(enumerate(sims))")  # print (document_number, document_similarity) 2-tuples
    print(list(enumerate(sims)))  # print (document_number, document_similarity) 2-tuples
    sims = sorted(enumerate(sims), key=lambda item: -item[1])
    print("---sims")
    print(sims)







