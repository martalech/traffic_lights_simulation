#caculate the light intensity based on people class
from light import Light
from person import Person
import math
import numpy as np

#1. 设定光强的参数：最大值，模式（百分比），阈值
#2. 传入位置数据：行人位置和灯的位置
#3. 根据距离设定光强（似曾相似）

#4. 基于人还是基于灯？？？？？？？？返回这么多人的光强判定有意义吗？？？？

#Q:是否有必要新建一个类？？？？？？？？？？？？参数获取似乎重合？
#天晚矣，明日再战ZZZ

class Intensity():

    def __init__(self):
        
