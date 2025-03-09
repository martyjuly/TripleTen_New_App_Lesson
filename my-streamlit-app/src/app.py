import streamlit as st

def main():
    st.title("My Streamlit App")
    st.write("Welcome to my Streamlit application!")

    # Add more components and functionality here
    if st.button("Say Hello"):
        st.write("Hello, World!")

if __name__ == "__main__":
    main()