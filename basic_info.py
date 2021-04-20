import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# solve Chinese font
plt.rcParams['font.sans-serif'] = ['KaiTi']
plt.rcParams['font.serif'] = ['KaiTi']
# plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题,或者转换负号为字符串


class BasicInfo:

    numCar = 0
    sumCar = 0
    numNoCar = 0

    numGender = {
        "male": 0,
        "female": 0
    }
    numAge = {
        "18-": 0,
        "19-25": 0,
        "26-30": 0,
        "31-40": 0,
        "41-50": 0,
        "51-60": 0,
        "61+": 0
    }
    numProvience = {}
    numCityGuangdong = {}
    numDegree = {
        '小学': 0,
        '初中': 0,
        '中专/高中': 0,
        '大专/本科': 0,
        '硕士及以上': 0
    }
    numJob = {
        '学生': 0,
        '通勤时间固定': 0,
        '通勤时间不固定': 0
    }
    numIncome = {
        '3k-': 0,
        '3k-6k': 0,
        '6k-10k': 0,
        '10k+': 0
    }



    # init fuctions
    def __init__(self, df):
        """ This is the init function. 
            It initializes members. 

        Args:
            df (Pandas DataFrame): df of data.csv
        """        
        self.genders = df["gender"]
        self.ages = df["age"]
        self.proviences = df["provience"]
        self.cities = df['city']
        self.dfCitiesGuangdong = df[df['provience'] == '广东']
        self.citiesGuangdong = self.dfCitiesGuangdong['city']
        self.degree = df['degree']
        self.jobs = df['job']
        self.income = df['income_mounth']
        self.isCar = df['is_car']

        self.putNumAge()
        self.putNumGender()
        self.putNumProvience()
        self.putNumCityGuangdong()
        self.putNumDegree()
        self.putNumJob()
        self.putNumIncome()
        self.putIsCar()
    
    def putNumGender(self):
        """ It init numGender. 
        """        
        for gender in self.genders:
            if gender == 1:
                self.numGender['male'] += 1
            elif gender == 2: 
                self.numGender['female'] += 1

    def putNumAge(self):
        """ It init numAge. 
        """        
        for age in self.ages:
            if age == 1:
                self.numAge['18-'] += 1
            elif age == 2:
                self.numAge['19-25'] += 1
            elif age == 3:
                self.numAge['26-30'] += 1
            elif age == 4:
                self.numAge['31-40'] += 1
            elif age == 5:
                self.numAge['41-50'] += 1
            elif age == 6:
                self.numAge['51-60'] += 1
            elif age == 7:
                self.numAge['61+'] += 1

    def putNumProvience(self):
        for provience in self.proviences:
            if self.numProvience.get(str(provience), 0) == 0:
                self.numProvience[provience] = 1
            else:
                self.numProvience[provience] += 1

    def putNumCityGuangdong(self):
        for city in self.citiesGuangdong:
            if self.numCityGuangdong.get(str(city), 0) == 0:
                self.numCityGuangdong[city] = 1
            else:
                self.numCityGuangdong[city] += 1
        
    def putNumDegree(self):
        for i in self.degree:
            if i == 1:
                self.numDegree['小学'] += 1
            elif i == 2:
                self.numDegree['初中'] += 1
            elif i == 3:
                self.numDegree['中专/高中'] += 1
            elif i == 4:
                self.numDegree['大专/本科'] += 1
            elif i == 5:
                self.numDegree['硕士及以上'] += 1

    def putNumJob(self):
        for i in self.jobs:
            if i == 1:
                self.numJob['学生'] += 1
            elif i == 2:
                self.numJob['通勤时间固定'] += 1
            elif i == 3:
                self.numJob['通勤时间不固定'] += 1

    def putNumIncome(self):
        for i in self.income:
            if i == 1:
                self.numIncome['3k-'] += 1
            elif i == 2:
                self.numIncome['3k-6k'] += 1
            elif i == 3:
                self.numIncome['6k-10k'] += 1
            elif i == 4:
                self.numIncome['10k+'] += 1

    def putIsCar(self):
        for i in self.isCar:
            if i == 1:
                self.numCar += 1
                self.sumCar += 1
            else:
                self.sumCar += 1
                self.numNoCar += 1



    # debug functions
    def printGenders(self):
        print(self.genders)

    def printAges(self):
        print(self.ages)

    def printCities(self):
        print(self.cities)

    def printCitiesGuangdong(self):
        print(self.citiesGuangdong)
    


    # print functions
    def getNumGender(self):
        print("male number: " + str(self.numGender['male']))
        print('female number: ' + str(self.numGender['female']))

    def getNumAge(self):
        print("18-: " + str(self.numAge['18-']))
        print("19-25: " + str(self.numAge['19-25']))
        print("26-30: " + str(self.numAge['26-30']))
        print('31-40: ' + str(self.numAge['31-40']))
        print('41-50: '+ str(self.numAge['41-50']))
        print('51-60: ' + str(self.numAge['51-60']))
        print('61+: ' + str(self.numAge['61+']))

    def getNumProvience(self):
        for i in self.numProvience.items():
            print(i)

    def getIsCar(self):
        print('一共有'+ str(self.sumCar) + '调查者')
        print('一共有' + str(self.numCar) + '拥有私家车')
        print('一共有' + str(self.numNoCar) + '没有私家车')
        


    # draw fuctions
    def drawNumAge(self):
        sNumAge = pd.Series(self.numAge)
        sNumAge.plot.bar()
        plt.show()

    def drawNumProvience(self):
        sNumProvience = pd.Series(self.numProvience)
        # sort with value (down)
        sNumProvience = sNumProvience.sort_values(ascending=False)
        sNumProvience.plot.bar()
        plt.show()

    def drawNumCityGuangdong(self):
        sNumCityGuangdong = pd.Series(self.numCityGuangdong)
        # sort with value (down)
        sNumCityGuangdong = sNumCityGuangdong.sort_values(ascending=False)
        sNumCityGuangdong.plot.bar()
        plt.show()
    
    def drawNumDegree(self):
        sNumDegree = pd.Series(self.numDegree)
        sNumDegree.plot.bar()
        plt.show()

    def drawNumJob(self):
        sNumJob = pd.Series(self.numJob)
        # change index to Chinese
        sNumJob.plot.bar()
        plt.show()
    
    def drawNumIncome(self):
        sNumIncome = pd.Series(self.numIncome)
        sNumIncome.plot.bar()
        plt.show()