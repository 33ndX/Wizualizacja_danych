import pandas as pd
import numpy as np

# 1. Stwórz jednowymiarową serię danych przechowującą liczby całkowite
int_series = pd.Series([1, 2, 3, 4, 5])
print("\n", int_series)

# 2. Stwórz jednowymiarową serię danych przechowującą stringi
str_series = pd.Series(["a", "b", "c", "d", "e"])
print("\n", str_series)

# 3. Stwórz listę i następnie przekształć ją na serię
list_data = [10, 20, 30, 40, 50]
list_series = pd.Series(list_data)
print("\n", list_series)

# 4. Przekształć jedną z serii stworzonych wcześniej na listę
series_to_list = int_series.tolist()
print("\n", series_to_list)

# 5. Stwórz tablicę jednowymiarową (z biblioteki Numpy) i przekształć ją na serię
np_array = np.array([100, 200, 300, 400, 500])
np_series = pd.Series(np_array)
print("\n", np_series)

# 6. Przekształć jedną z serii stworzonych wcześniej na tablicę (z biblioteki Numpy)
series_to_np_array = str_series.to_numpy()
print("\n", series_to_np_array)

# 7. Wykonaj dodawanie, odejmowanie, mnożenie i dzielenie na dwóch dowolnych seriach danych z indeksami (nazwami)
series_a = pd.Series([1, 2, 3], index=["a", "b", "c"])
series_b = pd.Series([4, 5, 6], index=["a", "b", "c"])
print("Dodawanie:\n", series_a + series_b)
print("Odejmowanie:\n", series_a - series_b)
print("Mnożenie:\n", series_a * series_b)
print("Dzielenie:\n", series_a / series_b)

# 8. Stwórz serię danych przechowującą 10 liczb losowych z przedziału [-10, 10] z krokiem 0.1,
random_series = pd.Series(np.random.uniform(-10, 10, 10))
print("Seria losowych liczb:\n", random_series)

# a) następnie stwórz serię zawierającą liczby ujęte w wcześniej stworzonej serii w tym podpunkcie
sampled_series = random_series.sample(frac=0.5)
print("Próbkowana seria:\n", sampled_series)

# b) Przekształć list, słownik, tablic¡ Numpy oraz serie danych na ramki danych.
my_list = [1, 32, -37, 91, 12, 11, -5]
df_from_list = pd.DataFrame(my_list, columns=['Values'])
print(df_from_list)

my_dict = {'a': [1, 3, 2], 'b': [2, 5, 7], 'c': [3, 4, 8], 'd': [4, 10, 12]}
df_from_dict = pd.DataFrame(my_dict)
print(df_from_dict)

my_array = np.array([[1, 2, 5], [-2, 3, 3], [5, 2, 6]])
df_from_array = pd.DataFrame(my_array, columns=['Col1', 'Col2', 'Col3'])
print(df_from_array)

my_series = pd.Series([1, 32, -37, 91, 12, 11, -5],
                      index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
df_from_series = my_series.to_frame(name='Values')
print(df_from_series)

list_from_df = df_from_list['Values'].tolist()
dict_from_df = df_from_dict.to_dict()
array_from_df = df_from_array.to_numpy()
series_from_df = df_from_series['Values']

# c) Stwórz ramkę danych zgodnie z podanym przykładem
data = {
    'a': [1, 2, 4],
    'b': [2, 3, 8],
    'c': [4, 5, 10],
    'd': [5, 6, 12]
}
df = pd.DataFrame(data, index=['l1', 'l2', 'l3'])
print("Pierwotna ramka danych:\n", df)

# Wyciągnięcie elementów
element = df.loc['l1', 'b']
print("Element [l1, 'b']:\n", element)

# Sortowanie w kolumnie 'b'
df_sorted = df.sort_values(by='b')
print("Posortowana ramka danych według kolumny 'b':\n", df_sorted)

# Zmiana kształtu - pivot
df_pivot = df.melt(id_vars=['a'], value_vars=['b', 'c', 'd'])
print("Ramka danych po zmianie kształtu:\n", df_pivot)
