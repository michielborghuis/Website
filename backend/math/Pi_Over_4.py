import math
import streamlit as st

def div(n):
    divisors = []
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            divisors.append(i)
    divisors.append(n)
    return sorted(divisors)

def is_prime(n):
    return div(n) == [1, n]

def pioverfour(int_range):
    positive = 1
    negative = 0
    for i in range(3, int_range, 2):
        if (i+1) % 4 == 0:
            negative -= 1/i
        else:
            positive += 1/i
    pi_over_four = positive + negative
    pi = pi_over_four * 4
    return pi

def pioversix(int_range):
    pi_over_six = 0
    for i in range(1, int_range):
        pi_over_six += 1/(i**2)
    piSquared = pi_over_six * 6
    pi = math.sqrt(piSquared)
    return pi

def twooverpi(int_range):
    positive = 1
    for i in range(3, int_range, 2):
        if is_prime(i):
            if (i - 1) % 4 == 0:
                result = 1+(1/i)
                positive *= result
            else:
                result = 1-(1/i)
                positive *= result
    pi = 2 / positive
    return pi

st.title("Pi Approximations")
n = st.number_input("Enter range:", min_value=2, value=1000, step=1)

if st.button("Calculate"):
    pi1 = pioverfour(n)
    pi2 = pioversix(n)
    pi3 = twooverpi(n)
    st.write(f"**piOverFour gives pi =** {pi1}")
    st.write(f"**piOverSix gives pi =** {pi2}")
    st.write(f"**twoOverPi gives pi =** {pi3}")
