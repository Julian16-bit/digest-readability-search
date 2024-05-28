import streamlit as st
import numpy as np
import plotly.figure_factory as ff
import plotly.express as px
import pandas as pd
from scipy.stats import zscore
import matplotlib.pyplot as plt


st.set_page_config(layout="wide")

df1 = pd.read_csv('digest_descriptives_merged.csv')
df2 = pd.read_csv('digest_descriptives_merged_highschool_bestversionL6V2.csv')

tab1, tab2 = st.tabs(["All Sections", "Search"])

with tab1:
    fig = px.scatter(df1, x='section_number', y='flesch_kincaid_grade', title="All Sections Readability",  height = 1500)
    fig.update_layout(xaxis_title='',margin_b=400, margin_l = 40, margin_r=10, margin_t=50)
    st.plotly_chart(fig, theme=None, use_container_width=True)

with tab2:
    user_input = st.text_input("", placeholder="🔍 Search for a section number", label_visibility="collapsed")
    
    if user_input:
        section = df1.loc[df1['section_number']==user_input]
        section = section[['section_text', 'flesch_kincaid_grade', 'gunning_fog', 'sentence_length_mean']]
        simple_section = df2.loc[df2['section_number']==user_input]
        simple_section = simple_section[['simplified_text', 'flesch_kincaid_grade', 'gunning_fog', 'sentence_length_mean']]
        st.table(section)
        st.table(simple_section)
