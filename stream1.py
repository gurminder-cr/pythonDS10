# pip install streamlit 
import streamlit as st 
# to run this file - 
# streamlit run file_name.py 
# python -m streamlit run file_name.py 

st.set_page_config(page_title="Main Page",page_icon="🏡")
st.header("Class - Python Data Science")
st.subheader("Subheading")
st.write("Streamlit is an open-source Python framework that allows you to build interactive, beautiful web applications for data science and machine learning projects without needing any web development experience")

email= st.text_input(label="Email", placeholder="Write Email here..")
st.text_input(label="Password", type='password')

st.number_input(label="Age", min_value=5)

gender= st.radio('Gender',options=['Male','Female'])

terms= st.checkbox("Agree terms and conditions")
state= st.selectbox("Select State",options=['Punjab','HP','UP','MP','UK'])
hobbies= st.multiselect("Hobbies",options=['Gaming','Travelling','Watching Reels','Reading Books'])


marks = st.slider(label="Marks",min_value=10, max_value=100)

btn= st.button("Save")
if btn:
    # st.success("Details Saved")
    st.warning("Warning")
    st.error("Error")
    st.write(email)