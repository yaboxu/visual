"""
绘制锡特卡和死亡谷这两个地区在某时段内的气温变化图形
"""

import csv
from datetime import datetime
import matplotlib.pyplot as plt

def get_weather_data(filename, dates, highs, lows):
    with open(filename) as f_obj:
        reader = csv.reader(f_obj)
        header = next(reader)   # 表头header是一个列表
        for index,column in enumerate(header):
            print(index, column)
        
        for row in reader:
            try:
                date = datetime.strptime(row[0], "%Y-%m-%d")
                high = int(row[1])
                low = int(row[3])
            except ValueError:
                print(filename, date, "missing data")
            else:
                dates.append(date)
                highs.append(high)
                lows.append(low)


# 绘制锡特卡气温图表，根据数据绘制图形
filename1 = 'sitka_weather_2014.csv'
dates,highs,lows = [],[],[]
get_weather_data(filename1, dates, highs, lows)
fig = plt.figure(dpi=128, figsize=(10,5))

plt.plot(dates, highs, c='red', alpha=0.3) 
plt.plot(dates, lows, c='blue', alpha=0.3)
plt.fill_between(dates, lows, highs, facecolor='blue', alpha=0.1)

# 在现有图形中加入死亡谷气温数据
filename2 = 'death_valley_2014.csv'
dates,highs,lows = [],[],[]
get_weather_data(filename2, dates, highs, lows)

plt.plot(dates, highs, c='red', alpha=0.5) 
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, lows, highs, facecolor='blue', alpha=0.2)

# 给图表添加说明，设置图形格式
plt.title("sitka`s and death valley`s weather 2014", fontsize=24)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()   # 绘制斜的x轴日期标签
plt.ylabel("tem(F)", fontsize=14)
# print(plt.ylim())   # 查看y值范围
plt.ylim(10,130)   # y值范围分别为：(15,74)(15,117)
plt.tick_params(axis='both', which='major', labelsize=10)

plt.show()
