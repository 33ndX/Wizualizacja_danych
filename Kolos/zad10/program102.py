import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'jajka2024.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the dataframe to understand its structure
data.head()

# It seems like there are some issues with the delimiter and formatting in the CSV file.
# I will attempt to load the file again with a different delimiter and fix the formatting issues.

data = pd.read_csv(file_path, delimiter=';', skipinitialspace=True)

# Display the dataframe again to verify the structure
data.head()

# The data looks better now but still needs some cleaning.
# I will rename the columns and convert the price values to numeric.

data.columns = ['Sklep', 'Gorny_Slask', 'Bydgoszcz', 'Lublin', 'Warszawa', 'Trojmiasto', 'Krakow']

# Replace commas with dots and convert to numeric
for column in data.columns[1:]:
    data[column] = data[column].str.replace(',', '.').astype(float)

# Display the cleaned dataframe
print(data)

melted_data = data.melt(id_vars=['Sklep'], var_name='Miasto', value_name='Cena')

# Create a box plot of prices depending on the city
fig, axs = plt.subplots(1, 2, figsize=(15, 8))

# Boxplot for each city
melted_data.boxplot(column='Cena', by='Miasto', ax=axs[0], grid=False)
axs[0].set_title('Ceny jaj w zależności od miasta')
axs[0].set_xlabel('Miasto')
axs[0].set_ylabel('Cena (PLN)')

# Boxplot for each store
melted_data.boxplot(column='Cena', by='Sklep', ax=axs[1], grid=False)
axs[1].set_title('Ceny jaj w zależności od sklepu')
axs[1].set_xlabel('Sklep')
axs[1].set_ylabel('Cena (PLN)')

plt.tight_layout()
plt.show()