import streamlit as st

st.title("columns")

col1, col2 = st.columns(2)

with col1:
    st.write("hellooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")
    st.header("voting area 1 ")
    vote1= st.button("vote A")

    # image 
    st.image("https://media.magnific.com/home/relaunch/media/useCases/card-workflow-2x.webp?w=477", width= 300)

with col2:
    st.write("helloooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo2")
    st.header("voting area 2 ")
    vote2= st.button("vote B")

if vote1:
    st.success("thanks for voting A")
elif vote2:
    st.success("thanks for voting B")


    
    