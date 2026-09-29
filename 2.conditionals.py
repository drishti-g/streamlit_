import streamlit as st

st.title("title")

# button 
if st.button("press button"):  # add what you want to happen if button is pressed
    st.write("button pressed")
    st.success("comes when button pressed")


# checkbox
c= st.checkbox("check box , check it")
# what happens on checking the box:
if c:
    st.write("checkbox checked")


# radio button
r= st.radio("choose anything: ", ["one","two","three","four"])
st.write(f"selected radio is {r}")
if r:
    st.write(f"you chose {r}")


# dropdown
s= st.selectbox("choose option: ", ["1","2","3","4","5"])
st.write(f"you chose option {s}, excellent choice")

# slider
sd= st.slider("level you want: ", 0 , 10, 2)  # start, end , default
st.write(f"you chose level {sd}")

# num_input
ni= st.number_input(" how many : ", min_value=1 , max_value=20, step=1)
st.write(f"selected quantity {ni}")

# text_input
ti= st.text_input("enter your frekin name: ")
if ti:
    st.write(f"welcome {ti}")

# date input 
di= st.date_input("select your dob: ")
st.write(f"your dob is {di}")

# sidebar - whatever you write .idebar , goes in sidebar
age= st.sidebar.text_input("enter age")
st.sidebar.write(f"your age is {age} , this is in sidebar")
st.write(f"your age is {age} , this is NOT in sidebar")

# expander
with st.expander("instructions"):
    st.write(""" 
    1. hello
    2. bellow
    3. fellow
""")

# markdown
st.markdown('# markdown heading #')
st.markdown('> markdown ')
