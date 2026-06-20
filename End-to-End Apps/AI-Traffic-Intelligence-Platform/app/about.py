import pandas as pd
import streamlit as st
import graphviz

df = pd.read_csv('https://raw.githubusercontent.com/MohammedAyanSyed/projects/refs/heads/main/End-to-End%20Apps/AI-Traffic-Intelligence-Platform/data/processed/cleaned_dataset.csv',
                 parse_dates=['time'])
def about_project():
    st.sidebar.write('Tech Stack')
    st.sidebar.markdown("""
    - 🐍 Python
    - 🐼 Pandas
    - 📊 Plotly
    - 🧊 Scikit-learn
    - 〇 Optuna
    - ⚡ FastAPI
    - 🖥️ Streamlit
    - 🐋 Docker
    - ®️ Render
    """)
    st.sidebar.subheader('Connect')
    s1,s2 = st.sidebar.columns([2,8])
    with s1:
        st.markdown(
            """
            <a href="https://github.com/MohammedAyanSyed" target="_blank">
                <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" 
                     alt="GitHub Logo" width="60" style="border:none;"/>
            </a>
            """,
            unsafe_allow_html=True
        )
    with s2:
        st.markdown(
            """
            <a href="https://www.linkedin.com/in/mohammad-ayan-syed" target="_blank">
                <img src="https://cdn.worldvectorlogo.com/logos/linkedin-icon-2.svg" 
                     alt="LinkedIn Logo" width="45" style="border:none;"/>
            </a>
            """,
            unsafe_allow_html=True
        )
    st.title('About Project')
    st.text('Learn more about the AI Traffic Intelligence Platform, its architecture and technologies used.')
    st.divider()
    col1,col2 = st.columns([3,7])
    with col1:
        st.image('images/traffic.png',width=300)
    with col2:
        st.subheader(':blue[**Project Overview**]')
        st.write('The AI Traffic Intelligence Platform is an end-to-end solution designed to analyze traffic patterns and'
                 'predict congestion levels using Machine Learning.')
        st.write('It helps users understand traffic behaviour, make informed decisions and reduce travel time by providing '
                 'accurate congestion predictions.')
        st.write('The platform integrates data preprocessing, feature engineering, model optimization, API deployment,'
                 'and interactive visualization into a unified workflow.')
        st.write(':green[**Predict congestion levels on a scale 0 to 100**]')
    st.divider()
    col3,col4 = st.columns(2)
    with col3:
        st.subheader(":green[𖦏 Goal]")
        st.write('To build an Intelligent system that predicts traffic congestion levels based on road and time conditions'
                 'and provide actionable insights through an interactive dashboard')
    with col4:
        st.subheader(":orange[✰ Key Features]")
        st.markdown("""
        - Explore traffic trends and patterns
        - User-friendly and interactive dashboard
        - Deployed and accessible online""")
    st.divider()

    st.subheader(':blue[𖠿 **Project Workflow**]')
    st.write('\n')
    dot = graphviz.Digraph(graph_attr={'rankdir':'LR','bgcolor':'transparent'})
    dot.node('A','Data Source',shape='box',style='filled',color='light blue',textsize='20',fillcolor="#CFFDFF",
             fontname="Helvetica-Bold")
    dot.node('B', 'Data Preprocessing', shape='box', style='filled', color='light green',fillcolor='#CFFFD1',
             fontname="Helvetica-Bold")
    dot.node('C','Model Training',shape='box',style='filled',color='light purple',fillcolor='#BA7DE3',
             fontname="Helvetica-Bold")
    dot.node('D', 'Deployment', shape='box', style='filled', color='light orange',fillcolor='#E0A667',
             fontname="Helvetica-Bold")
    dot.node('E','Dashboard',shape='box',style='filled',color='light blue',fillcolor='#E0DE67',
             fontname="Helvetica-Bold")
    dot.edge("A", "B", color="grey",penwidth="2",minlen="2")
    dot.edge("B", "C", color="grey",penwidth="2",minlen="2")
    dot.edge("C", "D", color="grey",penwidth="2",minlen="2")
    dot.edge("D", "E", color="grey",penwidth="2",minlen="2")
    st.graphviz_chart(dot)
    st.divider()

    col5,col6 = st.columns([4,2])
    information = {
      "Source" : 'Traffic Congestion Dataset',
      "Total Records" : len(df),
      "Total Features" : len(df.columns),
      "Target" : "congestion_level",
      "Cities Covered" : len(df['city'].unique()),
      "Date Range" : str(df.loc[df.index[0],'time'].date())+' - '+str(df.loc[df.index[-1],'time'].date())
    }
    with col5:
        st.subheader(":violet[Dataset Information]")
        st.dataframe(information)

    col6.subheader(":yellow[Project Links]")
    col1,col2 = col6.columns([2,8])
    with col1:
        st.image('images/github.png',width=80)
    with col2:
        st.write('\n')
        st.link_button('**Github repository**',url='https://github.com/MohammedAyanSyed/projects/tree/main/End-to-End%20Apps/AI-Traffic-Intelligence-Platform')
    col3, col4 = col6.columns([2,8])
    with col3:
        st.image('images/docker.png', width=80)
    with col4:
        st.write('\n')
        st.link_button('**Docker Image**',url='https://hub.docker.com/repository/docker/ayansyed19/traffic-api/general')
    col7,col8 = col6.columns([2,8])
    with col7:
        st.image('images/fast.png',width=80)
    with col8:
        st.write('\n')
        st.link_button('**Render FastAPI**',url='https://traffic-api-latest-3gyz.onrender.com/')