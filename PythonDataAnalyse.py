#加载处理数据所需要的库
import pandas as pd

#引入时间模块, 确定周期时间
import datetime

#读取数据文件
# path 文件路径 index_col 指定行索引
df = pd.read_excel('order2020.xlsx',index_col='id')

#确定开始时间节点与结束时间节点
startTime = datetime.datetime(2020, 1, 1) #开始时间（默认补齐）
endTime = datetime.datetime(2020, 12, 31, 23, 59, 59) #结束时间

#将2020年1月1日前数据删除
df[df.orderTime < startTime]
#删除数据 drop(index="索引", inplace=True,False)
df.drop(index=df[df.orderTime < startTime].index, inplace=True) #inplace=True在原df数据删除

#将2020年12月31日后数据删除
df[df.orderTime > endTime]
df.drop(index=df[df.orderTime > endTime].index, inplace=True)

#下单时间与支付时间间隔
df['payinterval'] = (df.payTime-df.orderTime).dt.total_seconds()
#支付时间间隔大于30分钟与支付时间早于下单时间
df[df.payinterval>1800]
df.drop(index=df[df.payinterval>1800].index, inplace=True)
df.drop(index=df[df.payinterval<0].index, inplace=True)

# 订单金额为负
df[df.orderAmount < 0]
# 付款金额为负
df[df.payment < 0]
# 删除相应订单
df.drop(index=df[df.orderAmount < 0].index, inplace=True) #删除负订单金额
df.drop(index=df[df.payment < 0].index, inplace=True) #删除负付款金额

''''#1.查看非空信息
df.info()
#2. 查看整体描述
df.describe()
print(df.describe())
'''

# 订单orderID不重复的个数
df.orderID.unique().size
# 删除重复数据
df.drop(index=df[df.orderID.duplicated()].index, inplace=True)
# df.info()

# PR000000  代表商品下架
df.goodsID[df.goodsID == 'PR000000'].size
df.drop(index=df[df.goodsID == 'PR000000'].index, inplace=True)
# df.info()

#1.查看chanelID空值
df[df.chanelID.isnull()]
#2.对空值进行修补
df['chanelID'].fillna(value=df.chanelID.mode()[0], inplace=True)
#df.info()

#df.platformType.unique() #列出所有不重复平台

df['platformType']=df['platformType'].str.replace(" ","") #空字符串代替空格
df.platformType.unique() #列出所有不重复平台，再次检查
#print(df.platformType.unique())

# 创建折扣字段
df['discount'] = (df.payment/df.orderAmount)
#df.describe()

# 平均折扣
meanDiscount = df[df['discount']<=1].discount.sum() / df[df['discount']<=1].discount.size
meanDiscount

# 找到折扣大于1的数据
df[df['discount']>1]
df['payment'] = df['payment'].mask(df['discount']>1,None)

# 对折扣大于1的数据进行填补
df['payment'].fillna(value=df.orderAmount*meanDiscount , inplace=True)
#df.info()

df['discount'] = round((df.payment/df.orderAmount),2)

df['month'] = df['orderTime'].dt.month #提取月份
df['weekday'] = df['orderTime'].dt.dayofweek+1 #周几
df['orderDate'] = df['orderTime'].dt.date

#总体概览
# 1.销售GMV
df.orderAmount.sum()/10000
# 2.成交总和
df.payment.sum()/10000
# 3.实际成交额
df[df.chargeback=="否"].payment.sum()/10000
# 4.订单数量
df.orderID.unique().size
# 5.退货订单数
df[df.chargeback=="是"].orderID.size
# 6.退货率
df[df.chargeback=="是"].orderID.size/df.orderID.unique().size
# 7.用户数
df.userID.unique().size

# pd.set_option('display.width',None)
# print(df.describe())


