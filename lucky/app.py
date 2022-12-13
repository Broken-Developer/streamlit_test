# https://docs.streamlit.io/library/get-started/main-concepts
# https://docs.streamlit.io/library/cheatsheet
# streamlit 라이브러리 호출
import streamlit as st
import numpy as np
import pandas as pd

# st.write() 마크다운
st.title("조 추첨 페이지")
st.header("여러분의 참여를 환영합니다!")

# ./ : repository상 가장 윗 폴더
# ./ -> ./lucky
st.image("./lucky/cute_dog.jpg")

# 추첨 대상인 13명의 이름을 넣을 수 있는 text_input을 만든다.
# 4 X 4 행렬로 배치

tabs = st.tabs(['참가자', '조'])

# st.columns(n) : 열을 배치하는 메서드
# columns = st.columns(4) # 화면을 열로 나눠서 배치

# 0번째 탭에 참가자 컬럼(열)을 넣겠다.
columns = tabs[0].columns(4)
# 가로 4개의 열 -> columns = [col1, col2, col3, col4]
# col1, col2, col3, col4로 언팩킹해서 사용해도 된다.

# 우리는 for문을 사용한다.
for idx, col in enumerate(columns) : # 열의 위치
    # enumerate() : index와 value의 묶음
    # col.text_input(f"조 추첨 대상 {idx + 1}", key="idx")
    for idx2 in range(4) :
        # 키가 겹치면 안된다.
        # col 안에 메서드를 통해서 요소들을 생성해주겠다는 의미
        col.text_input(f"조 추첨 대상 {idx + 1 + idx2 * 4}", key=f"n{idx + 1 + idx2 * 4}")

# 2번째 탭에 조 컬럼(열)을 넣겠다.
columns2 = tabs[1].columns(4)
# 가로 4개의 열 -> columns = [col1, col2, col3, col4]
# col1, col2, col3, col4로 언팩킹해서 사용해도 된다.

# 우리는 for문을 사용한다.
for idx, col in enumerate(columns2) : # 열의 위치
    # enumerate() : index와 value의 묶음
    # col.text_input(f"조 추첨 대상 {idx + 1}", key="idx")
    for idx2 in range(4) :
        # 키가 겹치면 안된다.
        # col 안에 메서드를 통해서 요소들을 생성해주겠다는 의미
        col.text_input(f"조 목록 {idx + 1 + idx2 * 4}", key=f"g{idx + 1 + idx2 * 4}")
        # n -> g : 겹치지 말라고 변경

# <추첨 버튼>
if st.button('추첨 시작') :
    # 13명이 소속될 조 이름을 넣을 위치를 만든다.
    # st.write(st.session_state)
    # np.random.choice -> 추출해서 이름들을 목록화한다.
    # 1. st.session_state -> n, g가 섞여있음
    ss = pd.Series(st.session_state) # 딕셔너리 -> 시리즈
    # st.write(ss)
    # ss2 = ss[ss != ""]
    ss2 = ss[ss.ne("")]
    # st.write(ss2)

    # string과 관련된 메서드를 사용할 수 있게 한다.
    n_idx = ss2.index.str.contains('n')
    n_data = ss2[n_idx]
    # st.write(n_data)

    g_idx = ss2.index.str.contains('g')
    g_data = ss2[g_idx]
    # st.write(g_data)

    # n_data를 섞어준다(비복원으로)
    n_rd = np.random.choice(n_data, len(n_data), replace=False)
    # st.write(n_rd)

    # g_data를 섞어준다(비복원으로)
    g_rd = np.random.choice(g_data, len(g_data), replace=False)
    # st.write(g_rd)

    # 2. df형태로 분리
    # 13개의 짝을 지어서 표시해줄 그래픽
    df = pd.DataFrame({
        "추첨 대상자 이름" : n_rd,
        "조 이름" : g_rd
    })

    # st.balloons()
    st.snow()
    st.write(df)
