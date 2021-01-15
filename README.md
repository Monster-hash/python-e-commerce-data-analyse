# 一.读取数据

## 1.1 加载数据文件
```
import pandas as pd //加载处理数据所需要的库
df = pd.read_excel('order2020.xlsx',index_col='id')  //读取数据文件 
#pd.set_option('display.width',None) //设置数据展示宽度
#print(df.tail(10)) //展示导入数据的后10行，以便检查
```
 - pd.set_option('display.width',None)  //设置数据展示宽度，解决列展示出现省略号问题
 - print(df.head()) //默认读取前5行记录
 - print(df.tail(10)) //读取后10行的数据，无参默认为5行
![001](https://github.com/Monster-hash/python-e-commerce-data-analyse/blob/main/picture/001.png)
## 1.2 提取数据

### 1.2.1根据业务需要提取数据,提取2020年数据

```
# 1.引入时间模块, 确定周期时间
import datetime

# 2.确定开始时间节点与结束时间节点  
startTime = datetime.datetime(2020, 1, 1) #开始时间
endTime = datetime.datetime(2020, 12, 31, 23, 59, 59) #结束时间

# 3.将2020年1月1日前数据删除  
df[df.orderTime < startTime]  
#删除数据 drop(index="索引", inplace=True,False)  
df.drop(index=df[df.orderTime < startTime].index, inplace=True)  
  
# 4.将2020年12月31日后数据删除  
df[df.orderTime > endTime]  
df.drop(index=df[df.orderTime > endTime].index, inplace=True)  
```
![002](https://github.com/Monster-hash/python-e-commerce-data-analyse/blob/main/picture/002.png)
### 1.2.2提取数据时,处理与业务流程不符合数据、支付时间间隔过长数据
```
# 1.下单时间与支付时间间隔 
df['payinterval'] = (df.payTime-df.orderTime).dt.total_seconds()

# 2.支付时间间隔大于30分钟与支付时间早于下单时间 
df[df.payinterval>1800]
df.drop(index=df[df.payinterval>1800].index, inplace=True)
df.drop(index=df[df.payinterval<0].index, inplace=True)
```
![003](https://github.com/Monster-hash/python-e-commerce-data-analyse/blob/main/picture/003.png)
### 1.2.3提取数据时,处理与业务流程不符合数据,订单金额与支付金额为负
```
# 1.订单金额为负  
df[df.orderAmount < 0]  
# 2.付款金额为负  
df[df.payment < 0]  
# 3.删除相应订单  
df.drop(index=df[df.orderAmount < 0].index, inplace=True) #删除负订单金额  
df.drop(index=df[df.payment < 0].index, inplace=True) #删除负付款金额
```
![004](https://github.com/Monster-hash/python-e-commerce-data-analyse/blob/main/picture/004.png)

