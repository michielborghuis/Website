import streamlit as st
from matplotlib import pyplot as plt
import random


class Triangles:
    def __init__(self, number):
        self.number = number

    def triangles(self):
        xs = [1, 2, 3]
        ys = [0, 2, 0]

        a = [1, 0]
        b = [2, 2]
        c = [3, 0]

        start = [2, 1]

        for i in range(self.number):
            rand = random.randrange(1, 4)
            xs.append(start[0])
            ys.append(start[1])
            if rand == 1:
                start = [(start[0] + a[0])/2, (start[1] + a[1])/2]
            elif rand == 2:
                start = [(start[0] + b[0]) / 2, (start[1] + b[1]) / 2]
            elif rand == 3:
                start = [(start[0] + c[0]) / 2, (start[1] + c[1]) / 2]

        fig, ax = plt.subplots()
        ax.scatter(xs, ys, s=1, color='black')
        ax.set_title("Triangles Plot")
        return fig


st.title("Triangles Plot Generator")
n = st.number_input("Give amount of points (> 1000 recommended):", min_value=1, value=1000, step=100)
t = Triangles(int(n))
fig = t.triangles()
st.pyplot(fig)
