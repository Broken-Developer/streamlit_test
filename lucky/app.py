# streamlit 라이브러리 호출
import streamlit as st
import numpy as np

# https://docs.streamlit.io/library/get-started/main-concepts
# st.write() 마크다운
st.title("조 추첨 페이지")

# 추첨 대상인 13명의 이름을 넣을 수 있는 text_input을 만든다.
# 13명이 소속될 조 이름을 넣을 위치를 만든다.

# <추첨 버튼>
# 13개의 짝을 지어서 표시해줄 그래픽