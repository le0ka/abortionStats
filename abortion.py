import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import pearsonr

abortion_csv = pd.read_csv("./abortion.csv")
income_csv = pd.read_csv("./income_clean.csv")

abortData = pd.DataFrame(abortion_csv)
incomeData = pd.DataFrame(income_csv)

most_pro_choice = abortData["% Yes"].max()
most_income = incomeData["Annual_Wage"].max()

most_pro_choice_sorted = abortData.sort_values(by='% Yes')
most_income_sorted = incomeData.sort_values(by='Annual_Wage')

# Scatter plot part

x = abortData['% Yes']
y = incomeData['Annual_Wage']

plt.scatter(x, y)
plt.title('Scatterplot of df1 vs df2')
plt.xlabel('df1 values')
plt.ylabel('df2 values')
plt.grid(True)
plt.show()

# r coefficent
#r, _ = pearsonr(x, y)
#print(r)