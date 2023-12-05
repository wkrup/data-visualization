import streamlit as st


def traffic_vol():
    pass


def num_buildings():
    pass


def population_density():
    pass


def subway_history():
    pass


def road_packaging():
    pass


def public_transportation():
    pass


st.set_page_config(page_title="Urbanization")
st.markdown("# 도시화")
st.sidebar.header("User Settings")
st.write(
    """도시와 교통이 발전할수록 삶의 질은 높아지고, 많은 사람들이 편리함을 누릴 수 있게됩니다.
    다음의 데이터는 서울의 도시화 과정을 보여줍니다."""
)

st.markdown("### 교통량")
traffic_vol()

st.markdown("### 건물 수")
num_buildings()

st.markdown("### 인구 밀도")
population_density()

st.markdown("### 지하철 노선도")
subway_history()

st.markdown("### 도로 포장률")
road_packaging()

st.markdown("### 대중교통 분담률")
public_transportation()
