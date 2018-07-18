# coding=utf-8
import re

import jieba

str = ("【安利】《死战骑士团》创新十足的休闲游戏"
       "<p>《死战骑士团》是由国内独立游戏制作团队“The Rock Studio ”制作的一款休闲策略类游戏。"
       "创新的塔防类战斗、明亮卡通的画风、完善的养成系统、再加上各种独创的趣味玩法，让这款游戏充满了休闲舒适的氛围。"
       "</p> <p> <!--IMG0--></p> <hr> <p>先说这游戏的战斗系统，与传统的塔防游戏类似却又不同。"
       "横版的画面下，玩家控制固定位置的一个角色，面对不断靠近的敌人进行指哪打哪的操作，期间有技能可供使用。"
       "游戏整体以关卡递进的形式逐渐增加难度，是不是听起来略有无聊呢，不过独特的画风、音效、特效下，有种莫名的爽快感。"
       "不过这款游戏毕竟是以休闲作为卖点，让我们静下心来一起看看具体休闲在哪方面"
       "</p> <p> <!--IMG1--></p> <hr> <p>先说主界面，分别有:</p> <p><br> </p><p>进入战斗: 选择关卡，没关有三种难度可供选择，"
       "每通过一个难度将解锁一个宝箱</p> <p><br></p> <p>商店:&nbsp;欧非鉴定中心，也就是抽卡</p> <p><br></p> <p>"
       "娱乐场: 赌博，类似简化了的老虎机</p> <p><br></p> <p>博物馆: 融合了放置类的玩法，当角色进入关卡，"
       "每次遇到新的怪物都会成为图鉴收藏到博物馆，并持续生产金币</p> <p><br></p> <p>英雄属性:是游戏最重要系统之一，"
       "玩家可在这里进行属性加点、技能加点、天赋加点，以及升级装备，不过游戏内的装备系统仅仅只是固定装备的多段升级。"
       "</p> <p>游戏内一共可解锁五种不同职业的角色。"
       "</p> <p> <!--IMG3--><br></p> <p> <!--IMG2--><br></p> <p><br></p> <p>训练场:这也算是游戏的一个亮点，"
       "玩家在这里可以选择五种属性进行训练，每种训练对应一种小游戏，五个小游戏各有不同，角色属性提升的重要场所"
       "</p> <p> <!--IMG4--> <!--IMG5--></p> <hr> <p>我发现这款游戏的标签里有策略和塔防，但我觉得这并不是这款游戏的主旋律，"
       "仅仅只是一种陪衬而已。本质还是一款养成休闲类游戏，它具备了养成类游戏的主要元素，并加以简化，同时依然具备养成类游戏独有的满足感。"
       "它不是一款需要肝的游戏，而是平时静静地躺在手机的角落里，并在无聊的时候打开游戏玩两关，去老虎机碰碰运气，在训练场玩玩小游戏，"
       "商城抽抽卡，偶尔去博物馆收集金币，看着角色一点一滴成长起来，还是别有一番风味的</p> <hr> <p>  <!--USER0-->&nbsp;"
       "<br> </p><p><br></p>")


def filter_html_chars(str):
    """去除字符串里的html元素和一些特殊字符"""
    str = str.strip().replace('\n', '').replace(' ', '').replace('\t', '').replace('\r', '').replace('&nbsp;', '')
    str = re.sub(r'<.+?>', "", str)
    print str


def get_stop_word_list(path='stop_word.txt'):
    """去掉停用词，和一些自己指定的词，针对全局"""
    stopwords = [line.strip() for line in open(path, 'r').readlines()]
    return stopwords


def get_custom_stop_word_list(addition_stop_word_list=None):
    """添加自定义的停用词"""
    stop_word_list = get_stop_word_list()
    if addition_stop_word_list:
        stop_word_list.extend(addition_stop_word_list)
    return stop_word_list


def add_custom_words(word_list=None):
    """添加自身不想被分词的词语"""
    if word_list:
        for word in word_list:
            jieba.add_word(word)


def filter_stop_word(seg_list, stop_word_list):
    """输入jieba分词后的结果，和停用词，输出空格隔开的字符串"""
    seg_list_after = []
    # 去停用词
    for seg in seg_list:
        if seg not in stop_word_list:
            seg_list_after.append(seg)
    return ' '.join(seg_list_after)





def main_process():
    # TODO:从配置表读取自定义的词
    word_list = None
    add_custom_words(word_list)
    # TODO:从配置表读取自定义的词
    custom_stop_word_list = None
    stop_word_list = get_custom_stop_word_list(custom_stop_word_list)



if __name__ == '__main__':
    print(stop_word_list())
