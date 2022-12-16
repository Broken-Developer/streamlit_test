# Streamlit 머신러닝
# 1-1. 머신러닝 라이브러리/패키지 requirements에 설치
# 1-2. 데이터, 패러미터들로 모델 훈련 -> 모델 사용
# -> 훈련에 많은 시간 안 걸리는 경우

# 2. Colab, Jupyter Notebook ... -> pkl 모델 파일 -> joblib 읽어들여와서 쓰는 방법
# -> 훈련 자체 시간이 많이 걸린다, 결과값만 빠르게 보여주고 싶다

# streamlit 라이브러리 호출
import streamlit as st

with st.echo(code_location="below"):
    import pandas as pd

    df = pd.read_csv('https://raw.githubusercontent.com/bigdata-young/ai_26th/main/data/insurance.csv')
    st.write(df)

with st.echo():
    import joblib # 사이킷런 import 안해도 model 객체 자체를 pkl로 불러옴
    import os
    # os.path... 파이썬 경로문제

    model_path = f"{os.path.dirname(os.path.abspath(__file__))}/model.pkl"
    model = joblib.load(model_path)
    st.write("## 선형 회귀 모델")
    st.write(pd.Series(model.coef_, index=["age", "bmi", "children", "smoker", "sex_male", "region_northwest", "region_northeast", "region_southwest"]))

# age : 나이
st.number_input(
    label="나이",
    step=1,
    value=30,
    key='age'
)
# st.session_state['age']
# st.write(st.session_state['age'])

# sex : 성별
st.radio(
    label='성별',
    options=["남성", "여성"],
    index=0, # 기본 선택
    key='sex'
)
# st.write(st.session_state['sex'])

# bmi : 비만도(실수형)
st.number_input(
    label='BMI',
    step=0.1, # 실수형으로 받을 수 있게
    value=25.0,
    key='bmi'
)
# st.write(st.session_state['bmi'])

# children : 자녀수
st.number_input(
    label='자녀수',
    step=1,
    value=1,
    key='children'
)
# st.write(st.session_state['children'])

# smoker : 흡연여부
st.checkbox(
    label='흡연여부',
    value=False,
    key='smoker'
)
# st.write(st.session_state['smoker'])

# region : 지역
st.selectbox(
    label='지역',
    options=["북동", "북서", "남동", "남서"],
    index=2,
    key='region'
)
# st.write(st.session_state['region'])

if st.button('예측') :
    st.balloons()
    # 예측
    # model.predict(X_test) -> 전처리한 데이터 형태로 들어간 행렬, df.
    # df X -> 이중 리스트([])
    # [ [age,bmi,children,smoker,sex_male,
    #    region_northwest,region_northeast,region_southwest] ]

    state = st.session_state
    # model.predict(...)
    # (...) -> 예측에 쓰일 여러 개의 행들
    # 행 : df에 쓰이는 독립변수들을 담은 행들(1개 이상 ~)
    input_values = [[
        state['age'], state['bmi'], state['children'], state['smoker'],
        state['sex'] == '남성', state['region'] == '북서', state['region'] == '북동',
        state['region'] == '남서'
    ]]
    pred = model.predict(input_values)
    # -> y값 하나만 나타낸다.
    # -> rows들에 대응하는 예측값(y값들의 리스트)
    # st.write(pred[0])
    st.metric(label='예측값', value=pred[0])