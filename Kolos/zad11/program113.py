import seaborn as sns
import matplotlib.pyplot as plt

# Wczytanie danych
iris = sns.load_dataset("iris")

# Wykresy zależności punktowej
sns.scatterplot(data=iris, x='sepal_length', y='sepal_width', hue='species')
plt.title('Sepal Length vs. Sepal Width')
plt.show()

sns.scatterplot(data=iris, x='petal_length', y='petal_width', hue='species')
plt.title('Petal Length vs. Petal Width')
plt.show()

# Wykresy catplot
sns.catplot(data=iris, x='species', y='sepal_length', kind='box')
plt.title('Sepal Length by Species')
plt.show()

sns.catplot(data=iris, x='species', y='sepal_width', kind='box')
plt.title('Sepal Width by Species')
plt.show()

sns.catplot(data=iris, x='species', y='petal_length', kind='box')
plt.title('Petal Length by Species')
plt.show()