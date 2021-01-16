from PythonDataAnalyse import df
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

my_font =FontProperties(fname='C:/Windows/Fonts/Deng.ttf',size=12,)

#RFM根据用户的活跃程度，频率，贡献程度 分类

#1.备份整个数据
customdf = df.copy()

#2.删除退单
customdf.drop(index=df[df.chargeback == '是'].index, inplace=True)
customdf

#3.将userID设置为索引
customdf.set_index('userID',drop=True,inplace=True)

#4.将原始订单中订单量全部置为1
customdf['orders'] = 1
customdf

#5.数据透视
rfmdf = customdf.pivot_table(index=['userID'],
                    values=['orderAmount','orderDate','orders'],
                    aggfunc={'orderDate':'max',
                            'orderAmount':'sum',
                            'orders':'sum'})

#6.处理RFM模型中的R
rfmdf['R'] = (rfmdf.orderDate.max()-rfmdf.orderDate).dt.days

#7.处理RFM模型中的F与M
rfmdf.rename(columns={'orderAmount':'M','orders':'F'},inplace=True)
rfmdf.head()
rfmdf.describe()

#1. 对用户分类，设置标签
def rfm_func(x):
    level = x.apply(lambda x: "1" if x >= 0 else '0')
    label = level.R + level.F + level.M
    d = {
        '011':'重要价值客户',
        '111':'重要唤回客户',
        '001':'重要深耕客户',
        '101':'重要挽留客户',
        '010':'潜力客户',
        '110':'一般维持客户',
        '000':'新客户',
        '100':'流失客户'
    }
    result = d[label]
    return result

#2.根据模型打标签
rfmdf['label'] = rfmdf[['R','F','M']].apply(lambda x:x-x.mean()).apply(rfm_func,axis=1)

#3.分组聚合
rfmdf_res = rfmdf.groupby('label').count()
#print(rfmdf_res)

#1.绘制图形
rfmdf.label.value_counts().plot.bar(figsize=(20,9))
#2.设置X轴
plt.xticks(rotation=0,fontproperties=my_font)
plt.savefig('t6.png')