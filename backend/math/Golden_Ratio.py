import streamlit as st



def goldenratio(n):
    ratios = []
    lst = [0, 1]
    for i in range(n):
        lst.append(lst[i] + lst[i + 1])
        if i > 0:
            ratios.append(lst[i + 1] / lst[i])
    return ratios


st.title("Golden Ratio Calculator")
st.markdown('[Inspiration video](https://youtu.be/cjx23aMeBkQ?si=urCjoGa2bJAQJg_r)')
n = st.number_input("How many terms of the Fibonacci sequence?", min_value=2, value=10)
ratios = goldenratio(n)

st.write(f"Approximate Golden Ratio: {ratios[-1]}")
st.line_chart(ratios)
