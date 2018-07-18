# coding=utf-8
import synonyms

if __name__ == "__main__":
    # synonyms.display("美丽")
    # synonyms.display("美国")
    sen1 = "第五 第五"
    sen2 = ["第五", "人格", "第五人格", "勇者", "经营", "十分", "巨龙", "招募", "介绍", "设定"]
    sen3 = "第五 人格 勇者 经营 十分 巨龙 招募 介绍 设定"
    r = synonyms.compare(sen1,sen3,seg=False,ignore=False)
    print r
    # for x in sen2:
    #     r = synonyms.compare(sen1, x, seg=False)
    #     print r
    # print("人脸: %s" % (synonyms.nearby("人脸")))
    # print("识别: %s" % (synonyms.nearby("识别")))
    # print("NOT_EXIST: %s" % (synonyms.nearby("NOT_EXIST")))

    sen1_list = ['品位',
                 '词典',
                 '游戏',
                 '膝盖',
                 '一箭',
                 '游戏',
                 '测评',
                 '先锋',
                 '恶搞',
                 '患者',
                 '失败',
                 '存活',
                 '小淘气',
                 '成绩',
                 '游戏',
                 'ip',
                 '原作',
                 '情怀',
                 '肥宅',
                 'flag',
                 '立过',
                 '游戏',
                 '如风',
                 '单杀',
                 '第五人格',
                 '益智']
