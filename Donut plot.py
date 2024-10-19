'''
This is a donut delivery process of a company:
1. How many late delivery until the present?
2. The reason and how many percentage they account for, causing the late delivery?
3. Show the chart visualizing makes it easy to analyse, and solve th eproblem based on which priority first?
'''


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import datetime

df= pd.read_csv("D:\\donut.csv", index_col = 0)
print('{:,} lines'.format(len(df)))
print(df)


df_late = df[(df['Last Status']== 'Delivery Time') & (df['Reason Code'] != '')].copy()
print(df_late)
df_late = pd.DataFrame(df_late.groupby(['Reason Code'])['#Shipment'].nunique())
print(df_late)

my_circle = plt.Circle( (0,0), 0.5, color='white')

ax = df_late.plot.pie(figsize=(10, 10),
                      y='#Shipment'
                      , legend= False, fontsize = 14, colormap='Paired', autopct='%1.1f%%', explode=(0.05, 0.05, 0.05,
                                                                                                     0.05, 0.05))
plt.title('{:,} shipments delivered with delay by reason code'.format(df_late['#Shipment'].sum()), fontsize = 14)
plt.axis('off')
p = plt.gcf()
p.gca().add_artist(my_circle)
plt.show()






