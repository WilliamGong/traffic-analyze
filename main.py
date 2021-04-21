import numpy as np
import pandas as pd
import basic_info
import out_feature

df = pd.read_csv("data.csv")

#print(df)
#print(df['provience'])
#print(df[df['provience'] == '广东'])
#print(df.loc[:, ['order_daily', 'order_life', 'order_play', 'order_no_out']])

dfBasicInfo = basic_info.BasicInfo(df)
dfOutFeature = out_feature.OutFeature(df)

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
'''
dfOutFeature.drawNumIsPublic()