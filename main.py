import numpy as np
import pandas as pd
import basic_info

df = pd.read_csv("data.csv")

#print(df)
#print(df['provience'])
#print(df[df['provience'] == '广东'])

dfBasicInfo=basic_info.BasicInfo(df)

#dfBasicInfo.printCitiesGuangdong()

'''
dfBasicInfo.getNumGender()
dfBasicInfo.getNumAge()
'''

'''
dfBasicInfo.getNumProvience()
'''
dfBasicInfo.getIsCar()
'''
dfBasicInfo.drawNumProvience()
dfBasicInfo.drawNumAge()
dfBasicInfo.drawNumCityGuangdong()
dfBasicInfo.drawNumDegree()
dfBasicInfo.drawNumJob()
dfBasicInfo.drawNumIncome()
'''