import random
import copy

unlst = []

for i in range(100):
    unlst.append(random.randrange(1, 100))

unlstcopy = unlst.copy()
unlstcopysorted = sorted(unlstcopy)


def sort(lst, rng):
    fullysorted = True
    for i in range(rng - 1):
        if lst[i] > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
            fullysorted = False
    if fullysorted == True:
        return True
    else:
        return lst


def go(lst):
    for i in range(len(lst)):
        print(lst)
        ans = sort(lst, len(lst))
        if ans == True:
            return lst


endlst = go(unlst)

print("\n\n\n\n\n")
print(endlst)
print(unlstcopy)
print(unlstcopysorted)
if endlst == unlstcopysorted:
    print("jaaaa")
