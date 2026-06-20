def home():
    import pandas as pd
    import plotly.express as px
    import streamlit as st

    df = pd.read_csv('https://raw.githubusercontent.com/MohammedAyanSyed/projects/refs/heads/main/End-to-End%20Apps/AI-Traffic-Intelligence-Platform/data/processed/traffic_fe.csv')
    model_df = pd.read_csv('https://raw.githubusercontent.com/MohammedAyanSyed/projects/refs/heads/main/End-to-End%20Apps/AI-Traffic-Intelligence-Platform/src/data_processing/comparison.csv')
    fi = pd.read_csv('https://raw.githubusercontent.com/MohammedAyanSyed/projects/refs/heads/main/End-to-End%20Apps/AI-Traffic-Intelligence-Platform/data/processed/fi.csv')

    col1,col2,col3,col4 = st.columns(4)
    with col1:
        st.metric(label='Total Records',value=len(df),delta_description='Rows in Dataset',border=True)
    with col2:
        st.metric(label='Cities',value=len(df['city'].unique()),delta_description='Unique Cities',border=True)
    with col3:
        st.metric(label='Model Used',value='RandomForest',delta='+0.03',delta_description='Best Performing Model',border=True)
    with col4:
        st.metric(label='R² Score',value=0.998,delta_description='Score On Test Data',border=True)

    city = ['All'] + list(df['city'].unique())
    cities = st.sidebar.multiselect('**Select the Cities**', city,default=['All'])
    hour = st.sidebar.slider('**Enter Hour**', 0, 23)
    weekend = st.sidebar.radio('**Weekend Filter**',['All','Weekdays','Weekend'])
    rush = st.sidebar.radio('**Rush Hour Filter**',['All','Rush Hours','Non-Rush Hours'])
    timeline = ['Morning','Afternoon','Evening','Night','Late Night']
    period = st.sidebar.multiselect('**Time Period**',timeline)

    col1,col2,col3 = st.columns(3)
    choice_df = df.copy()
    if not cities or 'All' in cities:
        choice_df = choice_df
    else:
        choice_df = choice_df[choice_df['city'].isin(cities)]
    if hour:
        choice_df = choice_df[choice_df['hour']<=hour]
    if weekend !='All':
        choice_df = choice_df[choice_df['weekend'].map({0:'Weekdays',1:'Weekend'})==weekend]
    if rush!='All':
        choice_df = choice_df[choice_df['rush_hours'].map({0:'Non-Rush Hours',1:'Rush Hours'})==rush]
    if period:
        choice_df = choice_df[choice_df['time_period'].isin([t.lower() for t in period])]
    config = {'displayModeBar':False}
    with col1:
        def congestion_city(x):
            congestion = x.groupby('city')['congestion_level'].mean().reset_index()
            congestion = sorted(zip(congestion['city'],congestion['congestion_level']),key=lambda y:y[1],reverse=True)
            if not congestion :
                return [],[]
            sl,sv = zip(*congestion)
            return sl,sv

        def congestion_plot(x,y):
            if not x or not y:
                st.error('No data available for the selected time period')
                return None
            fig = px.bar(x=x,y=y,color=x,color_discrete_sequence=['#40BDFF'])
            fig.update_layout(title={'text':'Avg Congestion By City','x':0.3,'y':0.9},title_font={'size':20},
                              xaxis_title='City',yaxis_title='Congestion Level',xaxis_showgrid=False,yaxis_showgrid=False,showlegend=False)
            fig.update_traces(hovertemplate='Congestion : %{y}<br>')
            return fig
        city,values = congestion_city(choice_df)
        figure = congestion_plot(city,values)
        if figure is not None:
            col1.plotly_chart(figure,config=config)
    with col2:
        def congestion_hour(x):
            cong_hour = x.groupby('hour')['congestion_level'].mean().reset_index()
            return cong_hour
        def hour_plot(x):
            fig = px.line(data_frame=x,x='hour',y='congestion_level',color_discrete_sequence=['red'],markers='o')
            fig.update_layout(title={'text':'Avg Congestion By Hour','x':0.3,'y':0.9},title_font={'size':20},
                              xaxis_title='Hour',yaxis_title='Congestion Level',xaxis_showgrid=False,showlegend=False)
            fig.update_traces(hovertemplate='Hour : %{x} ,Congestion : %{y}<br>')
            return fig
        avg_hour = congestion_hour(choice_df)
        figure2 = hour_plot(avg_hour)
        col2.plotly_chart(figure2,config=config)
    with col3:
        def highlight(x):
            style = pd.DataFrame('',index=x.index,columns=x.columns)
            style.loc[4,:] = "background-color:green"
            return style
        st.write('### Model Performance Comparison')
        styled_df = model_df.style.apply(highlight,axis=None)
        st.dataframe(styled_df)

    col4,col5,col6 = st.columns([3,3,4])
    with col4:
        def weekday(x):
            avg = x.groupby('weekend')['congestion_level'].mean().reset_index()
            avg['weekend'] = avg['weekend'].map({1:'weekend',0:'weekday'})
            return avg
        def pie(x):
            fig = px.pie(data_frame=x,names='weekend',values='congestion_level',hole=0.5,color='weekend',
             color_discrete_map={'weekend':'red','weekday':'blue'},
                 opacity=0.7)
            fig.update_layout(title=dict(text='Weekday vs Weekend', x=0.4, y=0.95, xanchor="center",
                                     yanchor="top"), title_font={'size': 16})
            fig.update_traces(textfont=dict(color='white', size=16),hovertemplate='congestion : %{value}<br>')
            return fig
        week = weekday(choice_df)
        figure3 = pie(week)
    col4.plotly_chart(figure3,config=config)
    with col5:
        def rush(x):
            rush_time = x.groupby('rush_hours')['congestion_level'].mean().reset_index()
            rush_time['rush_hours'] = rush_time['rush_hours'].map({1:'Rush Hour',0:'Non Rush Hour'})
            return rush_time
        def pie(x):
            fig = px.pie(data_frame=x,names='rush_hours',values='congestion_level',hole=0.5,color='rush_hours',
                     color_discrete_map={'Rush Hour':'green','Non Rush Hour':'orange'},opacity=0.7)
            fig.update_layout(title=dict(text='Rush Hour vs Non Rush Hour',x=0.4,y=0.95,xanchor="center",
                yanchor="top"),title_font={'size':16})
            fig.update_traces(textfont=dict(color='white',size=16),hovertemplate='congestion : %{value}<br>')
            return fig
        hour = rush(choice_df)
        figure4 = pie(hour)
        col5.plotly_chart(figure4,config=config)
    with col6:
        def fe_plot(df):
            fig = px.bar(x=df.iloc[:,1],y=df.iloc[:,0],color_discrete_sequence=['#2A1A4F'])
            fig.update_layout(title=dict(text='Feature Importance (Random Forest)',x=0.4,y=0.9),title_font={'size':16}
                              ,xaxis_title='Importances',yaxis_title='')
            fig.update_traces(textfont=dict(color='white',size=16),hovertemplate='congestion : %{x}<br>')
            return fig
        figure5 = fe_plot(fi)
        col6.plotly_chart(figure5,config=config)
    col7,col8 = st.columns([6,4])
    with col7:
        def congestion(x):
            val = x.groupby('congestion_level')['weekend'].count().reset_index()
            return val
        def distribution(x):
            fig = px.histogram(data_frame=x,x=x['congestion_level'],color_discrete_sequence=['purple'],nbins=5)
            fig.update_layout(title=dict(text='Congestion Level Distribution',x=0.3,y=0.9),title_font=dict(size=26),
                              xaxis_title='Congestion_level',yaxis_showgrid=False,xaxis_showgrid=False,showlegend=False,
                              bargap=0.2)
            fig.update_traces(textfont=dict(color='white',size=16),hovertemplate='congestion : %{y}<br>')
            return fig
        values = congestion(choice_df)
        figure6 = distribution(values)
        col7.plotly_chart(figure6,config=config)
    with col8:
        st.success(f'✔ Random Forest achieved R² = {0.998} indicating a strong fit to traffic patterns')
        st.info('ⓘ Peak Congestion occurs during rush hours and evening rush hours')
        st.warning('⚠︎ Routes with longer travel imes tend to experience significantly higher congestion.'
                   'Travel time is one of the stronget indicators of traffic conditions')
        st.error('🚨 Low vehicle speed are strongly associated with severe congestion levels. As '
                 'traffic speed decreases, congestion intensity generally decreases')