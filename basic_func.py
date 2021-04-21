import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# solve Chinese font
plt.rcParams['font.sans-serif'] = ['KaiTi']
plt.rcParams['font.serif'] = ['KaiTi']
# plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题,或者转换负号为字符串




# init functions
def initNum(dic, ser):
    """ This function is used to init the dictionary with index of "非常愿意", "愿意", "一般", "不愿意", "非常不愿意". 

    Args:
        dic (python dictionary): Num dictionary to storage data
        ser (pandas series): series from source df. 
    """    
    for i in ser:
        if i == 1:
            dic['非常愿意'] += 1
        elif i == 2:
            dic['愿意'] += 1
        elif i == 3:
            dic['一般'] += 1
        elif i == 4:
            dic['不愿意'] += 1
        elif i == 5:
            dic['非常不愿意'] += 1



# draw functions
def drawNumPie(dic, title):
        sDic = pd.Series(dic, name=title)
        sDic.plot.pie(autopct='%.2f')
        plt.show()