import streamlit as st
import matplotlib.pyplot as plt
import random
from decimal import Decimal

def randomFibo(rng):
    lstx = [0, 1]
    lstratio = [0, 0]
    lsty = [1, 1]
    lstyabs = [1, 1]
    for i in range(rng):
        lstx.append(i+2)
        a = random.randrange(0, 2)
        if a == 0:
            nummer = lsty[i] + lsty[i+1]
            lsty.append(nummer)
            lstyabs.append(abs(nummer))
        else:
            getal = lsty[i+1] - lsty[i]
            lsty.append(getal)
            lstyabs.append(abs(getal))
        ratio = round(abs(lsty[-1])**(1/Decimal(len(lsty))), 3)
        lstratio.append(ratio)
    fig, ax = plt.subplots()
    ax.plot(lstx, lstyabs, 'ko', markersize=1)
    ax.set_yscale("log")
    ax.set_title("Random Fibonacci Absolute Values (log scale)")
    return fig

st.title("Random Fibonacci Plot Generator")
n = st.number_input("Give the range (1000 recommended):", min_value=1, value=1000, step=100)
fig = randomFibo(int(n))
st.pyplot(fig)
