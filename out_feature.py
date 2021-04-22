import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# solve Chinese font
plt.rcParams['font.sans-serif'] = ['KaiTi']
plt.rcParams['font.serif'] = ['KaiTi']
# plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题,或者转换负号为字符串

class OutFeature:

    numOutDaily = {
        '每天6次以上': 0,
        '每天4-6次': 0,
        '每天2-3次': 0,
        '每天一次': 0,    # "*" just looks the key not like an int var much.  
        '几乎不出门': 0
    }
    numOutAvg = {
        '10km+': 0,
        '5-10km': 0,
        '3-5km': 0,
        '1-3km': 0,
        '1km-': 0
    }
    numFirstOrderAim = {
        '通勤': 0,
        '生活': 0,
        '娱乐': 0,
        '几乎不出行': 0
    }
    numFirstOrderWay = {
        '公共交通': 0,
        '私家车': 0,
        '自行车电动车': 0,
        '步行': 0,
        '其他': 0
    }
    numIsPublic = {
        '每天使用': 0,
        '经常使用': 0,
        '偶尔使用': 0,
        '几乎不使用': 0,
        '不使用': 0
    }



    # init functions
    def __init__(self, df):
        # count of out daily
        self.outDaily = df['num_out_daily']
        # average distance daily
        self.outAvg = df['dis_out_avg']
        # order of out aim
        self.orderAimDaily = df['order_daily']
        self.orderAimLife = df['order_life']
        self.orderAimPlay = df['order_play']
        self.orderAimNoOut = df['order_no_out']
        # order of out methods
        self.orderWayPublic = df['order_public']
        self.orderWayPrivate = df['order_private']
        self.orderWayElec = df['order_elec_bike']
        self.orderWayFoot = df['order_foot']
        self.orderWayOthers = df['order_others']
        # use public transportation
        self.isPublic = df['is_public']

        self.putNumOutDaily()
        self.putNumOutAvg()
        self.putNumFirstOrderAim()
        self.putNumFirstOrderWay()
        self.putNumIsPublic()

    def putNumOutDaily(self):
        for i in self.outDaily:
            if i == 1:
                self.numOutDaily['每天6次以上'] += 1
            elif i == 2:
                self.numOutDaily['每天4-6次'] += 1
            elif i == 3:
                self.numOutDaily['每天2-3次'] += 1
            elif i == 4:
                self.numOutDaily['每天一次'] += 1
            elif i == 5:
                self.numOutDaily['几乎不出门'] += 1

    def putNumOutAvg(self):
        for i in self.outAvg:
            if i == 1:
                self.numOutAvg['10km+'] += 1
            elif i == 2:
                self.numOutAvg['5-10km'] += 1
            elif i == 3:
                self.numOutAvg['3-5km'] += 1
            elif i == 4:
                self.numOutAvg['1-3km'] += 1
            elif i == 5:
                self.numOutAvg['1km-'] += 1

    def putNumFirstOrderAim(self):
        # daily
        for i in self.orderAimDaily:
            if i == 1:
                self.numFirstOrderAim['通勤'] += 1
        for i in self.orderAimLife:
            if i == 1:
                self.numFirstOrderAim['生活'] += 1
        for i in self.orderAimPlay:
            if i == 1:
                self.numFirstOrderAim['娱乐'] += 1
        for i in self.orderAimNoOut:
            if i == 1:
                self.numFirstOrderAim['几乎不出行'] += 1

    def putNumFirstOrderWay(self):
        for i in self.orderWayPublic:
            if i == 1:
                self.numFirstOrderWay['公共交通'] += 1
        for i in self.orderWayPrivate:
            if i == 1:
                self.numFirstOrderWay['私家车'] += 1
        for i in self.orderWayElec:
            if i == 1:
                self.numFirstOrderWay['自行车电动车'] += 1
        for i in self.orderWayFoot:
            if i == 1:
                self.numFirstOrderWay['步行'] += 1
        for i in self.orderWayOthers:
            if i == 1:
                self.numFirstOrderWay['其他'] += 1

    def putNumIsPublic(self):
        for i in self.isPublic:
            if i == 1:
                self.numIsPublic['每天使用'] += 1
            elif i == 2:
                self.numIsPublic['经常使用'] += 1
            elif i == 3:
                self.numIsPublic['偶尔使用'] += 1
            elif i == 4:
                self.numIsPublic['几乎不使用'] += 1
            elif i == 5:
                self.numIsPublic['不使用'] += 1



    # print functions



    # draw functions
    def drawNumOutDaily(self):
        sNumOutDaily = pd.Series(self.numOutDaily, name='每日出行次数')
        sNumOutDaily.plot.bar()
        plt.show()

    def drawNumOutAvg(self):
        sNumOutAvg = pd.Series(self.numOutAvg, name='每日平均出行距离')
        sNumOutAvg.plot.bar()
        plt.show()

    def drawNumFirstOrderAim(self):
        sNumFirstOrder = pd.Series(self.numFirstOrderAim)
        sNumFirstOrder.plot.bar()
        plt.show()

    def drawNumFirstOrderWay(self):
        sNumFirstOrder = pd.Series(self.numFirstOrderWay)
        sNumFirstOrder.plot.bar()
        plt.show()

    def drawNumIsPublic(self):
        sNumIsPublic = pd.Series(self.numIsPublic, name='使用公共交通的频率')
        sNumIsPublic.plot.pie(autopct='%.2f')
        plt.show()