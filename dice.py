"""多次投掷两个骰子，点数相加"""

import pygal
from random import randint

class Dice():
    """一个表示骰子的类"""
    def __init__(self, num_sides=6):
        """初始化属性值"""
        self.num_sides = num_sides
        
    def roll(self):
        """掷骰子"""
        return randint(1, self.num_sides)


# 创建类的两个实例
d1 =Dice()
d2 =Dice(10)

# 掷骰子并储存结果
results = []
for roll_num in range(10000):
    result = d1.roll() + d2.roll()
    results.append(result)

# 分析结果
frequencies = [] 
max_result = d1.num_sides + d2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency) 
       
# 可视化结果
hist = pygal.Bar() 

hist.title = "Results of rolling a D6 and a D10 10000 times."
hist.x_labels = [str(value) for value in range(2, max_result+1)]  # 注意类型str
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies) 
hist.render_to_file('dice.svg')

# 浏览器file:///C:/users/Administrator/Desktop/python_work/keshihua/dice.svg
