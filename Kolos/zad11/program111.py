import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Wczytanie danych
penguins = pd.read_csv('penguins.csv')

# Średnia waga w każdej płci
mean_weight_sex = penguins.groupby('sex')['body_mass_g'].mean()

# Średnia waga z podziałem na płeć i gatunek
mean_weight_sex_species = penguins.groupby(['sex', 'species'])['body_mass_g'].mean()

print(mean_weight_sex)
print('\n\n\n', mean_weight_sex_species)

# Pingwiny z największą i najmniejszą wagą

max_weight_penguin = penguins.loc[penguins['body_mass_g'].idxmax()]
min_weight_penguin = penguins.loc[penguins['body_mass_g'].idxmin()]

print(max_weight_penguin)
print(min_weight_penguin)

# Ilość pingwinów każdego gatunku na każdej wyspie
penguin_count_species_island = penguins.groupby(['species', 'island']).size()

print(penguin_count_species_island)

# Ilość pingwinów gatunku 'Adelie' na każdej wyspie
adelie_count_island = penguins[penguins['species'] == 'Adelie'].groupby('island').size()

print(adelie_count_island)

# Normalizacja wartości w kolumnie 'sex' na małe litery i usunięcie NaN
penguins['sex'] = penguins['sex'].str.lower()
penguins = penguins.dropna(subset=['sex'])

# Słowniki do kolorów i kształtów
species_shapes = {'Adelie': 'o', 'Chinstrap': 's', 'Gentoo': 'D'}
colors = {'male': 'blue', 'female': 'red'}

plt.figure()

for species in penguins['species'].unique():
    species_data = penguins[penguins['species'] == species]
    for sex in species_data['sex'].unique():
        sex_data = species_data[species_data['sex'] == sex]
        plt.scatter(sex_data['bill_length_mm'], sex_data['bill_depth_mm'],
                    s=sex_data['body_mass_g'] / 2000 * 100, #tutaj trzeba zmienic jakos wielkosc punktow
                    c=colors[sex],
                    label=f'{species} ({sex})',
                    marker=species_shapes[species])

plt.xlabel('Bill Length (mm)')
plt.ylabel('Bill Depth (mm)')
plt.title('Bill Length vs. Bill Depth by Species and Sex')
plt.legend()
plt.show()
