import random

def fibo(x):
    fibonaci_secuence = [1, 1]
    counter = 0

    for i in range(x):
        fibonaci_secuence.append(fibonaci_secuence[-1] + fibonaci_secuence[-2])
        counter += 1
        golden_ratio = fibonaci_secuence[-1] / fibonaci_secuence[-2]
        print('golden ratio: ' + str(golden_ratio))
        if golden_ratio == 1.618033988749895:
            print(counter)
            break
#fibo(100)

def fibo2(x):
    fibonaci_secuence = [1, 1]
    counter = 0
    for i in range(x):
        plus_or_min = random.randrange(1, 3)
        if plus_or_min == 1:
            fibonaci_secuence.append(fibonaci_secuence[-1] + fibonaci_secuence[-2])
        else:
            fibonaci_secuence.append(fibonaci_secuence[-1] - fibonaci_secuence[-2])
        counter += 1
    vinwath_last = fibonaci_secuence[-1]
    vinwath_lastlast = fibonaci_secuence[-2]
    if vinwath_last < 0:
        vinwath_last = 0 - vinwath_last
    if vinwath_lastlast < 0:
        vinwath_lastlast = 0 - vinwath_lastlast
    vinwath = vinwath_last / vinwath_lastlast
    print(vinwath)

fibo2(400000)

def fibonaci(index):
    if index == 0:
        return 1
    elif index == 1:
        return 1
    else:
        return fibonaci(index-1) + fibonaci(index-2)

#fibonaci(10)