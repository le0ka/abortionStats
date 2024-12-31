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



# Scatter plot part
x = abortData['% Yes']
y = incomeData['Annual_Wage']

plt.scatter(x, y)
plt.title('Pecentage of "Yes" on 3 Votes and Average Income per MO County')
plt.xlabel('Percentage of County that voted "Yes" on Amendment 3')
plt.ylabel('Average Income of County')
plt.grid(True)
plt.show()

# r coefficent
r, _ = pearsonr(x, y)
print(r)
