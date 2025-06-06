import streamlit as st


def pi(x):
    count = 1
    pi_div = 1
    for i in range(x):
        count += 2
        if (count-1) % 4 == 0:
            pi_div += 1/count
        else:
            pi_div -= 1/count
    pi = pi_div * 4
    return pi

st.title("Estimate Pi")
points = st.number_input("Number of random points", min_value=100, value=10000, step=100)
pi_estimate = pi(points)
st.write(f"Estimated value of Pi after {points} iterations: {pi_estimate}")
