import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import mplcursors
import numpy as np

#reading data
df_2021 = pd.read_excel("2021_disposal_rates_munis.xlsx")
#prediction model
df_2021["Predicted_Recycle_Rate"] = (6.3004224e-06 * df_2021["POPULATION\n"]) + 0.0034237
#weighing data
df_2021["Weighted Recycling Rate"] = (df_2021["Recycled %"] * 100 * df_2021["POPULATION\n"]) / df_2021["POPULATION\n"].sum()
#making it clickable
matplotlib.use("TkAgg")
#graph prediction data
plt.figure()
scatter = plt.scatter(df_2021["POPULATION\n"], df_2021["Predicted_Recycle_Rate"], color="red")
plt.xlabel("Population")
plt.ylabel("Recycle Rate")
plt.title("2021 Predicted Recycle Rate in NJ based on 2017 Recycle Rate in NJ")
#getting city names
cities = []
for city in df_2021["MUNICIPALITY"]:
    cities.append(city)
#make it hover able
cursor = mplcursors.cursor(scatter, hover=True)
cursor.connect("add", lambda sel: sel.annotation.set_text(cities[sel.index]))
#print correlation for predicted recycle rate and graph
r = np.corrcoef(df_2021["POPULATION\n"], df_2021["Predicted_Recycle_Rate"])
print(r[0, 1])
plt.show()
#graph actual data
plt.figure()
scatter2 = plt.scatter(df_2021["POPULATION\n"], df_2021["Weighted Recycling Rate"], color="green")
plt.xlabel("Population")
plt.ylabel("Recycle Rate")
plt.title("2021 Recycle Rate in NJ")
#make it hoverable
cursor2 = mplcursors.cursor(scatter2, hover=True)
cursor2.connect("add", lambda sel: sel.annotation.set_text(cities[sel.index]))
plt.show()
#print correlation for predicted recycle rate
r2 = np.corrcoef(df_2021["POPULATION\n"], df_2021["Weighted Recycling Rate"])
print(r2[0, 1])
