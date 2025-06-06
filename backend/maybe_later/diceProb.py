import random



def roll6():
    a = random.randrange(0, 2)
    if a == 0:
        return roll2()
    else:
        return 6

def roll5():
    a = random.randrange(0, 2)
    if a == 0:
        return 4
    else:
        return 5

def roll4():
    a = random.randrange(0, 2)
    if a == 0:
        return 2
    else:
        return 3

def roll3():
    a = random.randrange(0, 2)
    if a == 0:
        return roll1()
    else:
        return 1

def roll2():
    a = random.randrange(5, 7)
    if a == 5:
        return roll5()
    else:
        return roll6()

def roll1():
    a = random.randrange(3, 5)
    if a == 3:
        return roll3()
    else:
        return roll4()

def roll0():
    a = random.randrange(1, 3)
    if a == 1:
        return roll1()
    else:
        return roll2()

ran = 1000000
lst = []
for i in range(ran):
    lst.append(roll0())

a1 = lst.count(1)
a2 = lst.count(2)
a3 = lst.count(3)
a4 = lst.count(4)
a5 = lst.count(5)
a6 = lst.count(6)

print(int(a1/ran*1000))
print(int(a2/ran*1000))
print(int(a3/ran*1000))
print(int(a4/ran*1000))
print(int(a5/ran*1000))
print(int(a6/ran*1000))