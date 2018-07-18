# coding=utf-8
import os
import sys

from gensim.models import Word2Vec
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

if __name__ == '__main__':
    line_sent = []

    sentences = [
        u"大卫 李髌骨 韧带 撕裂 等待 MRI 篮球 5月 21日 NBA 记者 MichaelC.Wright RamonaShelburne 联合 报道 消息 人士 透露 马刺 大卫 诊断 膝盖 韧带 撕裂 当地 "
         u"时间 周日 接受 核磁共振 检查 确认 伤势 马刺 今天 主场 勇士 系列赛 比分 落后 李本场 比赛 进攻 落地 不幸 膝盖 提前 退出 比赛 今年 季后赛 李场 出战 4.1分 篮板 来源 "
         u"Twitter",u"尤文 双冠 剑指 欧冠 决赛 皇马 北京 时间 5月 21日 尤文图斯 主场 血虐克 罗托 提前 夺得 意甲 冠军 史无前例 蝉联 意甲 5月 18日 意大利杯 实现 杯赛 三连冠 目前 "
                      u"尤文 赛季 展现 强大 实力 目标 13年 拜仁 赛季 剑指 尤文 上一场 联赛 比赛 罗马 尤文 意大利杯 决赛 前景 担忧 斑马军团 完美 打消 拥趸 疑虑 顺利 夺得 赛季 冠军 "
                      u"头衔 尤文 处于 皮亚尼奇 赫迪拉 中场 主力 无法 出场 情况 完成 卫冕 赛季 尤文 想起 拜仁慕尼黑 当时 拥有 强大 罗贝里 组合 穆勒 拉姆 施魏 施泰格 进攻 防守 两端 强硬 "
                      u"会师 欧冠 决赛 罗本 一锤定音 拜仁 球迷 夜晚 流下 热泪 布冯 能够 年龄 耳朵杯 职业 生涯 集齐 世界杯", u"花式 吐饼 看看 尼日利亚 老乡 北京 时间 5月 21日 中超 "
                                                                                     u"继续 展开 较量 长春 亚泰 坐镇 经开 体育场 迎来 天津 "
                                                                                     u"泰达 挑战 。本场 比赛 陷入 保级 泥潭 试图 上半场 主场 "
                                                                                     u"作战 亚泰 发难 胡斯蒂 主罚 前场 任意球 亚泰 中卫 孙捷 "
                                                                                     u"力压 防守 球员 头槌 破门 主队 纪录 下半场 惠家康 精彩 "
                                                                                     u"边路 突破 助攻 德耶 闪电 扳平 比分 双方 起跑线 比赛 "
                                                                                     u"双方 制造 破门 机会 亚泰 获得 点球 良机 皮球 直接 送入 "
                                                                                     u"对方 门将 怀中 未能 破门 战罢 双方 握手言和 相比 平和 "
                                                                                     u"比分 双方 外援 浪费 进球 机会 唏嘘不已 亚泰 队长"]

    # sentences=['person 中国','呵呵 go 3333333']
    for s in sentences:
        line_sent.append(s.split())  # 句子组成list

    model = Word2Vec(line_sent,
                     size=300,
                     window=5,
                     min_count=1,
                     workers=4)
    model.save('./word2vec.model')
    # for i in model.vocab.keys():  # vocab是dict
    #     print type(i)
    #     print i
    model = Word2Vec.load('word2vec.model')
    # print model.wv['球员']
    # tmp= model.most_similar(['3333333'])
    print model.n_similarity([u'大卫',u'接受'],[u'大卫',u'北京'])

