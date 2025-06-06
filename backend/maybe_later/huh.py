import numpy as np

M = [[18, -14], [-7, 16], [-18, 10]]
N = [[2, 13, 8], [6, 11, -11]]

M1 = [[6, 5, 4], [9, 8, 7]]
N1 = [[6, 5, 4], [9, 8, 7]]
M2 = [[6, 5, 4], [9, 8, 7]]
N2 = [[4, 0], [4, 5], [8, 3]]
M3 = [[6, 5, 4], [9, 8, 7]]
N3 = [1, 2, 3]
M4 = [[ 0.5,  0.2,  0.0,   0.0,  -0.2], [ 0.2, -0.5, -0.1,  0.9, -0.8], [ 0.0,   0.2,  0.0,   0.1, -0.1], [ 0.1,  0.8,  0.3,  0.0,  -0.7]]
N4 = [[ 0.5,  0.2, -0.1,  0.9], [ 0.2, -0.5,  0.3,  0.1]]

# def shape(a, b):
#     if type(b) != list:
#         return 'dimError'
#     shape1 = np.shape(a)
#     shape2 = np.shape(b)
#     try:
#         if not shape2[1]:
#             return 'vector'
#         elif shape1[1] == shape2[0]:
#             return 'matrix_normal'
#         elif shape1[0] == shape2[1]:
#             return 'matrix_flipped'
#     except:
#         try:
#
#
# print(shape(M4, N4))
# print(shape(M2, N2))
# print(shape(1, 2))
# print(np.shape(M3))
# print(shape(M3, N3))


# def matrix_productV(M: np.ndarray, v: np.ndarray):
#     if len(M[0]) == len(v):
#         out = []
#         for i in range(0, len(v)-1):
#             out.append(0)
#         count = 0
#         for j in M:
#             count2 = 0
#             for k in j:
#                 ans = k * v[count2]
#                 out[count] += ans
#                 count2 += 1
#             count += 1
#         return np.array(out)
#     else:
#         return "Helaas"


def matrix_product(M: np.ndarray, N: np.ndarray):
    try:
        test = len(N[0])
        lenn = len(N)
        lennzero = len(N[0])
    except:
        lenn = len(N)
        lennzero = 1
    if len(M[0]) == lenn:
        result = []
        for a in range(0, len(M)):
            horizontal = []
            for b in range(0, lennzero):
                horizontal.append(0)
            result.append(horizontal)

        for i in range(len(M)):
            for j in range(lennzero):
                for k in range(lenn):
                    result[i][j] += M[i][k] * N[k][j]

        return np.array(result)
    else:
        return "Helaas"



# print('M,N')
# print(matrix_product(M, N))
# print('\n\n')
# print('M1,N1')
# print(matrix_product(M1, N1))
# print('\n\n')
# print('M2,N2')
# print(matrix_product(M2, N2))
print('\n\n')
print('M3,N3')
print(matrix_product(M3, N3))
print('\n\n')
print('M4,N4')
print(matrix_product(M4, N4))
