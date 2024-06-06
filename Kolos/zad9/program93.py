
f = open('tekst1.txt', 'r+', encoding='utf-8')
s = f.read()
print(s)
print(type(s))
f.close()

# Użycie konstrukcji with do obsługi plików
with open('tekst1.txt', 'r+', encoding='utf-8') as f:
    s = f.read()
    print(s)
    print(type(s))

# Przykład z kodowaniem 'utf-8'
with open('tekst1.txt', 'r+', encoding='utf-8') as f:
    s = f.read()
    print(s)

# Przykład z kodowaniem 'latin-1'
with open('tekst1.txt', 'r+', encoding='latin-1') as f:
    s = f.read()
    print(s)
