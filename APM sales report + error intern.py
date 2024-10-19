'''
This is a sales report of APM Springs product: OEM, REM, report in 2022,2023
1. Which months does have the highest sales? 2023: April, 2022: May ==> January in total
2. Which months does have the highest revenue? 2023: April, 2022: January ==> March in total
3. Calculate Bias, MAE, MAPE, RMSE: quarter, products --> show the error, calculate the accuracy and bias of the demand forecast 
'''

import pandas as pd
import os
import matplotlib.pyplot as plt

path = "D:\\APM Python report sales 2223.xlsx"
df = pd.read_excel(path)
print(df)

df['Sales']=df['S_OEM']+df['S_REM']+df['S_Export']
df['Revenue']=df['R_OEM']+df['R_REM']+df['R_Export']
df['Forecast']=df['F_OEM']+df['F_REM']+df['F_Export']

print(df)

a=2023
print('In year: ', a)
maxR=df.loc[df['Year'] == a,'Revenue'].max()
maxS=df.loc[df['Year'] == a,'Sales'].max()
maxF=df.loc[df['Year'] == 2023,'Forecast'].max()

maxRmonth = df.loc[df['Revenue'] == maxR, 'Month'].values[0]
maxSmonth = df.loc[df['Sales'] == maxS, 'Month'].values[0]
maxFmonth = df.loc[df['Forecast'] == maxF, 'Month'].values[0]

print('max revenue in month:',maxRmonth,':',maxR)
print('max sales in month:',maxSmonth,':',maxS)
print('max forecast in month:',maxFmonth,':',maxF)

s_value=df.groupby('Month').sum()['Sales']
r_value=df.groupby('Month').sum()['Revenue']
f_value=df.groupby('Month').sum()['Forecast']
print(s_value,r_value,f_value)


s_value_df = s_value.reset_index()
r_value_df = r_value.reset_index()
f_value_df = f_value.reset_index()


Monthr = r_value_df.loc[r_value_df['Revenue'] == r_value.max(), 'Month'].values[0]
Months = s_value_df.loc[s_value_df['Sales'] == s_value.max(), 'Month'].values[0]
Monthf = f_value_df.loc[f_value_df['Forecast'] == f_value.max(), 'Month'].values[0]


print('The sum all value each criteria: revenue, sale, forecast max in', Monthr, Months, Monthf, r_value.max(), s_value.max(), f_value.max())


Average_sale=df.loc[df['Year'] == a,'Sales'].mean()


df['Error'] = df['Forecast'] - df['Sales']
bias = df['Error'].mean()

print(f"Forecast Bias: {bias:.2f}")
print(f"Forecast Bias Per: {bias/Average_sale*100:.2f}%")

df['Absolute Error'] = abs(df['Error'])
mae = df['Absolute Error'].mean()
print(f"Mean Absolute Error (MAE): {mae:.2f}")
mae1=mae/Average_sale*100
print(f"Mean Absolute Error Per(MAE%): {mae1 :.2f}%")

df['Absolute Percentage Error'] = ((df['Absolute Error']) / df['Sales']) * 100
mape = df['Absolute Percentage Error'].mean()
print(f"Mean Absolute Percentage Error (MAPE): {mape:.2f}%")

df['Squared Error'] = (df['Error']) **2
rmse = (df['Squared Error'].mean()) **0.5
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"Root Mean Squared Error Per(RMSE%): {rmse/Average_sale*100:.2f}%")

print(df)
