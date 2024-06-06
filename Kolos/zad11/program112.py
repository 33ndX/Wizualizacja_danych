import seaborn as sns
import matplotlib.pyplot as plt

# Wczytanie danych
penguins = sns.load_dataset("penguins")

# Normalizacja wartości w kolumnie 'sex' na małe litery i usunięcie NaN
penguins['sex'] = penguins['sex'].str.lower()
penguins = penguins.dropna(subset=['sex'])

sns.scatterplot(data=penguins, x='bill_length_mm', y='bill_depth_mm',
                hue='sex', size='body_mass_g', style='species',
                palette='deep', sizes=(20, 200))

plt.xlabel('Bill Length (mm)')
plt.ylabel('Bill Depth (mm)')
plt.title('Bill Length vs. Bill Depth by Species and Sex')
plt.legend()
plt.show()
