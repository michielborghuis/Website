import streamlit as st
import numpy as np
import math
import matplotlib.pyplot as plt


def mandel(repeats, x, y):
    pyt = 0
    manx = x
    many = y
    mana = 0
    manb = 0
    mandelgetal = 0

    while pyt <= 2 and mandelgetal < repeats:
        mandelgetal += 1
        newmana, newmanb = formule(manx, many, mana, manb)
        pyt = math.sqrt(newmana*newmana + newmanb*newmanb)
        mana = newmana
        manb = newmanb

    return mandelgetal

def formule(x, y, a, b):
    manx = a*a - b*b + x
    many = 2*a*b + y
    return manx, many

st.title("Mandelbrot Set")

size = st.slider("Image size (pixels)", 100, 1000, 400)
repeats = st.slider("Max iterations", 1, 300, 100)

img = np.zeros((size, size))

for x in range(size):
    for y in range(size):
        x_val = (x - (size / 2)) * 0.01
        y_val = (y - (size / 2)) * 0.01
        mandel_number = mandel(repeats, x_val, y_val)
        # Normalize for display: 0 if in set, 1 if out
        if mandel_number % 2 == 0 and mandel_number != repeats:
            img[y, x] = 1  # white
        else:
            img[y, x] = 0  # black

fig, ax = plt.subplots()
ax.imshow(img, cmap="gray", extent=[-2, 2, -2, 2])
ax.set_axis_off()
st.pyplot(fig)
