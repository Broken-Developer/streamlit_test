# streamlit 라이브러리 호출
import streamlit as st

# 마크다운을 기반으로 한 꾸미기 기능 작동
st.write(
    """
    # 제 첫 웹 페이지입니다.
    ## 부족하지만 많이 사랑해주세요!
    * 1$ = 1,300원
    """
)

st.image(
    "https://cdn.pixabay.com/photo/2016/02/18/18/37/puppy-1207816_960_720.jpg"
)