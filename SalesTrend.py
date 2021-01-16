from PythonDataAnalyse import df #调用PythonDataAnalyse.py的df函数

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

#1.2设置字体
my_font =FontProperties(fname='C:/Windows/Fonts/Deng.ttf',size=12,)

#1.3设置画布大小
plt.figure(figsize=(10,6))

#1.4设置网格线 辅助线
plt.grid(alpha=0.4)

#2.横纵坐标值
#2.1所有横坐标都一致
x = df.groupby('month')['orderAmount'].sum().index
#2.2GMV
y1 = df.groupby('month')['orderAmount'].sum().values/10000
#2.3销售实际付款
y2 = df.groupby('month')['payment'].sum().values/10000
#2.4不含退单销售额
y3 = df[df.chargeback=="否"].groupby('month')['payment'].sum().values/10000

#2.5 X横轴坐标文字
x_ticks_label = ["{}月份".format(i) for i in x]
#2.6 x轴刻度，标签文字
plt.xticks(x,x_ticks_label,rotation = 45,fontproperties = my_font)

#3. 绘制三条折线走势
#plot 折线图
#color 单词，#0022FF rgb(0,255)
plt.plot(x,y1,label='GMV',color="red",marker='o')
plt.plot(x,y2,label='销售额',color="orange",marker='*')
plt.plot(x,y3,label='不含退单',color="blue",marker = '.')

#4.标记横纵轴名字与标题
plt.xlabel('月份',fontproperties=my_font)
plt.ylabel("销售额万元",fontproperties=my_font)
plt.title('销售额走势',fontproperties=my_font,color='red',size=15)

#5.添加折点坐标
for a,b in zip(x,y1):
    plt.annotate('(%.2f)'%(b),xy=(a,b),xytext=(-10,10),textcoords='offset points')

#6.设置图例
plt.legend(prop=my_font,loc='upper left')
#7.显示图形
#plt.show()
plt.savefig('t1.png')