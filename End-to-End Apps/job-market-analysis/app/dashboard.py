import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from sqlalchemy import create_engine,text

@st.cache_data
def load_data(file):
    csv = pd.read_csv(file)
    return csv
df = load_data('https://raw.githubusercontent.com/MohammedAyanSyed/projects/refs/heads/main/End-to-End%20Apps/job-market-analysis/data/processed/final_cleaned_data.csv')

st.set_page_config(layout='wide')
st.markdown("""<style>.block-container { 
        padding-top: 3rem;
        padding-left: 2rem}
        </style>""",unsafe_allow_html=True)
st.markdown("""<style>[data-testid="stSidebar"] h1 {
        font-size: 2rem;
        margin-top: 0;     
    }</style>""",unsafe_allow_html=True)
st.sidebar.title(':rainbow[JOB MARKET DASHBOARD]')


# ---------------------------------------KPIs--------------------------------------
col1,col2,col3,col4= st.columns(4)
with col1:
    #
    col1.metric(label='📊 Total Jobs',value=len(df),border=True)
with col2:
    col2.metric(label='🏢 Total Companies',value=len(df['company_name'].unique()),border=True)
with col3:
    cate = df['job_category'].value_counts().idxmax()
    col3.metric(label='💼 Top Job Category',value=cate,border=True)
with col4:
    location = df['location'].value_counts().keys()
    col4.metric(label='📍 Top Location',value=location[1],border=True)

st.divider()

# -------------------------------------CHARTS-----------------------------------------
# # Level - 1
col1,col2= st.columns(2)

# Chart - Vertical Bar Plot

PLOT_CONFIG = {'displayModeBar':False}
def create_bar_chart(x,y,df,text):
    fig = px.bar(x=x, y=y, data_frame=df, text=text, color=x,
                 color_discrete_sequence=px.colors.sequential.Plasma)
    fig.update_layout(title={'text': 'Distribution Of Jobs per Category', 'x': 0.3, 'y': 0.9},
                      font={'size': 16, 'family': 'Arial'},
                      xaxis_title='Jobs Category', yaxis_title='Distribution', showlegend=False, xaxis_showgrid=False,
                      yaxis_showgrid=False)
    fig.update_traces(textposition='outside', hovertemplate='Posting : %{y}<br>')
    return fig


job_distribution = df.groupby('job_category')['job_title'].count().reset_index()
sorted_jobs = sorted(zip(job_distribution['job_category'],job_distribution['job_title']),key=lambda x : x[1],reverse=True)
cate,counts = zip(*sorted_jobs)
new = st.sidebar.multiselect('Select Jobs Category',options=cate,default=cate,key='job_category_filter')
only = job_distribution[job_distribution['job_category'].isin(new)]
only = only.sort_values(by='job_title',ascending=False)
fig = create_bar_chart(x='job_category',y='job_title',df=only,text='job_title')
col1.plotly_chart(fig,use_container_width=True,config=PLOT_CONFIG)

# Chart - Horizontal Bar plot

def create_horizontal_plot(x,y,text,c):
    fig = px.bar(x=x, y=y, orientation='h', text=text, color=c,
                  color_discrete_sequence=px.colors.sequential.Viridis)
    fig.update_layout(title={'text': 'Skills Distribution', 'x': 0.5, 'y': 0.9},
                       title_font={'size': 16, 'family': 'Arial'},
                       xaxis_title='Count', yaxis_title='Skills', xaxis_showgrid=False, yaxis_showgrid=False,
                       showlegend=False)
    fig.update_traces(textposition='outside')
    return fig

skills = ['python','machine learning','deep learning','data visualization','r','sql','ai','data analysis']
counts2 = []
for i in skills:
    counts2.append(len(df[df['skills'].str.contains(i,case=False,na=False)]))
order = sorted(zip(skills,counts2),key=lambda x : x[1],reverse=False)
sl,sv = zip(*order)
sz = st.sidebar.slider('Select Top Skills',1,8,value=8,key='skills_slider')
fig2 = create_horizontal_plot(x=sv[-sz:],y=sl[-sz:],text=sv[-sz:],c=sl[-sz:])
col2.plotly_chart(fig2,use_container_width=True,config=PLOT_CONFIG)


# Level - 2
col3,col4,col5 = st.columns([4,3,3])

# Chart - B1 Heatmap
def create_heatmap(k):
    fig = px.imshow(k, text_auto=True, color_continuous_scale=px.colors.sequential.Cividis, aspect='equal',
                     title='Salary Distribution According to Experience')
    fig.update_layout(title={'x': 0.25, 'y': 0.85})
    return fig
sal_distribution = pd.pivot_table(data=df,index='salary_category',columns='experience_level',values='job_category',aggfunc='count',fill_value=0)
fig3 = create_heatmap(sal_distribution)
col3.plotly_chart(fig3,use_container_width=True,config=PLOT_CONFIG)

# Chart - B2 Pie Chart
def create_pie_chart(s,v,n,c):
    fig = px.pie(data_frame=s, values=v, names=n, color=c,
                  color_discrete_sequence=px.colors.sequential.Magma, hole=0.7, title='Salary Distribution')
    fig.update_layout(title={'x': 0.2, 'y': 0.5})
    return fig
salary_distribution = df.groupby('salary_category')['job_category'].count().reset_index()
salary_distribution = salary_distribution.sort_values(by='job_category',ascending=True)
fig4 = create_pie_chart(s=salary_distribution,v='job_category',n='salary_category',c='salary_category')
col4.plotly_chart(fig4,use_container_width=True,config=PLOT_CONFIG)

# Chart - B3 Lollipop
def create_lollipop_chart(x,y):
    fig = go.Figure()
    fig.add_trace(go.Bar(x=x, y=y, width=0.05, showlegend=False))
    fig.add_trace(go.Scatter(x=x, y=y, mode='markers',showlegend=False, marker=dict(size=15, color='#7CFFB2')))
    fig.update_layout(
        title=dict(text='Jobs Across Various Locations', x=0.3, y=0.8, font=dict( size=20)),
        xaxis_title='Location', font=dict(size=12), yaxis_title='Distribution', yaxis_showgrid=False)
    return fig
company_distribution = df.groupby('location')['skill_count'].count().reset_index()
company_distribution = company_distribution.sort_values(by='skill_count',ascending=False).iloc[1:9,0:]
choice = st.sidebar.slider('Enter Number of Locations',1,8,value=5,key='location_slider')
fig5 = create_lollipop_chart(x=company_distribution['location'][:choice],y=company_distribution['skill_count'][:choice])
col5.plotly_chart(fig5,use_container_width=True,config=PLOT_CONFIG)


# Level - 3
col6,col7,col8 = st.columns([3,4,3])
# Chart - C1
with col6:
    st.markdown("<div style='margin-top:-20px'></div>", unsafe_allow_html=True)
    st.success('AI Engineer roles Dominate current hiring market')
    st.info('R , Python and SQL are most requested skills across job')
    st.warning('High-paying opportunities are limited compared to low and medium salary categories')
    st.error('Senior-level positions are significantly fewer, indicating strong competition for experienced roles')

# Chart - C2
def create_line_chart(x):
    fig = px.line(x=range(1, len(x) + 1), y=x.values, markers=True)
    fig.update_layout(title={'text': 'Skills Vs Job Distribution', 'x': 0.4, 'y': 0.9},
                       font={'size': 15},
                       xaxis_title={'text': 'Number Of Skills'}, yaxis_title={'text': 'Number Of Jobs'},
                       yaxis_showgrid=False)
    fig.update_traces(line=dict(color='#00D4FF'), marker=dict(size=12, color='#7CFFB2')
                       , hovertemplate='Postings : %{y}<extra></extra>')
    return fig

skill_count = df.groupby('skill_count')['skill_count'].count()
fig7 = create_line_chart(skill_count)
col7.plotly_chart(fig7, use_container_width=True, config=PLOT_CONFIG)

# Chart - C3
def create_scatter_chart(x,y):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x,y=y,mode='markers',name='',marker=dict(
        size=y,color='#38BDF8',sizemin=8,opacity=0.7,),hovertemplate="Company: %{x}<br>Openings: %{y}"))
    fig.update_layout(title={'text':'Top 5 Companies By Job Openings','x':0.3,'y':0.85},font={'size':15},
                   xaxis_title='Companies',yaxis_title={'text':'Postings'})
    return fig

posting_count = df.groupby('company_name')['skill_count'].count().reset_index()
posting_count = posting_count.sort_values(by='skill_count',ascending=False).iloc[0:5,:]
fig8 = create_scatter_chart(x=[i[:8] for i in posting_count['company_name']],y=posting_count['skill_count'])
col8.plotly_chart(fig8,use_container_width=True,config=PLOT_CONFIG)

st.divider()

# -------------------------------TABS--------------------------------------
tab1,tab2 = st.tabs(['CSV','Suggestion Box'])

with tab1:
    c1,c2 = st.columns(2)
    c1.dataframe(df.head(8),use_container_width=True)
    c2.dataframe(df.describe())
    csv = df.to_csv(index=False).encode('UTF-8')
    st.download_button(label='Download CSV File',data=csv,file_name='Jobs.csv',mime='csv')


@st.cache_resource
def init_connection():
    return create_engine(st.secrets['DB_URL'])

engine = init_connection()
def create_table():
    with engine.connect() as conn:
        conn.execute(text("""CREATE TABLE IF NOT EXISTS suggestions(
                                id SERIAL PRIMARY KEY,
                                name VARCHAR(500) NOT NULL,
                                rating INT NOT NULL,
                                suggestion VARCHAR(25000))"""))
        conn.commit()
create_table()
with tab2:
    Name = st.text_input('Enter Name')
    Rating = st.slider('Rating',1,10)
    Suggestion = st.text_area('Any Suggestion',value='No Suggestion')
    submit = st.button('Submit')
    if submit:
        DB_URL = st.secrets["DB_URL"]

        if Name.strip() and Suggestion.strip():
            try:
                with engine.connect() as conn:
                    conn.execute(text("""INSERT INTO suggestions(name,rating,suggestion)
                                    VALUES(:name,:rating,:suggestion)"""),
                {'name':Name,'rating':Rating,'suggestion':Suggestion})
                    conn.commit()
                    st.success(f'Thanks for your feedback {Name}')
                    st.balloons()
            except Exception as e:
                st.error('Database Connection Error')
        else:
            st.error('Please Enter Details')
