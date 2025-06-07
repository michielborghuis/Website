import streamlit as st
import matplotlib.pyplot as plt
from math import sqrt
from itertools import count, islice
import numpy as np


def decimal2base(n, b):
    return int(np.base_repr(n, b))


def base2decimal(n, b):
    return int(n, b)


def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))


def verse_base_plot(base):
    lstx = []
    lsty = []
    for i in range(100000):
        if is_prime(i):
            lstx.append(i)
            normal = decimal2base(i, base)
            reversed_str = str(normal)[::-1]
            decreversed = base2decimal(reversed_str, base)
            lsty.append(i - decreversed)
    fig, ax = plt.subplots()
    ax.plot(lstx, lsty, 'ko', markersize=1)
    ax.set_title("Reversed Base Plot")
    return fig


st.title("Reversed Base Plot Generator")
st.markdown('[Inspiration video](tps://youtu.be/pAMgUB51XZA?si=nEqy5SZa8g-7jITC&t=472)')
base = st.number_input("Give base between 2 and 10:", min_value=2, max_value=10, value=2, step=1)
fig = verse_base_plot(int(base))
st.pyplot(fig)
