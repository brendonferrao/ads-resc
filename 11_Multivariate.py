import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

data = pd.read_csv('society.csv')

plt.figure(figsize=(10,6))
plt.subplot(2, 2, 1)
grouped_data = data.groupby('Gender')['Income'].mean().reset_index()
plt.bar(grouped_data['Gender'], grouped_data['Income'], color=['blue', 'pink','yellow'])
plt.title('Grouped Bar Plot of Average Income by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Income')

plt.subplot(2, 2, 2)
plt.scatter(data['Age'], data['Income'], color='blue', alpha=0.5)
plt.title('Scatter Plot of Age vs Income')
plt.xlabel('Age')
plt.ylabel('Income')

plt.subplot(2, 2, 3)
plt.scatter(data['Age'], data['Income'], s=data['Productivity_Score']*50, alpha=0.5)
plt.title('Bubble Chart of Age vs Income')
plt.xlabel('Age')
plt.ylabel('Income')

plt.subplot(2, 2, 4)
plt.plot(data['ID'], data['Income'], marker='o', linestyle='-')
plt.title('Run Chart of Income')
plt.xlabel('ID')
plt.ylabel('Income')

plt.tight_layout()
plt.show()

plt.figure(figsize=(10,3))
sns.scatterplot(x='Age', y='Income', hue='Gender', size='Productivity_Score', data=data)
plt.title('Multivariate Chart of Age vs Income')
plt.xlabel('Age')
plt.ylabel('Income')
plt.grid(True)
plt.show()

plt.figure(figsize=(5,3))
numeric_data = data.select_dtypes(include=['int64', 'float64'])
numeric_data.drop(columns=['ID'], inplace=True)
correlation_matrix = numeric_data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Heatmap of Correlation Matrix')
plt.show()
