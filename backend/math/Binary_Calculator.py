import streamlit as st
import math


def normalToBinary(normal):
    binary = ''
    normal = int(normal)
    while normal > 0:
        binary += str(normal % 2)
        normal = normal // 2
    return int(binary[::-1])

# def binaryToNormal(binary):
#     binary = binary[::1]
#     counter = 0
#     decimal = 0
#     while counter < len(binary):
#         if int(binary[counter]) == 1:
#             decimal += 2**counter
#         counter += 1
#     return decimal

st.title("Binary Calculator")
num = st.number_input("Enter a decimal number:", min_value=1, value=10)
num_binary = normalToBinary(num)
st.write(f"{num} gives binary = {num_binary}")

# bin = st.text_input("Enter a binary number:", value='1010')
# bin_decimal = binaryToNormal(bin)
# st.write(f"{bin} gives decimal = {bin_decimal}")
