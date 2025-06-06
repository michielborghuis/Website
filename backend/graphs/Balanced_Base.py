import streamlit as st
import matplotlib.pyplot as plt
import math
import numpy as np


def decimal2base(n, b):
    if n == 0:
        return 0
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return int(''.join(str(x) for x in digits[::-1]))


def base2decimal(n, b):
    return int(str(n), b)


def balanced_base_plot(r, base):
    lstx = []
    lsty = []
    for i in range(r):
        res = 0
        new = []
        lstx.append(i)
        ter = decimal2base(i, base)
        ster = str(ter)
        if '2' in ster:
            for j in ster:
                if j == '2':
                    new.append(-1)
                else:
                    new.append(int(j))
            lengte = len(new)
            for k in new:
                res += math.pow(base, lengte-1) * k
                lengte -= 1
            lsty.append(res)
        else:
            lsty.append(base2decimal(str(ter), base))
    fig, ax = plt.subplots()
    ax.plot(lstx, lsty, 'ko', markersize=1)
    ax.set_title("Balanced Base Plot")
    return fig


st.title("Balanced Base Plot Generator")
n = st.number_input("Give the range (> 1000 recommended):", min_value=1, value=1000, step=100)
base = st.number_input("Base (2 or 3 recommended):", min_value=2, value=3, step=1)
fig = balanced_base_plot(int(n), int(base))
st.pyplot(fig)
