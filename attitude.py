import numpy as np
import pandas as pd
import basic_func

class Trend:
    avgs = []
    index = [
        '我知道并关注最新的疫情相关防控措施', 
        '我知道并关注国内的疫情新增情况', 
        '我知道并关注国外的疫情新增情况', 
        '我知道并关注最新的新冠疫苗发展情况'
    ]

    def __init__(self, df):
        new = df['agree_new']
        newNational = df['agree_new_national']
        newInternational = df['agree_new_international']
        vaccine = df['agree_vaccine']

        self.avgs.append(basic_func.indexAvg(new))
        self.avgs.append(basic_func.indexAvg(newNational))
        self.avgs.append(basic_func.indexAvg(newInternational))
        self.avgs.append(basic_func.indexAvg(vaccine))



class Mask:
    avgs = []
    index = [
        '只要出门，我就会戴好口罩保护自己', 
        '现阶段，我认为戴口罩乘坐公共交通出行很安全', 
        '现阶段，我认为不戴口罩乘坐公共交通出行很安全', 
        '我认为接种了新冠疫苗后，乘坐公共交通就不用佩戴口罩了'
    ]

    def __init__(self, df):
        selfProtect = df['agree_mask_self-protect']
        safePublicWithMask = df['agree_mask_safe_public-with-mask']
        safePublicNoMask = df['agree_mask_safe_public-no-mask']
        publicNoMaskAfterVaccine = df['agree_mask_public-no-mask-after-vaccine']

        self.avgs.append(basic_func.indexAvg(selfProtect))
        self.avgs.append(basic_func.indexAvg(safePublicWithMask))
        self.avgs.append(basic_func.indexAvg(safePublicNoMask))
        self.avgs.append(basic_func.indexAvg(publicNoMaskAfterVaccine))



class Necessity:
    avgs = []
    index = [
        '减少发车班次', 
        '重点防疫站点不停靠', 
        '高峰期限制站点人流量', 
        '站点及车厢设置避免拥挤标志', 
        '强化站点每日设施消毒', 
        '落实工作人员和司机每日健康检查', 
        '乘客必须佩戴口罩', 
        '检查乘客绿色健康码', 
        '测量乘客体温', 
        '跟踪乘客出行轨迹', 
        '设置不同时段价格优惠引导乘客错峰出行', 
        '根据上下班出行需求定制公交', 
        '为老人孩童等易感人群设置低风险车厢'
    ]

    def __init__(self, df):
        decline = df['agree_public_decline']
        noStop = df['agree_public_no-stop']
        limit = df['agree_public_limit-people']
        sign = df['agree_public_sign']
        disinfect = df['agree_public_disinfect']
        check = df['agree_public_driver-check']
        mask = df['agree_public_mask']
        qr = df['agree_public_qr']
        temp = df['agree_public_temp']
        track = df['agree_public_track']
        time = df['agree_public_multiple-time']
        custom = df['agree_public_custom']
        special = df['agree_public_special']

        self.avgs.append(basic_func.indexAvg(decline))
        self.avgs.append(basic_func.indexAvg(noStop))
        self.avgs.append(basic_func.indexAvg(limit))
        self.avgs.append(basic_func.indexAvg(sign))
        self.avgs.append(basic_func.indexAvg(disinfect))
        self.avgs.append(basic_func.indexAvg(check))
        self.avgs.append(basic_func.indexAvg(mask))
        self.avgs.append(basic_func.indexAvg(qr))
        self.avgs.append(basic_func.indexAvg(temp))
        self.avgs.append(basic_func.indexAvg(track))
        self.avgs.append(basic_func.indexAvg(time))
        self.avgs.append(basic_func.indexAvg(custom))
        self.avgs.append(basic_func.indexAvg(special))



class Effect:
    avgs = []
    index = [
        '减少发车班次', 
        '重点防疫站点不停靠', 
        '高峰期限制站点人流量', 
        '站点及车厢设置避免拥挤标志', 
        '强化站点每日设施消毒', 
        '落实工作人员和司机每日健康检查', 
        '乘客必须佩戴口罩', 
        '检查乘客绿色健康码', 
        '测量乘客体温', 
        '跟踪乘客出行轨迹', 
    ]

    def __init__(self, df):
        decline = df['agree_public-eff_decline']
        noStop = df['agree_public-eff_no-stop']
        limit = df['agree_public-eff_limit-people']
        sign = df['agree_public-eff_sign']
        disinfect = df['agree_public-eff_disinfect']
        check = df['agree_public-eff_driver-check']
        mask = df['agree_public-eff_mask']
        qr = df['agree_public-eff_qr']
        temp = df['agree_public-eff_temp']
        track = df['agree_public-eff_track']

        self.avgs.append(basic_func.indexAvg(decline))
        self.avgs.append(basic_func.indexAvg(noStop))
        self.avgs.append(basic_func.indexAvg(limit))
        self.avgs.append(basic_func.indexAvg(sign))
        self.avgs.append(basic_func.indexAvg(disinfect))
        self.avgs.append(basic_func.indexAvg(check))
        self.avgs.append(basic_func.indexAvg(mask))
        self.avgs.append(basic_func.indexAvg(qr))
        self.avgs.append(basic_func.indexAvg(temp))
        self.avgs.append(basic_func.indexAvg(track))



class Reason:
    avgs = []
    index = [
        '出行便利程度', 
        '出行时间长度', 
        '车厢拥挤程度', 
        '票价优惠程度', 
        '家人朋友意见', 
        '权威专家意见', 
        '其他人的意见'
    ]

    def __init__(self, df):
        convience = df['agree_reason_convience']
        time = df['agree_reason_time']
        crowd = df['agree_reason_crowd']
        price = df['agree_reason_price']
        friend = df['agree_reeason_friend']
        export = df['agree_reason_export']
        others = df['agree_reason_others']

        self.avgs.append(basic_func.indexAvg(convience))
        self.avgs.append(basic_func.indexAvg(time))
        self.avgs.append(basic_func.indexAvg(crowd))
        self.avgs.append(basic_func.indexAvg(price))
        self.avgs.append(basic_func.indexAvg(friend))
        self.avgs.append(basic_func.indexAvg(export))
        self.avgs.append(basic_func.indexAvg(others))