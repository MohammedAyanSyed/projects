import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from pydantic import BaseModel,Field
import requests


class Data(BaseModel):
    free_flow_speed_kmh : int = Field(ge=10,le=300)
    weekend : int
    time_period : str = Field(max_length=15)
    travel_time_category : str = Field(max_length=15)
    speed_kmh : int = Field(ge=5,le=180)
    rush_hours : int
    hour : int = Field(ge=0,le=23)
    travel_time_per_10_km_min : int = Field(ge=1,le=100)


def congestion_predict(a,b,c,d,e,f,g,h):
    try:
        df = {
            'free_flow_speed_kmh':a,
            'weekend':b,
            'time_period':c,
            'travel_time_category':d,
            'speed_kmh':e,
            'rush_hours':f,
            'hour':g,
            'travel_time_per_10_km_min':h
        }
        info = Data(**df)
        info_dict= info.model_dump()
        response = requests.post('https://traffic-api-latest-3gyz.onrender.com/predict',json=info_dict)
        if response.status_code == 200:
            return info_dict,response.json()['congestion_level']
        else:
            return response.text

    except Exception as e:
        return f'Error = {e}'

def congestion():
    metric_df = pd.read_csv("C:\\Users\\Mohammed Ayan Syed\\projects\\End-to-End Apps\\AI-Traffic-Intelligence-Platform\\"
                     "data\\processed\\traffic_fe.csv")
    st.sidebar.metric(label='Total Records',value=len(metric_df),border=True)
    st.sidebar.metric(label='Total Cities',value=len(metric_df['city'].unique()),border=True)
    st.sidebar.metric(label='Total Features', value=len(metric_df.columns), border=True)
    st.sidebar.metric(label='Best Model',value='RandomForest',border=True)

    congestion_value = 0
    st.title('ō͡≡o Congestion Predictor')
    st.subheader(':rainbow[Predict traffic congestion travel based on road and time conditions]')
    st.divider()
    st.subheader('Enter Traffic Conditions')
    col1,col2,col3 = st.columns([2,2,6])
    selected = {'No':0,'Yes':1}
    with col1:
        speed = st.number_input('Free Flow Speed (km/h)',10,300)
        current_speed = st.number_input('Current Speed (km/h)',5,180)
        travel_speed = st.number_input('Travel Time per 10 km (min)',1,100)
        hour = st.slider('Hour (0-23)',0,23)
        weekend = selected[st.selectbox('Weekend',['No','Yes'])]

    with col2:
        rush = selected[st.selectbox('Rush Hour',['No','Yes'])]
        period = st.selectbox('Time Period',['Morning','Afternoon','Evening','Night','Late Night']).lower()
        category = st.selectbox('Travel Time Category',['Fast','Moderate','Heavy']).lower()
        speed_cat = st.selectbox('Speed Category',['Low','Medium','Fast','High']).lower() # Not Used
        city = st.selectbox('City',['Berlin','Chicago','Dublin','London','Los Angeles','New York City',
                                    'Paris','Sydney','Tokyo']) # Not Used

        btn = st.button('Predict Congestion', key='btn_right')
    if btn:
        user_df,congestion_value = congestion_predict(speed,weekend,period,category,current_speed,rush,hour,travel_speed)
        if congestion_value > 100:
            congestion_value = 100
        user_df = pd.DataFrame([user_df])
        user_df['weekend'].replace(to_replace=[0,1],value=['No','Yes'],inplace=True)
        user_df['rush_hours'].replace(to_replace=[0,1],value=['No','Yes'],inplace=True)
        user_df['speed_cat'] = speed_cat
        user_df['city'] = city
        user_df['congestion_level'] = congestion_value
        st.dataframe(user_df)

    with col3:
        def meter(val):
            fig = go.Figure(go.Indicator(mode='gauge+number',value=val,domain=dict(x=[0,1],y=[0,1]),
                                    gauge=dict(axis=dict(range=[0,100]),bar=dict(color="rgba(0,0,0,0)"),
                                    steps=[{'range':[0,25],'color':'green'},{'range':[25,50],'color':'#C4BD31'},
                                    {'range':[50,75],'color':'orange'},{'range':[75,100],'color':'red'}],
                                    threshold=dict(line=dict(color='white',width=4),thickness=1,value=congestion_value))))
            fig.update_layout(
                width=350,
                height=350,
                title=dict(text='Congestion Predicted',x=0.3,y=0.9,font=dict(size=25)),
                font=dict(size=20)
            )
            return fig
        level = meter(congestion_value)
        col3.plotly_chart(level,config=dict(displayModeBar=False))
        one,two = st.columns(2)
        if btn:
            with one:
                if congestion_value <=25:
                    st.success('🟢 Low Traffic')
                elif congestion_value <=50:
                    st.info('🔵 Moderate Traffic')
                elif congestion_value <=55:
                    st.warning('🟠 High Traffic')
                else:
                    st.error('🔴 Severe Traffic')
            with two:
                if congestion_value <= 25:
                    st.success('Recommended route is clear for normal travel')
                elif congestion_value <=50:
                    st.info('Consider observing traffic conditions during peak hours')
                elif congestion_value <=55:
                    st.warning('Consider alternative travel schedules')
                else:
                    st.error("Consider alternative routes if possible")
    if btn:
        st.info('Note : Prediction is based on trained machine learning model and provided inputs')