## 2. Introduction To The Data ##

import pandas as pd
df = pd.read_csv("unrate.csv")
df['DATE'] = pd.to_datetime(df['DATE'])
unrate =df

unrate.head(12)

## 6. Introduction to Matplotlib ##

import matplotlib.pyplot as plt
plt.plot() 
plt.show()

## 7. Adding Data ##

import matplotlib.pyplot as plt
x_value = unrate['DATE'].head(12)
y_value = unrate['VALUE'].head(12)


plt.plot(x_value,y_value) 
plt.show()

## 8. Fixing Axis Ticks ##

import matplotlib.pyplot as plt

x_value = unrate['DATE'].head(12)
y_value = unrate['VALUE'].head(12)
plt.xticks(rotation=90) 
plt.plot(x_value,y_value) 
plt.show()


## 9. Adding Axis Labels And A Title ##

import matplotlib.pyplot as plt

x_value = unrate['DATE'].head(12)
y_value = unrate['VALUE'].head(12)
plt.xticks(rotation=90) 
plt.xlabel("Month")
plt.ylabel("Unemployment Rate")
plt.title("Monthly Unemployment Trends, 1948")

plt.plot(x_value,y_value) 
plt.show()
