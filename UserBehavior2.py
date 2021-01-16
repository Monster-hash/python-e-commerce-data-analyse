from PythonDataAnalyse import pd
from PythonDataAnalyse import df
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

my_font =FontProperties(fname='C:/Windows/Fonts/Deng.ttf',size=12,)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

#1.备份整个数据
df1 = df.copy()

#2.设置时间周期30min
s = df1['orderTime'].dt.floor('30T')

#3.将下单时间转换成时间段
df1['orderTime'] = s.dt.strftime('%H:%M') + '-' + (s + pd.Timedelta(30 * 60, unit='s')).dt.strftime('%H:%M')
df1
#4.根据时间段分组聚合
tiemdf = df1.groupby('orderTime')['orderID'].count()
tiemdf
tiemdfX = tiemdf.index
tiemdfY = tiemdf.values
tiemdfY

#5.设置画布大小
plt.figure(figsize=(20,8),dpi=80)

#6.设置样式风格
plt.style.use('ggplot')

#7.X轴形式
plt.xticks(range(len(tiemdfX)),tiemdfX,rotation=90)

#8.绘制数据条形图
rect = plt.bar(tiemdfX,tiemdfY,width=0.3,color=['orange'])
plt.title('用户下单时间段分析',fontproperties=my_font,color='red',size=20)
plt.savefig('t4.png')


#1.客单价
df.orderAmount.sum()/df.userID.unique().size

#1.检查数据字段
df['userid'] = df["userID"].str[0:4]
df['userid'].unique()

#2.userID只保留数字
df['userID'] = df["userID"].str[5:]

pivoted_counts=df.pivot_table(index='userID',columns='month',values='orderTime',aggfunc='count').fillna(0)
pivoted_counts.head()

#print(pivoted_counts)

