from decimal import Decimal
import random

def ratio(rng):
    lst = [1, 1]
    count = 0
    for i in range(rng):
        if i != 0:
            count += 1
        a = random.randrange(0, 2)
        if a == 0:
            lst.append(lst[count+1] + lst[count])
        else:
            lst.append(lst[count + 1] - lst[count])
        if len(lst) > 10000:
            del lst[:5000]
            count -= 5000
    return abs(lst[-1])**(1/Decimal(len(lst)))


print(ratio(20000))