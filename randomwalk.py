"""随机漫步"""

from random import choice
import matplotlib.pyplot as plt

class RandomWalk():
    """一个表示随机漫步的类"""
    def __init__(self, num_points=5000):
        """初始化属性值"""
        self.num_points = num_points
        
        # 随机漫步起始坐标(0,0)
        self.x_values = [0]
        self.y_values = [0]
    
    def get_step(self):
        """确定每次漫步的距离和方向"""
        direction = choice([1,-1])
        distance = choice([0,1,2,3,4])
        step = direction * distance
        return step
           
    def fill_walk(self):
        """确定每次漫步经过的所有点的坐标"""
        
        # 持续漫步直至达到所设点数
        while len(self.x_values) < self.num_points:
            
            # 确定漫步的距离和方向
            x_step = self.get_step() 
            y_step = self.get_step() 
            
            # 拒绝原地踏步
            if x_step==0 and y_step==0:
                continue
                
            # 确定漫步经过的点的坐标
            next_x = self.x_values[-1] + x_step 
            next_y = self.y_values[-1] + y_step
            
            self.x_values.append(next_x)
            self.y_values.append(next_y)
            

while True:
    # 创建一个RandomWalk()实例
    rw = RandomWalk(50000)
    rw.fill_walk() 
    
    # 设置图形大小
    plt.figure(dpi=128, figsize=(10,5))
    
    point_numbers = list(range(rw.num_points))
    # 颜色映射，c值为列表
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, 
               edgecolor='none', s=1)
    
    # 绿点开始，红点结束         
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    
    plt.show()
    
    # 询问是否继续漫步，若否，结束
    keep_running = input("Make aother walk?(y/n): ")
    if keep_running == 'n':
        break
