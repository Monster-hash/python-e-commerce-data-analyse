
from PythonDataAnalyse import df
import matplotlib.pyplot as plt

from matplotlib.font_manager import FontProperties

my_font =FontProperties(fname='C:/Windows/Fonts/Deng.ttf',size=12,)

#1.按照渠道分组聚合，统计用户数
custom = df.groupby('chanelID')['userID'].count()
#2.设置字体
plt.rcParams['font.sans-serif']=['SimHei']
#3.使用pandas中方法直接画图
custom.plot.pie(figsize=(12,8),labels=custom.index,autopct="%1.1f%%",rotatelabels=True)
#4.设置标题
plt.title('各渠道来源用户占比',loc='left',fontproperties=my_font,color='red',size=15)
plt.savefig('t2.png')
