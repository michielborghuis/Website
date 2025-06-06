from itertools import permutations


perm = permutations(['N', 'A', 'T', 'H', 'A', 'N', 'D', 'E', 'M', 'L'])
counter = 0
for i in list(perm):
    counter += 1
print(counter)