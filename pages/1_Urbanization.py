import streamlit as st
import streamlit.components.v1 as components


def population_density():
    population_html = open('urban_html/population_density.html', 'r', encoding='utf-8')  
    population_code = population_html.read()
    components.html(population_code, width=950, height=450)


def traffic_vol():
    traffic_html = open('urban_html/traffic_vol.html', 'r', encoding='utf-8')  
    traffic_code = traffic_html.read()
    components.html(traffic_code, width=950, height=450)


def road_length():
    road_html = open('urban_html/road_length.html', 'r', encoding='utf-8')  
    road_code = road_html.read()
    components.html(road_code, width=950, height=450)


def parking_space():
    parking_html = open('urban_html/parking_space.html', 'r', encoding='utf-8')  
    parking_code = parking_html.read()
    components.html(parking_code, width=950, height=450)


def water_supply():
    water_html = open('urban_html/water_supply.html', 'r', encoding='utf-8')  
    water_code = water_html.read()
    components.html(water_code, width=950, height=450)

def electricity_regional():
    electricity_html = open('urban_html/electricity_regional.html', 'r', encoding='utf-8')  
    electricity_code = electricity_html.read()
    components.html(electricity_code, width=950, height=450)


def electricity_purpose():
    pass
    # electricity_html = open('urban_html/electricity_purpose.html', 'r', encoding='utf-8')  
    # electricity_code = electricity_html.read()
    # components.html(electricity_code, width=950, height=450)


st.set_page_config(page_title="Urbanization")
st.markdown("# 도시화")
# st.sidebar.header("User Settings")

urb_titles = st.sidebar.selectbox(
    '도시화',
    ['인구 밀도', '교통량', '도로 연장', '주차장', '상수도', '전력 사용량']
)

st.write(
    """도시와 교통이 발전할수록 삶의 질은 높아지고, 많은 사람들이 편리함을 누릴 수 있게됩니다.
    다음의 데이터는 서울의 도시화 과정을 보여줍니다."""
)

if urb_titles == '인구 밀도':
    st.markdown("### 인구 밀도")
    population_density()

if urb_titles == '교통량':
    st.markdown("### 교통량")
    traffic_vol()

if urb_titles == '도로 연장':
    st.markdown("### 도로 연장")
    road_length()

if urb_titles == '주차장':
    st.markdown("### 주차장")
    parking_space()

if urb_titles == '상수도':
    st.markdown("### 상수도")
    water_supply()

if urb_titles == '전력 사용량':
    st.markdown("### 전력 사용량")
    graph_types = st.radio(
        "분류를 선택해주세요.",
        ["자치구 별", "용도 별"], 
        horizontal=True
    )
    if graph_types == '자치구 별':
        electricity_regional()
    else:
        electricity_purpose()

