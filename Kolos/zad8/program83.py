import numpy as np

country = np.array(['China', 'Japan', 'Gremany', 'USA', 'South Korea', 'India', 'Brazil', 'Mexico', 'Spain', 'Russia'])
_1999 = np.array([0.56, 8.1, 5.3, 5.63, 2.63, 0.53, 1.1, 0.99, 2.28, 0.94])
_2014 = np.array([19.91, 8.27, 5.6, 4.25, 4.12, 3.12, 2.31, 1.91, 1.89, 1.69])

for i in range(0, len(country)):
    print(f'Country: {country[i]} {(_2014[i]/_1999[i])*100}%')

max_value = np.max(_1999)
min_value = np.min(_1999)

for i in range(0, len(country)):
    if _2014[i] < _1999[i]:
        print(country[i])
