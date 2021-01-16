from PythonDataAnalyse import df
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt

my_font =FontProperties(fname='C:/Windows/Fonts/Deng.ttf',size=12,)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

pivoted_counts=df.pivot_table(index='userID',columns='month',
                             values='orderTime',aggfunc='count').fillna(0)
pivoted_counts.head()
#复购率
# 复购率的定义是在某时间窗口内消费两次及以上的用户在总消费用户中占比。这里的时间窗口是月。

#1.引入numpy
import numpy as np

#2. 将数据转换一下，消费两次及以上记为1，消费一次记为0，没有消费记为NaN。
pcRepeatBuy =pivoted_counts.applymap(lambda x: 1 if x>1 else np.NaN if x==0 else 0)
pcRepeatBuy.head()

#3.绘图
#用sum和count相除即可计算出复购率。count是总的消费用户数，sum是两次以上的消费用户数。
(pcRepeatBuy.sum()/pcRepeatBuy.count()).plot(figsize=(15,6))

plt.title('复购率分析',fontproperties=my_font,color='red',size=15)
plt.savefig('t5.png')