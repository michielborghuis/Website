import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


def decimal2base(n, b):
    return int(np.base_repr(n, b))


def base2decimal(n, b):
    return int(n, b)


def overlap(a, b):
    string_1 = ''
    string_2 = ''
    if len(a) > len(b):
        string_1 += a
        string_2 += b
    else:
        string_1 += b
        string_2 += a

    for i in range(len(string_2)):
        if string_1[i] == string_2[i] == '1':
            return True
    return False


def overlapreverse(a, b):
    a1 = a[::-1]
    b1 = b[::-1]
    return overlap(a1, b1)


def remy(r, base):
    lstx = []
    lsty = []
    lstb = []
    for i in range(1, r):
        pos = list(range(r))
        lstx.append(i)
        binary = decimal2base(i, base)
        sbinary = str(binary)
        if i == 1:
            lsty.append(0)
            lstb.append('1')
        else:
            for j in lstb:
                if overlapreverse(j, sbinary):
                    if lsty[lstb.index(j)] in pos:
                        pos.remove(lsty[lstb.index(j)])
            lstb.append(sbinary)
            lsty.append(pos[0])
    fig, ax = plt.subplots()
    ax.plot(lstx, lsty, 'ko', markersize=1)
    ax.set_title("Remy Sigrets Plot")
    return fig

st.title("Balanced Base Plot Generator")
st.markdown('[Inspiration video](https://youtu.be/j0o-pMIR8uk?si=6zAn9bjI6rrgJy90&t=371)')
n = st.number_input("Give the range (700 recommended):", min_value=1, value=700, step=100)
base = st.number_input("Give the base between 2 and 10 (2 recommended):", min_value=2, max_value=10, value=2, step=1)
fig = remy(int(n), int(base))
st.pyplot(fig)
