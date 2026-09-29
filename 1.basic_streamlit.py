import streamlit as st

st.title("title")
st.subheader("subheader")
st.text("text")
st.write("write")

# selectbox / dropdown
s= st.selectbox("choose option: ", ["1","2","3","4","5"])

st.write(f"you chose option {s}, excellent choice")

# success message
st.success("success")