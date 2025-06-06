def matrix_product(M: np.ndarray, v: np.ndarray) -> np.ndarray: # TODO
    if len(M[0]) == len(v):
        out = []
        for i in range(0, len(v)-1):
            out.append(0)
        count = 0
        for j in M:
            count2 = 0
            for k in j:
                ans = k * v[count2]
                out[count] += ans
                count2 += 1
            count += 1
        return(np.array(out))
    else:
        raise DimensionError("Vectors niet hetzelfde formaat")
