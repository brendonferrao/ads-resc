import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('society.csv')
productivity_scores = data['Productivity_Score']

plt.figure(figsize=(10, 6))
plt.subplot(2, 2, 1)
plt.stem(productivity_scores)
plt.title('Stem-and-Leaf Plot of Productivity Scores')
plt.xlabel('Index')
plt.ylabel('Productivity Score')

plt.subplot(2, 2, 2)
plt.boxplot(productivity_scores)
plt.title('Box Plot of Productivity Scores')
plt.ylabel('Productivity Score')

plt.subplot(2, 2, 3)
plt.hist(productivity_scores, bins=10, color='skyblue', edgecolor='black')
plt.title('Histogram of Productivity Scores')
plt.xlabel('Productivity Score')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
