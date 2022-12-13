import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.write(
    "http://data.seoul.go.kr/dataList/OA-20578/S/1/datasetView.do"
)

# df
# UTF-8 / CP-949
# https://seong6496.tistory.com/269
df = pd.read_csv('./mini_project/seoul_apt_price.csv', encoding='cp949')
st.write(df)