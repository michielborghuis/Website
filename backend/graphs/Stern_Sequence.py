import streamlit as st
import matplotlib.pyplot as plt


def sternsequence(r):
    all = []
    lst = [1, 1]

    for i in range(r):
        lengte = len(lst)
        new = [0] * (lengte * 2 - 1)
        for j in range(lengte):
            if j == 0:
                new[j] = lst[j]
            else:
                new[j*2] = lst[j]
                new[j*2-1] = lst[j-1] + lst[j]
        lst = new
        all.append(new)
    return all


def sternsequenceplot(r):
    allseq = sternsequence(r)
    lstx = []
    lsty = []
    count = 0
    for i in allseq:
        for j in i:
            lstx.append(count)
            lsty.append(j)
            count += 1
    fig, ax = plt.subplots()
    ax.plot(lstx, lsty, 'ko', markersize=1)
    ax.set_title("Stern Sequence Plot")
    return fig


st.title("Stern Sequence Plot Generator")
st.markdown('[Inspiration video](https://youtu.be/j0o-pMIR8uk?si=VG2_l-ZexYxWJtEA&t=1)')
n = st.number_input("Give the range (12 recommended):", min_value=1, value=12, step=1)
fig = sternsequenceplot(int(n))
st.pyplot(fig)
