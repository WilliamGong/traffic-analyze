import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import basic_func

# solve Chinese font
plt.rcParams['font.sans-serif'] = ['KaiTi']
plt.rcParams['font.serif'] = ['KaiTi']
# plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题,或者转换负号为字符串

class Choice:
    numChoiceDaily = {
        '非常愿意': 0,
        '愿意': 0,
        '一般': 0,
        '不愿意': 0,
        '非常不愿意': 0
    }
    numChoicePlay= {
        '非常愿意': 0,
        '愿意': 0,
        '一般': 0,
        '不愿意': 0,
        '非常不愿意': 0
    }
    numChoiceWeekday= {
        '非常愿意': 0,
        '愿意': 0,
        '一般': 0,
        '不愿意': 0,
        '非常不愿意': 0
    }
    numChoiceHoliday= {
        '非常愿意': 0,
        '愿意': 0,
        '一般': 0,
        '不愿意': 0,
        '非常不愿意': 0
    }



    # init functions
    def __init__(self, df):
        choiceDaily = df['agree_choose_public_daily']
        choicePlay= df['agree_choose_public_play']
        choiceWeekday = df['agree_choose_public_weekday']
        choiceHoliday = df['agree_choose_public_holiday']

        basic_func.initNum(self.numChoiceDaily, choiceDaily)
        basic_func.initNum(self.numChoicePlay, choicePlay)
        basic_func.initNum(self.numChoiceWeekday, choiceWeekday)
        basic_func.initNum(self.numChoiceHoliday, choiceHoliday)




    # draw functions