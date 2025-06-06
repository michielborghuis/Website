lst = []
for a in range(100):
    for b in range(100):
        number = a*a + b*b
        if number not in lst:
            lst.append(number)

lst2 = []
for i in range(lst[-1]):
    if i not in lst:
        lst2.append(i)

for i in lst2:
    print(i,end=', ')