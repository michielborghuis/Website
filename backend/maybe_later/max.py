myv = [1, 2, 3]
mym = [[12, 10, 8], [18, 16, 14]]

def matrix_product(M, v):
    mlst = list(M)
    vlst = list(v)
    antlst = []
    if len(M[0]) == len(v):
        for i in range(len(M[0])):
            antlst.append(0)
        j = -1
        for lst in M:
            c = 0
            j += 1
            for item in lst:
                som = item * v[c]
                antlst[j] += som
                c += 1
    return antlst

print(matrix_product(mym, myv))