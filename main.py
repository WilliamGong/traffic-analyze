import numpy as np
import pandas as pd
import basic_info
import out_feature
import choice
import basic_func
import attitude

df = pd.read_csv("data.csv")

#print(df)
#print(df['gender'])
#print(df['provience'])
#print(df[df['provience'] == '广东'])
#print(df.loc[:, ['order_daily', 'order_life', 'order_play', 'order_no_out']])

dfBasicInfo = basic_info.BasicInfo(df)
dfOutFeature = out_feature.OutFeature(df)
dfChoice = choice.Choice(df)
dfTrend = attitude.Trend(df)
dfMask = attitude.Mask(df)
dfNecessity = attitude.Necessity(df)
dfEffect = attitude.Effect(df)
dfReason = attitude.Reason(df)



# basic info
'''
dfBasicInfo.getNumGender()
dfBasicInfo.getNumAge()
'''
'''
dfBasicInfo.getNumProvience()
dfBasicInfo.getIsCar()
'''

'''
dfBasicInfo.drawNumGender()
basic_func.drawNumPie(dfBasicInfo.numAge, '年龄分布')
dfBasicInfo.drawNumProvience()
basic_func.drawNumPie(dfBasicInfo.numCityGuangdong, '广东省调查对象来源城市分布')
basic_func.drawNumPie(dfBasicInfo.numDegree, '学历分布')
basic_func.drawNumPie(dfBasicInfo.numJob, '工作性质分布')
basic_func.drawNumPie(dfBasicInfo.numIncome, '收入分布')
basic_func.drawNumPie(dfBasicInfo.numIsCar, dfBasicInfo.indexIsCar, '私家车拥有情况分布')
'''



# out feature
'''
dfOutFeature.drawNumOutDaily()
dfOutFeature.drawNumOutAvg()
dfOutFeature.drawNumFirstOrderAim()
dfOutFeature.drawNumFirstOrderWay()
dfOutFeature.drawNumIsPublic()
'''



# attitudes
'''
basic_func.drawNumBar(dfTrend.avgs, dfTrend.index, '关于疫情动向的同意程度')
basic_func.drawNumBar(dfMask.avgs, dfMask.index, '关于戴口罩出行的描述的同意程度')
basic_func.drawNumBar(dfNecessity.avgs, dfNecessity.index, '关于公共交通防控措施有实施的必要性的同意程度')
basic_func.drawNumBar(dfEffect.avgs, dfEffect.index, '防控措施的实施效果的满意程度')
basic_func.drawNumBar(dfReason.avgs, dfReason.index, '使用公共交通的影响因素')
'''



# choice
'''
basic_func.drawNumPie(dfChoice.numChoiceDaily, '上下班出行是否选择公共交通')
basic_func.drawNumPie(dfChoice.numChoicePlay, '娱乐出行是否选择公共交通')
basic_func.drawNumPie(dfChoice.numChoiceWeekday, '工作日出行是否选择公共交通')
basic_func.drawNumPie(dfChoice.numChoiceHoliday, '清明节假期出行是否愿意选择公共交通')
'''