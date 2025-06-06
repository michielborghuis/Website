v = [1, 2, 3]
M = [[6, 9], [5, 8], [4, 7]]
v2 = [1, 2, 3]
M2 = [[12, 10, 8], [18, 16, 14]]
v3 = [2, 4, 6]
M3 = [[6, 5, 4], [9, 8, 7]]
v4 = [1, 2, 3]
M4 = [[6, 5, 4], [9, 8, 7]]

myv = [1, 2]
mym = [[3, 4, 5, 6], [5, 6, 7, 8]]


def matrix(M, v):
    out = []
    for i in range(0, len(v)):
        for j in range(0, len(M)):
            vec = []
            for k in range(0, len(M[j])):
                vec.append(v[i]*M[j][k])
            print(vec)
            if not out:
                for l in vec:
                    out.append(l)
            else:
                for l in range(0, len(vec)):
                    out[l] += vec[l]
    print(out)

# matrix(M, v)
# matrix(M2, v2)
# matrix(M3, v3)
# matrix(M4, v4)

matrix(mym, myv)
