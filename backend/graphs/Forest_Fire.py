import streamlit as st
import matplotlib.pyplot as plt


def forestFire(r):
    lstx = []
    lsty = []
    for n in range(r):
        lstx.append(n)
        i, j, b = 1, 1, set()
        while n-2*i >= 0:
            b.add(2*lsty[n-i]-lsty[n-2*i])
            i += 1
            while j in b:
                b.remove(j)
                j += 1
        lsty.append(j)
    fig, ax = plt.subplots()
    ax.plot(lstx, lsty, 'ko', markersize=1)
    ax.set_title("Forest Fire Plot")
    return fig


st.title("Forest Fire Plot Generator")
st.markdown('[Inspiration video](https://youtu.be/o8c4uYnnNnc?si=QFEvMei_rY4cqMao&t=220)')
n = st.number_input("Give the range (> 1000 recommended):", min_value=1, value=1000, step=100)
fig = forestFire(int(n))
st.pyplot(fig)
 