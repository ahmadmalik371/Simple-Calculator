import streamlit as st
import math

# Title and description for the app
st.title("Simple Calculator with Streamlit")
st.write("Perform basic operations as well as power, square root, cosine, and logarithm.")

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    else:
        return x / y

# Function to calculate power (x^y)
def power(x, y):
    return math.pow(x, y)

# Function to calculate square root
def sqrt(x):
    if x < 0:
        return "Error: Square root of a negative number!"
    else:
        return math.sqrt(x)

# Function to calculate cosine
def cosine(x):
    return math.cos(math.radians(x))  # converting degrees to radians

# Function to calculate logarithm (base 10)
def logarithm(x):
    if x <= 0:
        return "Error: Logarithm of zero or negative number!"
    else:
        return math.log10(x)

# List of operations
operations = ["Add", "Subtract", "Multiply", "Divide", "Power", "Square Root", "Cosine", "Logarithm"]

# Streamlit UI to select operation
operation = st.selectbox("Select an operation:", operations)

# Based on the selected operation, take the required inputs and display the result
if operation in ["Add", "Subtract", "Multiply", "Divide", "Power"]:
    num1 = st.number_input("Enter first number:")
    num2 = st.number_input("Enter second number:")

    if st.button("Calculate"):
        if operation == "Add":
            result = add(num1, num2)
        elif operation == "Subtract":
            result = subtract(num1, num2)
        elif operation == "Multiply":
            result = multiply(num1, num2)
        elif operation == "Divide":
            result = divide(num1, num2)
        elif operation == "Power":
            result = power(num1, num2)
        st.write(f"Result: {result}")

elif operation == "Square Root":
    num = st.number_input("Enter number:")
    if st.button("Calculate"):
        result = sqrt(num)
        st.write(f"Result: {result}")

elif operation == "Cosine":
    num = st.number_input("Enter number (in degrees):")
    if st.button("Calculate"):
        result = cosine(num)
        st.write(f"Result: cos({num}) = {result}")

elif operation == "Logarithm":
    num = st.number_input("Enter number:")
    if st.button("Calculate"):
        result = logarithm(num)
        st.write(f"Result: log10({num}) = {result}")
