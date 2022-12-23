import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

path= "/home/mrov/Scrapy/scrapy/autoAm/autosAm/autosAm/all_data.csv"


if not os.path.exists():
    print("Error with loading file")

df=pd.read_csv("all_data.csv")
print(df.head())

numericDf = df.select_dtypes(include=np.number)

numericDf.plot(kind='scatter',x='mileage',y='price')
plt.show()

groupingDf=df.groupby("year")
print(numericDf.corr(method='pearson'))
prices=df["price"]
prices.plot()
plt.show()

print("The maximum price is ",df["price"].max())
print("The minimum price is ",df["price"].min())

print("The maximum mileage is ",df["mileage"].max())
print("The minimum mileage is",df["mileage"].min())

print("On 2017 year prices are ")
print(df[df['year']=="2017"]['price'])