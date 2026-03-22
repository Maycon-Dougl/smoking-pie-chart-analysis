import pandas as pd
import matplotlib.pyplot as plt
#load dataset from github
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)
#value_count:
resumo = df["smoker"].value_counts()
#generate a pie chart
plt.pie(resumo.values, labels=resumo.index, autopct='%1.1f%%')
#create title name:smokers vs non-smokers
plt.title("Smokers vs Non-Smokers")
#show chart
plt.show()