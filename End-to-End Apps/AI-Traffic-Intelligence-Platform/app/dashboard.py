import streamlit as st
from streamlit_option_menu import option_menu
import homepage
import predictor
import about

with st.sidebar:
   st.title('🚦AI Traffic Intelligence Platform')
   selected =  option_menu(menu_title='',options=['📊 Analytics Dashboard','🚦 Congestion Predictor','ℹ️ About Project'],
                           default_index=0)

st.set_page_config(layout='wide')
st.markdown("""<style>.block-container { 
        padding-top: 2rem;
        padding-left: 1rem}
        </style>""",unsafe_allow_html=True)
st.markdown("""<style>[data-testid="stSidebar"] h1 {
        font-size: 2rem;
        margin-top: 0;     
    }</style>""",unsafe_allow_html=True)

if selected == '📊 Analytics Dashboard':
    homepage.home()
    with st.sidebar.container():
        st.text('Technologies Used')
        st.markdown("""
         - Python
         - Numpy,Pandas
         - Plotly
         - RandomForest
         - Optuna
         - FastAPI
         - Streamlit
         - Render (Fast API)""")
if selected == '🚦 Congestion Predictor':
    predictor.congestion()
if selected == 'ℹ️ About Project':
    about.about_project()