import streamlit as st
import matplotlib.pyplot as plt
import math


def binaryToDecimal(binary):
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal


def reverseprime(r):
    lstx = []
    lsty = []
    for i in range(r):
        lstx.append(i)
        binarystring = "{0:b}".format(i)
        binarystringreversed = binarystring[::-1]
        result = binaryToDecimal(int(binarystring)) - binaryToDecimal(int(binarystringreversed))
        lsty.append(result)

    fig, ax = plt.subplots()
    ax.plot(lstx, lsty, 'ko', markersize=1)
    ax.set_title("Reversed Primes Plot")
    return fig

st.title("Reversed Primes Plot Generator")
st.markdown('[Inspiration video](https://youtu.be/pAMgUB51XZA?si=nEqy5SZa8g-7jITC&t=472)')
n = st.number_input("Give the range (> 1000 recommended):", min_value=1, value=1000, step=100)
fig = reverseprime(int(n))
st.pyplot(fig)
