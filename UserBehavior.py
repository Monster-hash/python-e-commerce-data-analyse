from PythonDataAnalyse import df
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

my_font =FontProperties(fname='C:/Windows/Fonts/Deng.ttf',size=12,)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
#1.按周几做聚合
week = df.groupby('weekday')['orderID'].count()
week

#2.设置横纵坐标
weekX = ['周一','周二','周三','周四','周五','周六','周日']
weekY = week.values

#3.设置X轴
plt.xticks(range(len(weekX)),weekX,fontproperties=my_font)

#4.设置条形图
rects = plt.bar(range(len(weekX)),weekY,width=0.3,color=['r','g','b'])

#5.设置每个数据条的位置
for rect in rects:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height+0.5, str(height),ha="center")

#6.设置标题
plt.title('用户下单时间分析',fontproperties=my_font,color='red',size=15)
#7.显示保存
plt.savefig('t3.png')