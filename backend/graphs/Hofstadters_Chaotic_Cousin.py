import streamlit as st
import matplotlib.pyplot as plt


def hofstadterssequence(r):
    lstx = []
    lsty = [1, 1]

    for i in range(r):
        lstx.append(i)
        if i != 0 and i != 1:
            lsty.append(lsty[lsty[i - 1] - 1] + lsty[i - lsty[i - 2] - 1])
    fig, ax = plt.subplots()
    ax.plot(lstx, lsty, 'ko', markersize=1)
    ax.set_title("Hofstadter's Chaotic Cousin")
    return fig


st.title("Hofstadter's Chaotic Cousin Plot Generator")
st.markdown('[Inspiration video](https://youtu.be/j0o-pMIR8uk?si=ngf4ppIIjWPeVemu&t=344)')
n = st.number_input("Give the range (1000000 recommended):", min_value=1, value=1000000, step=100000)
fig = hofstadterssequence(int(n))
st.pyplot(fig)
