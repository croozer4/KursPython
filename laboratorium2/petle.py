# Zadanie 1
print ("Zadanie 1")

studenci = ['Przystalski', 'Kowalska', 'Bolito', 'Wozniak', 'Kowalski', 'Nowak'] 

for student in studenci:
    print(student)

# Zadanie 2
print ("Zadanie 2")

szukany_student = 'Kowalski'

for student in studenci:
    if student == szukany_student:
        print(f'Student {szukany_student} został znaleziony na liście.')
        break

# Zadanie 3
print ("Zadanie 3")

szukany_student = 'Mazurek'

for student in studenci:
    if student == szukany_student:
        print(f'Student {szukany_student} został znaleziony na liście.')
        break
else:
    print(f'Student {szukany_student} nie został znaleziony na liście.')
