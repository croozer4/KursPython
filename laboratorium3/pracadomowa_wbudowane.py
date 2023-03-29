# zadanie 1

l = ['1', 2, '3', 4, 5, '-1', '-2', -3, '-4', '-5']

l = list(filter(lambda x: type(x) != str, l))
l = list(filter(lambda x: x >= 0, l))

suma = sum(l)
print("Suma pozostałych", suma)

# zadanie 2

a = ['abba', 'queen', 'acdc', 'soad']
b = [1988, 1981, 1973, 1999]

c = list(zip(a, b))
c.sort(key=lambda x: x[1])
print(list(map(lambda x: x[0], c)))
