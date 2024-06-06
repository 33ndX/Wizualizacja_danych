import numpy as np

# Dane ze zdjęcia
wzrost = np.array([153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175])
rozmiar_buta_us = np.array([5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15, 15.5, 16])
liczba_studentow = np.array([1, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66])

# Średni rozmiar buta
sredni_rozmiar_buta = np.mean(rozmiar_buta_us)
print(f"Średni rozmiar buta: {sredni_rozmiar_buta}")

# Maksymalny wymieniony rozmiar buta
maksymalny_rozmiar_buta = np.max(rozmiar_buta_us)
print(f"Maksymalny wymieniony rozmiar buta: {maksymalny_rozmiar_buta}")

# Średni wzrost osób z maksymalnym wymienionym rozmiarem buta
maks_rozmiar_buta_mask = rozmiar_buta_us == maksymalny_rozmiar_buta
sredni_wzrost_maks_rozmiar = np.mean(wzrost[maks_rozmiar_buta_mask])
print(f"Średni wzrost osób z maksymalnym rozmiarem buta: {sredni_wzrost_maks_rozmiar}")

# Najmniejszy wzrost osób z maksymalnym wymienionym rozmiarem buta
najmniejszy_wzrost_maks_rozmiar = np.min(wzrost[maks_rozmiar_buta_mask])
print(f"Najmniejszy wzrost osób z maksymalnym rozmiarem buta: {najmniejszy_wzrost_maks_rozmiar}")

# Średni rozmiar buta u osób każdego wzrostu
unikalne_wzrosty = np.unique(wzrost)
sredni_rozmiar_buta_dla_wzrostu = {height: np.mean(rozmiar_buta_us[wzrost == height]) for height in unikalne_wzrosty}
print("Średni rozmiar buta u osób każdego wzrostu:", sredni_rozmiar_buta_dla_wzrostu)

# Średni wzrost osób
sredni_wzrost = np.mean(wzrost)
print(f"Średni wzrost osób: {sredni_wzrost}")

# Najmniejszy i największy wzrost u osób z rozmiarem buta 10
rozmiar_10_mask = rozmiar_buta_us == 10
najmniejszy_wzrost_rozmiar_10 = np.min(wzrost[rozmiar_10_mask])
najwiekszy_wzrost_rozmiar_10 = np.max(wzrost[rozmiar_10_mask])
print(f"Najmniejszy wzrost u osób z rozmiarem buta 10: {najmniejszy_wzrost_rozmiar_10}")
print(f"Największy wzrost u osób z rozmiarem buta 10: {najwiekszy_wzrost_rozmiar_10}")

# Tablica zawierająca europejski rozmiar butów
rozmiar_buta_eu = rozmiar_buta_us + 33
print("Europejski rozmiar butów:", rozmiar_buta_eu)
