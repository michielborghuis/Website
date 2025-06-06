import streamlit as st


def prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6

    return True


st.title("Prime Checker")
num = st.number_input("Enter a number:", min_value=0, value=17)
checker = prime(num)
st.write(f"The number {num} is {'a prime number' if checker else 'not a prime number'}.")
