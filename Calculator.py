import streamlit as st

# Arithmetic functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "❌ Cannot divide by zero!"
    return x / y

# Streamlit UI
st.title("🧮 Simple Streamlit Calculator")
st.write("Perform basic arithmetic operations with ease! 🔢")

# User inputs
num1 = st.number_input("Enter the first number:", format="%.2f")
num2 = st.number_input("Enter the second number:", format="%.2f")

operation = st.selectbox(
    "Select an operation:",
    ("➕ Add", "➖ Subtract", "✖️ Multiply", "➗ Divide")
)

# Calculate on button click
if st.button("🧠 Calculate"):
    if operation == "➕ Add":
        result = add(num1, num2)
    elif operation == "➖ Subtract":
        result = subtract(num1, num2)
    elif operation == "✖️ Multiply":
        result = multiply(num1, num2)
    elif operation == "➗ Divide":
        result = divide(num1, num2)

    st.success(f"✅ Result: {result}")

    st.markdown("---")
    st.markdown("<p style='text-align: center; color: red;'>Made with ☕ and ❤️ by Ufaq Fatima</p>", unsafe_allow_html=True)
