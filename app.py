import streamlit as st
from scipy.optimize import minimize

def optimize_function(x):
    return x**2

st.title("Simple Optimization App")
st.write("This app demonstrates how to use Scipy's optimize module to minimize a function.")

x0 = st.number_input("Initial guess for x:")
res = minimize(optimize_function, x0)
st.write("Minimum found at:", res.x)
