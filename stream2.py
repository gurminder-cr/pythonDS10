import streamlit as st 
# to run this file - 
# streamlit run file_name.py 
# python -m streamlit run file_name.py 

st.set_page_config(page_title="Form Page",page_icon="🏡")

# with st.form(key='myform'):
#     # col1,col2 = st.columns(2)
#     col1,col2 = st.columns([1,1])
#     with col1:
#         email= st.text_input(label="Email", placeholder="Write Email here..")
#         st.text_input(label="Password", type='password')
#         st.number_input(label="Age", min_value=5)
#         gender= st.radio('Gender',options=['Male','Female'])
#     with col2: 
#         state= st.selectbox("Select State",options=['Punjab','HP','UP','MP','UK'])
#         hobbies= st.multiselect("Hobbies",options=['Gaming','Travelling','Watching Reels','Reading Books'])
#         marks = st.slider(label="Marks",min_value=10, max_value=100)
#         terms= st.checkbox("Agree terms and conditions")
#     btn= st.form_submit_button("Submit")
    
#media tags 

# st.image('https://static.vecteezy.com/system/resources/thumbnails/039/213/395/small/concept-save-the-world-save-environment-the-world-is-in-the-grass-of-the-green-bokeh-background-photo.jpg')

# st.video('https://youtu.be/Uvqo-q_V7P0?si=a1MoYR0ftbGhJo_m')
# # st.audio()
# st.sidebar.radio('menu')


# with st.sidebar:
#     # menu= st.radio('Menu',options=['Home','About','Contact'])
#     menu= st.selectbox('Menu',options=['Home','About','Contact'])
# pip install streamlit-option-menu
from streamlit_option_menu import option_menu

# with st.sidebar:
menu =  option_menu(menu_title='',options=['Home','About','Contact'],orientation='horizontal' , icons=['house-fill','info-square-fill','telephone-fill'])


if menu=='Home':
    st.header("Homepage")
elif menu=='About':
    st.header("About Page")
elif menu=='Contact':
    st.header("Contact Page")

