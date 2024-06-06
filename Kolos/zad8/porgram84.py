import numpy as np

# Dane
imiona = np.array(['Anna', 'Zofia', 'Sylwia', 'Katarzyna', 'Teresa', 'Tomasz', 'Cezary', 'Zenon', 'Filip', 'Adrian'])
wiek = np.array([21, 40, 23, 31, 34, 19, 13, 28, 20, 15])
plec = np.array(['K', 'K', 'K', 'K', 'K', 'M', 'M', 'M', 'M', 'M'])
waga = np.array([65, 80, 64, 69, 74, 61, 66, 90, 60, 77])
wzrost = np.array([179, 179, 151, 177, 157, 180, 151, 190, 160, 160])
okulary = np.array(['NIE', 'TAK', 'NIE', 'TAK', 'NIE', 'NIE', 'NIE', 'TAK', 'NIE', 'TAK'])

# 1. Wypisz na konsoli imiona posortowane alfabetycznie
imiona_sortowane = np.sort(imiona)
print("Imiona posortowane alfabetycznie:", imiona_sortowane)

# 2. Stwórz tablicę przechowującą imiona osób noszących okulary
imiona_okulary = imiona[okulary == 'TAK']
print("Imiona osób noszących okulary:", imiona_okulary)

# 3. Stwórz tablicę zawierającą imiona kobiet w wieku z przedziału lat [20, 30]
imiona_kobiety_20_30 = imiona[(plec == 'K') & (wiek >= 20) & (wiek <= 30)]
print("Imiona kobiet w wieku z przedziału [20, 30]:", imiona_kobiety_20_30)

# 4. Stwórz tablicę zawierającą imiona osób o wadze z przedziału [60, 80], wzroście [160, 180] nienoszących okularów
imiona_kryteria = imiona[(waga >= 60) & (waga <= 80) & (wzrost >= 160) & (wzrost <= 180) & (okulary == 'NIE')]
print("Imiona osób o wadze [60, 80] i wzroście [160, 180] nienoszących okularów:", imiona_kryteria)

# 5. Policz BMI dla wszystkich osób i wynik zapisz w tablicy (bmi = waga / wzrost^2)
bmi = waga / (wzrost / 100) ** 2
print("BMI wszystkich osób:", bmi)

# 6. Policz średni wiek i wyświetl na konsoli imię osoby najbliżej średniej
sredni_wiek = np.mean(wiek)
najblizszy_sredniej_index = np.argmin(np.abs(wiek - sredni_wiek))
najblizszy_sredniej_imie = imiona[najblizszy_sredniej_index]
print(f"Średni wiek: {sredni_wiek:.2f}")
print(f"Osoba najbliżej średniego wieku: {najblizszy_sredniej_imie}")






# imiona = np.array(['Anna', 'Zofia', 'Sylwia', 'Katarzyna', 'Teresa', 'Tomasz', 'Cezary', 'Zenon', 'Filip', 'Adrian'])
# wiek = np.array([21, 40, 13, 31, 34, 14, 13, 28, 20, 15])
# sex = np.array(['K', 'K', 'K', 'K', 'K', 'M', 'M', 'M', 'M', 'M'])
# waga = np.array([65, 80, 64, 69, 74, 61, 66, 61, 69, 77])
# wzorst = np.array([179, 179, 151, 177, 170, 157, 151, 153, 160, 160])
# okulary = np.array(['NIE', 'TAK', 'NIE', 'TAK', 'NIE', 'TAK', 'NIE', 'TAK', 'NIE', 'TAK'])
#
# def alfabetycznie():
#     imiona.sort()
#     for i in range(len(imiona)):
#         print(imiona)
# # alfabetycznie()
#
#
# okularyTak = np.array([])
# for i in range(0, len(imiona)):
#     if okulary[i] == 'TAK':
#         okularyTak = np.append(okularyTak, imiona[i])
# print(okularyTak)
#
#
# kobietyPo20 = np.array([])
# for i in range(0, len(imiona)):
#     if sex[i] == 'K':
#         if wiek[i] in range(20, 31):
#             kobietyPo20 = np.append(kobietyPo20, imiona[i])
# print(kobietyPo20)
#
# array4 = np.array([])
# for i in range(0, len(imiona)):
#     if waga[i] in range(60, 81) and wzorst[i] in range(160, 181) and okulary[i] == 'NIE':
#             array4 = np.append(array4, imiona[i])
# print(array4)
#
# def bmi(weight, height):
#     result = weight / (height * height)
#     return result
#
# array_bmi = np.array([])
# for i in range(0, len(imiona)):
#     array_bmi = np.append(array_bmi, bmi(waga[i], wzorst[i]))
# print(array_bmi)

