#!/usr/bin/env python    # -*- coding: utf-8 -*
'''

此程序测试笛子的获得期望

问题背景: 
n个玩家刷副本有几率获得独占道具
获得道具的人陪打
测试玩家获得道具的期望局数

author: Jiebang
date: 20200907 
'''
import math
import random 
import numpy as np

num_play = 7 # 刷狗人数
players = np.zeros(num_play)
probability = 0.1 # 获得笛子的概率
times = []
extra_play = 1 # 额外陪打

def get_fife(players):
    # roll点 获得道具 道具具有独占属性
    # 输入people 为此时的获得与陪打情况
    if random.random() > probability :
        return None # 没有出笛子
    else:
        index = random.randint(1,num_play) # 选择获得笛子的人
        while(np.where(np.where(players <= 0)[0] == index)[0].size > 0):
            '道具独占'
            index = random.randint(1,num_play) - 1
        return index


'有陪打 + 不定掉落率'
for i in range(2000000):
    players = np.array([j + 1 for j in players]) # 次数 + 1
    index = get_fife(players)
    if index != None : 
        index -= 1
        if index == 0:
            times.append(players[0]) 
            players = [0,0,0,0,0,0,0,0] # roll到啦，我爬了
        else:
            players[index] = -extra_play

print(np.mean(times))

# 在8人 0.1概率获得道具 陪打3局的期望局数为 80.7717689822294
# 在8人 0.1概率获得道具 陪打2局的期望局数为 80.33665394657562
# 在8人 0.1概率获得道具 陪打1局的期望局数为 81.08944210184885
# 在7人 0.1概率获得道具 陪打3局的期望局数为 69.42923103627842
# 在7人 0.1概率获得道具 陪打2局的期望局数为 70.78436924819482
# 在7人 0.1概率获得道具 陪打1局的期望局数为 70.12897569870603
