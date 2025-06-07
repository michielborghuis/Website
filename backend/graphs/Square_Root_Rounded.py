import streamlit as st
import matplotlib.pyplot as plt
import math


def sqrtrounded(r):
    lstx = []
    lsty = []
    for i in range(r):
        lstx.append(i)
        number = math.sqrt(i)
        lsty.append(int(number))

    fig, ax = plt.subplots()
    ax.plot(lstx, lsty, 'ko', markersize=1)
    ax.set_title("Square Root Rounded Plot")
    return fig

st.title("Square Root Rounded Plot Generator")
st.markdown('[Inspiration video](https://youtu.be/pAMgUB51XZA?si=mmkd4vSRp3sd-pS1&t=72)')
n = st.number_input("Give the range (> 1000 recommended):", min_value=1, value=1000, step=100)
fig = sqrtrounded(int(n))
st.pyplot(fig)
