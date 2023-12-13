import streamlit as st
import streamlit.components.v1 as components

import os

def vehicle():
    vehicle_html = open('double_html/vehicle.html', 'r', encoding='utf-8')    
    vehicle_code = vehicle_html.read()
    components.html(vehicle_code, width=950,height=450)
    

def water():
    water_html = open('double_html/water.html', 'r', encoding='utf-8')    
    water_code = water_html.read()
    components.html(water_code, width=950, height=450)

def green_energy():
    green_energy_html = open('double_html/green_energy.html', 'r', encoding='utf-8')
    green_energy_code = green_energy_html.read()
    components.html(green_energy_code, width=950, height=450)

def green_energy_map():
    st.markdown("### 자치구별 전력 에너지 사용량")
    electricity_html = open('urban_html/electricity_purpose.html', 'r', encoding='utf-8')  
    electricity_code = electricity_html.read()
    components.html(electricity_code, width=950, height=450)
    # st.image('Image/out_2020.png')
    st.markdown("### 자치구별 녹지 면적")
    nature_html = open('nature_html/full_nature_choropleth.html', 'r', encoding='utf-8')    
    nature_code = nature_html.read()
    components.html(nature_code, width=950, height=450)
    # st.image('Image/녹지_2020.png')
    




st.set_page_config(page_title="Double Visualization")
st.markdown("# 도시-자연환경 이중 변화")

double_titles = st.sidebar.selectbox(
    '도시-자연환경 이중 변화',
    ['차량수-온실가스 배출량 및 대중교통 분담률', '배수 계획 면적 - 사업 유지비', '녹지 면적 - 에너지 소비량']
)


st.markdown("")

if double_titles == '차량수-온실가스 배출량 및 대중교통 분담률':
    st.write(
    """
  
서울의 도시화 과정과 자연환경 변화 과정을 연도별로 시각화하여 보여줌으로써  
도시가 발전하는 만큼 자연도 함께 변하고 있음을 나타냈습니다.  
    """
)
    
    st.write(
        """
연도별 서울시 차량 등록 대수와 대중교통 분담률을 확인해보면,  
차량 수의 증가에도 불구하고 대중교통(버스, 지하철, 철도, 택시)의 분담률은 유지되거나 감소하는 경향을 보입니다.  
결과적으로 개인 차량이 증가하고, 온실가스 배출량을 증가시키는 원인이 됨을 확인할 수 있습니다.  

    """
    )
    st.markdown("### 차량 대수 - 온실가스 배출량/대중교통 분담률")
    vehicle()

if double_titles == '배수 계획 면적 - 사업 유지비':
    st.markdown("### 배수 계획 면적 - 사업 유지비")
    st.write(
        """
지난 2005년부터 2021년까지 서울시 내 배수 계획 면적과 사업 유지비를 시각화하면 아래와 같습니다.  
배수 계획 면적이 증가할수록 사업비도 함께 증가하고 있는데,  
특히 2013년 이후 뚜렷하게 확인할 수 있습니다.  
도시가 발전함에 따라 도시를 유지관리하는 비용도 증가하게 됩니다.

    """
    )
    water()

if double_titles == '녹지 면적 - 에너지 소비량':
    st.markdown("### 녹지 면적 - 에너지 소비량")
    st.write(
        """
서울시의 공원 및 녹지 면적을 연도별로 시각화한 결과입니다.  
녹지 면적은 점차 증가하고 있으나, 이는 대부분 아파트 내부 조경녹지와 기부채납 공원 등 폐쇄적인 녹지가 증가한 결과입니다.  
도시화에 따라 전력 에너지 사용량이 증가하고, 이에 따라 전력 탄소 배출량도 함께 증가하게 됩니다.  

    """
    )
    graph_types = st.radio(
        "Select type",
        ["Line Plot", "Map"], 
        horizontal=True
    )
    if graph_types == 'Line Plot':
        green_energy()
    else:
        green_energy_map()


