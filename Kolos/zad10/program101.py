import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

filename = 'jajka2024.csv'
data = np.genfromtxt(filename, delimiter=';', dtype=None, encoding='utf-8', skip_header=1)

# Wyciągnięcie nagłówków (nazwy miast)
with open(filename, 'r', encoding='utf-8') as f:
    headers = f.readline().strip().split(';')[1:]

# Wyciągnięcie nazw sieci i cen
networks = data[:, 0]
prices_str = data[:, 1:]

# Zamiana przecinków na kropki oraz pustych wartości na NaN
prices_str = np.char.replace(prices_str, ',', '.')
prices_str[prices_str == ''] = 'nan'

# Konwersja na typ float
prices = prices_str.astype(float)

# Obliczenie średniej ceny wszystkich jajek
average_price = np.nanmean(prices)
print(f'{average_price:.2f} PLN')

# Znalezienie miasta i sieci z najtańszymi i najdroższymi jajkami
min_price_index = np.nanargmin(prices)
max_price_index = np.nanargmax(prices)

print(min_price_index)

# Znalezienie miasta i sieci z najtańszymi i najdroższymi jajkami
min_price_index = np.nanargmin(prices)
max_price_index = np.nanargmax(prices)

min_price_city, min_price_network = np.unravel_index(min_price_index, prices.shape)
max_price_city, max_price_network = np.unravel_index(max_price_index, prices.shape)

print(f"Najtańsze jajka są w mieście {headers[min_price_city]} w sieci {networks[min_price_network]} za {prices[min_price_network, min_price_city]} PLN")
print(f"Najdroższe jajka są w mieście {headers[max_price_city]} w sieci {networks[max_price_network]} za {prices[max_price_network, max_price_city]} PLN")

# Zapisanie wyników jako dwuwymiarowa tablica
results = np.array([
    (headers[min_price_city], networks[min_price_network]),
    (headers[max_price_city], networks[max_price_network])
], dtype=[('Miasto', 'U50'), ('Siec', 'U50')])

print("Wynikowa tablica z par (Miasto, nazwa sieci):")
print(results)