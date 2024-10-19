
#Import
import pandas as pd
import os
import matplotlib.pyplot as plt
from pandas import to_datetime

#main
#1. in ra tap hop gom 12 filepath
path = "D:\HỌC TẬP FTU\sales report"

''' dien gia ro thoi
print(os.listdir(path))
filepaths = []

for file in os.listdir(path):
    filepath = path + "\\" + file
    filepaths.append(filepath)
print(filepaths)

df1 = pd.read_csv(filepaths[2])
print(df1.head(7))
#2. ghep frame 12 file lai
'''
#RESULT
frame = []
for file in os.listdir(path):
    filepath=path+"\\"+file   #lay filepath cua tung file
    dfnumber=pd.read_csv(filepath)  #doc du lieu tung filepath
    frame.append(dfnumber)             #ghep tung du lieu cua filepath vao frame
    result=pd.concat(frame)        #merge frame gan vao result
print(result)

#Add MONTH
'''
print(result['Quantity Ordered'])
print(result['Order Date'])
'''
result=result.dropna(how='all') #loai bo cac dong ko co du lieu
result['Month']=result['Order Date'].str[0:2] #them cot month
result=result[result['Month']!='Or']
print(set(result['Month']))
print(result)


result['Quantity Ordered']=pd.to_numeric(result['Quantity Ordered'],downcast='integer')
result['Price Each']=pd.to_numeric(result['Price Each'],downcast='integer') #chuyen kieu du lieu sang integer
result['Sales']=result['Quantity Ordered']*result['Price Each']
print(result['Sales'])
'''
column_sale=result.pop('Sales')
result.insert(4,'Sales',column_sale)
print(result)
'''
#add SALES
sales_value=result.groupby('Month').sum()['Sales']
print(sales_value)
print(sales_value.max())
'''
months=range(1,13)
plt.bar(x=months, height=sales_value)
plt.xticks(months)
plt.xlabel('Months')
plt.ylabel('Sales by months')
plt.show()
'''
#add CITY
def getcity(address):
    return address.split(',')[1]
result['City']=result['Purchase Address'].apply(getcity)
print(result)

sales_valuecity=result.groupby('City').sum()['Sales']
print(sales_valuecity)
print(sales_valuecity.max())

'''
cities=[city for city,sales in
        sales_valuecity.items()]
print(cities)

plt.bar(x=cities, height=sales_valuecity)
plt.xticks(cities,rotation=90,size=8)
plt.xlabel('City')
plt.ylabel('Sales by city')

plt.show()

'''

#add HOUR
result['Order Date']=pd.to_datetime(result['Order Date'])
result['Hour']=result['Order Date'].dt.hour
print(result['Hour'])

result['Order Date']=pd.to_numeric(result['Order Date'])
'''
sales_valuehour=result.groupby('Hour').sum()['Sales']
print(sales_valuehour)
print(sales_valuehour.max())

hourinchart=[a for a,b in sales_valuehour.items()]
plt.plot(hourinchart, sales_valuehour)
plt.grid(True)
plt.xticks(hourinchart,rotation=90,size=8)
plt.xlabel('Hour un day')
plt.ylabel('Sales by hour')

plt.show()

'''
sales_valuehour=result.groupby('Hour').count()['Sales']
print(sales_valuehour)
print(sales_valuehour.max())
'''
hourinchart=[a for a,b in sales_valuehour.items()]
plt.plot(hourinchart, sales_valuehour)
plt.grid(True)
plt.xticks(hourinchart,rotation=90,size=8)
plt.xlabel('Hour un day')
plt.ylabel('Sales by hour')

plt.show()

'''




