import streamlit as st
import matplotlib.pyplot as plt
import math


def flystraigtdammit(r):
    lstx = []
    lsty = [1, 1]
    for i in range(2, r):
        lstx.append(i)
        prev = int(lsty[i-1])
        gcd = math.gcd(i, prev)
        if gcd == 1:
            lsty.append(i+prev+1)
        else:
            lsty.append(prev/gcd)
    lsty = lsty[:-2]
    fig, ax = plt.subplots()
    ax.plot(lstx, lsty, 'ko', markersize=1)
    ax.set_title("Fly Straight Dammit Plot")
    return fig


st.title("Fly Straight Dammit Plot Generator")
n = st.number_input("Give the range (> 1000 recommended):", min_value=1, value=1000, step=100)
fig = flystraigtdammit(int(n))
st.pyplot(fig)
