import numpy as np
import pandas as pd
import basic_info
import out_feature
import choice
import basic_func

df = pd.read_csv("data.csv")

#print(df)
#print(df['gender'])
#print(df['provience'])
#print(df[df['provience'] == '广东'])
#print(df.loc[:, ['order_daily', 'order_life', 'order_play', 'order_no_out']])

dfBasicInfo = basic_info.BasicInfo(df)
dfOutFeature = out_feature.OutFeature(df)
dfChoice = choice.Choice(df)

#dfBasicInfo.printCitiesGuangdong()



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
dfBasicInfo.drawNumProvience()
dfBasicInfo.drawNumAge()
dfBasicInfo.drawNumCityGuangdong()
dfBasicInfo.drawNumDegree()
dfBasicInfo.drawNumJob()
dfBasicInfo.drawNumIncome()
'''



# out feature
'''
dfOutFeature.drawNumOutDaily()
dfOutFeature.drawNumOutAvg()
dfOutFeature.drawNumFirstOrderAim()
dfOutFeature.drawNumFirstOrderWay()
dfOutFeature.drawNumIsPublic()
'''



# choice
basic_func.drawNumPie(dfChoice.numChoiceDaily, '上下班出行是否选择公共交通')
basic_func.drawNumPie(dfChoice.numChoicePlay, '娱乐出行是否选择公共交通')
basic_func.drawNumPie(dfChoice.numChoiceWeekday, '工作日出行是否选择公共交通')
basic_func.drawNumPie(dfChoice.numChoiceHoliday, '清明节假期出行是否愿意选择公共交通')