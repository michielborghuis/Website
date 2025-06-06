import streamlit as st
import matplotlib.pyplot as plt


def wisteria(r):
    lstx = []
    lsty = []
    for i in range(r):
        value = 1
        string = str(i)
        for j in string:
            value *= int(j)
        lstx.append(i)
        lsty.append(i-value)
    fig, ax = plt.subplots()
    ax.plot(lstx, lsty, 'ko', markersize=1)
    ax.set_title("Wisteria Plot")
    return fig


st.title("Wisteria Plot Generator")
n = st.number_input("Give the range (> 1000 recommended):", min_value=1, value=1000, step=100)
fig = wisteria(int(n))
st.pyplot(fig)
