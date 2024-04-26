import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

data=pd.read_csv('society.csv')

numerical_data = data['Age']
categorical_data = data['Gender']
qualitative_data = data['Education']
quantitative_data = data['Income']

plt.figure(figsize=(10, 6))
plt.subplot(2, 2, 1)
sns.kdeplot(numerical_data,fill=True, color='blue')
plt.title('Density Plot of Numerical Data')
plt.xlabel('Age')
plt.ylabel('Density')
plt.grid(True)

plt.subplot(2, 2, 2)
categories, counts = categorical_data.value_counts().index, categorical_data.value_counts().values
plt.pie(counts, labels=categories, autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart for analysis of Gender')
plt.axis('equal')

plt.subplot(2, 2, 3)
plt.fill_between(range(len(quantitative_data)), quantitative_data, color="skyblue", alpha=0.4)
plt.plot(quantitative_data, color="Slateblue", alpha=0.6)
plt.title('Area Chart of Income')
plt.xlabel('ID')
plt.ylabel('Income')
plt.grid(True)

plt.subplot(2, 2, 4)
category_counts = pd.Series(qualitative_data).value_counts()
category_counts.plot(kind='bar', color='skyblue')
plt.title('Distribution of Education')
plt.xlabel('Education')
plt.ylabel('No. of Users')
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()
