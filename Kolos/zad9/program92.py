import pandas as pd

#Dane-----------
df1 = pd.DataFrame([[2942, 9840, 2794, 8891, 8111, 2933, 8301, 9125],
                    [ 'Sylwia', 'Katarzyna', 'Teresa', 'Tomasz', 'Cezary', 'Zenon', 'Filip', 'Adrian'],
                    [13, 31, 34, 14, 13, 28, 20, 15]]).T
df1.columns = ['ID', 'Name', 'Age']

weight = [65, 80, 64, 69, 74, 61, 66, 61]
height = [179, 179, 151, 177, 170, 157, 151, 153]
glasses = [False, True, False, True, False, True, False, True]

df2 = pd.DataFrame([[2312, 2336, 2942, 9840, 2794, 8891, 8111, 2933],
['Anna', 'Zofia', 'Sylwia', 'Katarzyna', 'Teresa', 'Tomasz', 'Cezary', 'Zenon'],
weight, height, glasses]).T

df2.columns = ['ID', 'Name', 'W', 'H', 'Gl']
#Dane-----------

# Połączenie tabel metodą inner
df0 = pd.merge(df1, df2, on=['ID', 'Name'], how='inner')
print(df0)

# Połączenie tabel metodą outer, dodaje rowniez z pustymi polami
df_outer = pd.merge(df1, df2, on=['ID', 'Name'], how='outer')
# print('\n', df_outer)

# Sortowanie imion alfabetycznie
df_sorted = df1.sort_values(by='Name', ascending=True)
# print(df_sorted)

# Tablica z imionami osób noszących okulary
df_glasses = df2[df2['Gl'] == True][['Name']]
# print(df_glasses)

# Tablica z imionami osób w wieku 20-30
df_age_20_30 = df1[(df1['Age'] >= 20) & (df1['Age'] <= 30)][['Name']]
print(df_age_20_30)

# Dodanie kolumny z BMI
df2['BMI'] = df2['W'] / (df2['H'] / 100) ** 2

# Obliczanie średniego wieku
average_age = df1['Age'].mean()

# Obliczanie średniego BMI osób noszących i nienoszących okulary
average_bmi_with_glasses = df2[df2['Gl'] == True]['BMI'].mean()
average_bmi_without_glasses = df2[df2['Gl'] == False]['BMI'].mean()
print('average_bmi_with_glasses', average_bmi_with_glasses)

average_age_with_glasses = df0[df0['Gl'] == True]['Age'].mean()
average_age_without_glasses = df0[df0['Gl'] == False]['Age'].mean()
print('average_age_with_glasses', average_age_without_glasses)

print(df0)