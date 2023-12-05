import streamlit as st
import streamlit.components.v1 as components

def energy_use():
    #https://discuss.streamlit.io/t/include-an-existing-html-file-in-streamlit-app/5655/2
    energy_html = open('nature_html/energy_page.html', 'r', encoding='utf-8')    
    energy_code = energy_html.read()
    components.html(energy_code, width=950, height=450)
    

def nature_area_1():
    nature_html = open('nature_html/full_nature_choropleth.html', 'r', encoding='utf-8')    
    nature_code = nature_html.read()
    components.html(nature_code, width=950, height=450)

def nature_area_2():
    nature_html2 = open('nature_html/full_nature_bar.html', 'r', encoding='utf-8')
    nature_code2 = nature_html2.read()
    components.html(nature_code2, width=950, height=450)

def sewage_cost():
    sewage_html = open('nature_html/sewage_page.html', 'r', encoding='utf-8')  
    sewage_code = sewage_html.read()
    components.html(sewage_code, width=950, height=450)

def atmos_contam():
    atmos_html = open('nature_html/atmos_page.html', 'r', encoding='utf-8')
    atmos_code = atmos_html.read()
    components.html(atmos_code, width=950, height=450)

def nature_perception():
    nat_perc_html = open('nature_html/nature_perception_page.html', 'r', encoding='utf-8')
    nat_perc_code = nat_perc_html.read()
    components.html(nat_perc_code, width=950, height=450)

def park_all():
    park_html = open('nature_html/park_page.html', 'r', encoding='utf-8')
    park_code = park_html.read()
    components.html(park_code, width=950, height=450)

def park_count():
    park_count_html = open('nature_html/park_count.html', 'r', encoding='utf-8')
    park_count_code = park_count_html.read()
    components.html(park_count_code, width=950, height=450)

def park_area():
    park_area_html = open('nature_html/park_area.html', 'r', encoding='utf-8')
    park_area_code = park_area_html.read()
    components.html(park_area_code,  width=950, height=450)



st.set_page_config(page_title="Environment")
st.markdown("# 자연 환경")
# st.sidebar.header("User Settings")

env_titles = st.sidebar.selectbox(
    '자연 환경',
    ['에너지 소비', '녹지 면적', '하수 처리 비용', '대기 오염', '체감 환경', '공원']
)



st.write(
    """시간의 흐름에 따라 도시화 되어가는 서울의 자연 환경을 다양한 측면에서 분석할 수 있도록 데이터를 시각화했습니다."""
)

if env_titles == '에너지 소비':
    st.markdown("### 에너지 소비")
    energy_use()


if env_titles == '녹지 면적':
    st.markdown("### 녹지 면적")
    graph_types = st.radio(
        "Select graph type",
        ["Choropleth", "Bar Graph"], 
        horizontal=True
    )
    if graph_types == 'Choropleth':
        st.caption("*2006년 은평구 데이터는 누락되었기 때문에 Graph에 등장하지 않습니다.")
        nature_area_1()
        st.caption("geojson file from https://github.com/southkorea/seoul-maps")
    else:
        st.caption("*2006년 은평구 데이터는 누락되었기 때문에 Graph에 등장하지 않습니다.")
        nature_area_2()




if env_titles == '하수 처리 비용':
    st.markdown("### 하수 처리 비용")
    sewage_cost()

if env_titles == '대기 오염':
    st.markdown("### 대기 오염")
    atmos_contam()

if env_titles == '체감 환경':
    st.markdown("### 체감 환경")
    st.markdown('###### 2010년 이전에는 10세 이상 조사, 그 외에는 13세 이상 조사')
    nature_perception()


if env_titles == '공원':
    st.markdown("### 공원")
    park_data = st.radio(
        "보고 싶은 데이터를 선택하세요",
        ["둘 다", "공원 개소", "공원 면적"], 
        horizontal=True
    )
    if park_data == '둘 다':
        park_all()
    elif park_data == '공원 개소':
        park_count()  
    else:
        park_area()