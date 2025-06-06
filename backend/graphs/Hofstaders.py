import streamlit as st
import matplotlib.pyplot as plt


def hofstadterssequence(r):
    lstx = []
    lsty = [1, 1]

    for i in range(r):
        lstx.append(i)
        if i != 0 and i != 1:
            lsty.append(lsty[i - lsty[i - 1]] + lsty[i - lsty[i - 2]])
    fig, ax = plt.subplots()
    ax.plot(lstx, lsty, 'ko', markersize=1)
    ax.set_title("Hofstadter's Q Sequence")
    return fig


st.title("Hofstadter's Q Sequence Plot Generator")
n = st.number_input("Give the range (5000 recommended):", min_value=1, value=5000, step=100)
fig = hofstadterssequence(int(n))
st.pyplot(fig)
