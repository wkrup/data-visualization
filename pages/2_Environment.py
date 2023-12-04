import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import folium 
import json
from chart_studio import plotly as py

import os

def fn_energy_use():
    energy_html = open('nature_html/energy_page.html', 'r', encoding='utf-8')    
    energy_code = energy_html.read()
    components.html(energy_code, height=450)
    

def nature_area():
    nature_html = open('nature_html/nature_choropleth.html', 'r', encoding='utf-8')    
    nature_code = nature_html.read()
    components.html(nature_code, height=450)

def sewage_cost():
    sewage_html = open('nature_html/sewage_page.html', 'r', encoding='utf-8')  
    sewage_code = sewage_html.read()
    components.html(sewage_code, height=450)

def atmos_contam():
    atmos_html = open('nature_html/atmos_page.html', 'r', encoding='utf-8')
    atmos_code = atmos_html.read()
    components.html(atmos_code, height=450)



st.set_page_config(page_title="Environment")
st.markdown("# 자연 환경")
st.sidebar.header("User Settings")
st.write(
    """시간의 흐름에 따라 변화하는 서울의 자연 환경을 다양한 측면에서 시각화했습니다."""
)

st.markdown("### 에너지 소비")
fn_energy_use()

st.markdown("### 녹지 면적")
nature_area()

st.markdown("### 하수 처리 비용")
sewage_cost()

st.markdown("### 대기 오염")
atmos_contam()

