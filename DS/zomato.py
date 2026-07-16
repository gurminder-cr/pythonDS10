import streamlit as st 
import pandas as pd
import plotly.express as px
st.set_page_config("Zomato")
st.header("Zomato Visualization")

data= pd.read_csv('zomato_dataset.csv')
# st.write(data)

# st.write(data.isnull().sum())
# st.write(data.shape)

data= data.dropna(axis=0)
# st.write(data.shape)
data.drop_duplicates(inplace=True)
st.write(data)
st.write(data.shape)

# st.write(data['Restaurant Name'].value_counts())

# fig1= px.pie(names=data['Restaurant Name'].value_counts().index[:5], values=data['Restaurant Name'].value_counts().values[:5])
# st.plotly_chart(fig1)

# data.sort_values(by='Votes',inplace=True,ascending=False)
# st.write(data)

# fig2= px.bar(data_frame=data,y=data.loc[:,'Votes'][:7],x=data.loc[:,'Item Name'][:7], color=data.loc[:,'Restaurant Name'][:7])
# st.plotly_chart(fig2)

unique_res= data.loc[:,'Restaurant Name'].value_counts().index
# st.write(unique_res)

with st.sidebar:
    selected= st.selectbox("Select Restaurant",options=unique_res)
    
data_selected = data[data.loc[:,'Restaurant Name']==selected]
# st.write(data_selected)
data_selected.sort_values(by='Votes',inplace=True,ascending=False)
fig3= px.bar(data_frame=data_selected,y=data_selected.loc[:,'Votes'][:7],x=data_selected.loc[:,'Item Name'][:7])
st.plotly_chart(fig3)