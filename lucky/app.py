# streamlit 라이브러리 호출
import streamlit as st
import numpy as np

# https://docs.streamlit.io/library/get-started/main-concepts
# st.write() 마크다운
st.title("조 추첨 페이지")
st.header("여러분의 참여를 환영합니다!")

# https://docs.streamlit.io/library/cheatsheet

# 추첨 대상인 13명의 이름을 넣을 수 있는 text_input을 만든다.
# 3 X 4 행렬로 배치
# 열을 배치하는 메서드
columns = st.columns(4) # 화면을 열로 나눠서 배치
# 가로 4개의 열 -> columns = [col1, col2, col3, col4]
# col1, col2, col3, col4로 언팩킹해서 사용해도 된다.
# 우리는 for문을 사용한다.
for idx, col in enumerate(columns) :
    # col.text_input(f"조 추첨 대상 {idx + 1}", key="idx")
    for idx2 in range(4) :
        # 키가 겹치면 안된다.
        col.text_input(f"조 추첨 대상 {idx + idx2 * 4}", key="idx + idx2 * 4")

# 13명이 소속될 조 이름을 넣을 위치를 만든다.

# <추첨 버튼>
# 13개의 짝을 지어서 표시해줄 그래픽