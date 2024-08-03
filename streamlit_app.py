import streamlit as st

st.title("🎈 My new app")
st.write("Hello world")
x = st.text_input("favorate movie")
st.write(f"You favorate movie is : {x}")
is_clicked = st.button("click here")

              
