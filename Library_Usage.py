
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import streamlit as st

# read dataframe
df = pd.read_csv('small_df.csv')

st.header('Library Usage Dashboard')

st.sidebar.title('Filters')

#selective FeedBack Side bar with No filters option

patron_options = ['No Filter'] + df['Patron Type Definition'].unique().tolist()
notice_options = ['No Filter'] + df['Notice Preference Definition'].unique().tolist()
email_options = ['No Filter'] + df['Provided Email Address'].unique().tolist()
county_options = ['No Filter'] + df['Outside of County'].unique().tolist()


selected_patrons = st.sidebar.multiselect('Patron Type'.title() , patron_options  , default='No Filter')
selected_notice = st.sidebar.multiselect('Notice Preference'.title() , notice_options , default='No Filter')
selected_email = st.sidebar.multiselect('Provided Email'.title() , email_options , default='No Filter')
selected_county = st.sidebar.multiselect('County Status'.title() , county_options , default='No Filter')

filtered_df = df.copy()


if 'No Filter' not in selected_patrons:
    filtered_df = filtered_df[filtered_df['Patron Type Definition'].isin(selected_patrons)]

if 'No Filter' not in selected_notice:
    filtered_df = filtered_df[filtered_df['Notice Preference Definition'].isin(selected_notice)]

if 'No Filter' not in selected_email:
    filtered_df = filtered_df[filtered_df['Provided Email Address'].isin(selected_email)]

if 'No Filter' not in selected_county:
    filtered_df = filtered_df[filtered_df['Outside of County'].isin(selected_county)]

#creating tabs
data , Dashboard = st.tabs(['Data' , 'Dashboard'])

with data:
  
  st.header('Raw Data')
  
  fig0= ff.create_table(filtered_df)
  fig0.update_layout(width = 1050)
  st.plotly_chart(fig0)

with Dashboard:
  
  st.subheader('Total Checkouts Analysis')
  
  col1 , col2 , col3 = st.columns(3)
  
  with col1 :
    
    st.subheader('Patron Type')
    
    fig1_1 = px.pie(data_frame = filtered_df , names = filtered_df['Patron Type Definition'] 
                  , values =filtered_df['Total Checkouts'] )
    fig1_1.update_layout(width = 320 , height = 320 , title = 'Patron Type')
    st.plotly_chart(fig1_1)
    
    
    fig1_2 = px.histogram(data_frame=df, x=filtered_df['Patron Type Definition'], y=filtered_df['Total Checkouts'] ,
                        color = filtered_df['Home Library Definition'] ,barmode = 'group', text_auto = True)
    fig1_2.update_layout(width = 320 , height = 320 , title = 'Home Library' )
    st.plotly_chart(fig1_2)
    
    
    
    
  with col2 :
    
    st.subheader('Year Registered and Notice')
    
    fig2_1 = px.histogram(data_frame=df, x=filtered_df['Year Patron Registered'].sort_values().astype('O')
                        , y=filtered_df['Total Checkouts'] , text_auto = True )
    fig2_1.update_layout(width = 320 , height = 320 , title = 'Year Patron Registered' )
    st.plotly_chart(fig2_1)
    
    fig2_2 = px.histogram(data_frame=df, x=filtered_df['Notice Preference Definition'], y=filtered_df['Total Checkouts'] ,
                        color = filtered_df['Provided Email Address'] ,barmode = 'group', text_auto = True )
    fig2_2.update_layout(width = 320 , height = 320 , title = 'Notice Pref (provided email)' )
    st.plotly_chart(fig2_2)
    
  with col3 :
    
    st.subheader('Active Circulation')
    
    fig3_1 = px.histogram(data_frame = filtered_df , x = filtered_df['Circulation Active Month'] 
                        , y=filtered_df['Total Checkouts'] , text_auto = True , color =  filtered_df['Circulation Active Month'])
    fig3_1.update_layout(width = 320 , height = 320, title = 'Circulation Active Month')
    st.plotly_chart(fig3_1)
    
    fig3_2 = px.histogram(data_frame = filtered_df , x = filtered_df['Circulation Active Year'] 
                        , y=filtered_df['Total Checkouts'] , text_auto = True , color = filtered_df['Circulation Active Year'])
    fig3_2.update_layout(width = 320 , height = 320 , title = 'Circulation Active Year')
    st.plotly_chart(fig3_2)
    
    
