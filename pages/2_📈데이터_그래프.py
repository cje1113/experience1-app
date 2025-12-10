'### :orange[Pandas 데이터프레임]'
import pandas as pd
df = pd.DataFrame(
    {'id': [1,2,3],
     'name': ['Alice', 'Bob', 'Charlie'],
     'age': [24, 34, 45]}
)
df # 데이터프레임 출력

'### :orange[지표(Metric)]'
import streamlit as st
col1, col2, col3 = st.columns(3)    # 3개 컬럼 생성
# st.metric(label -> 무엇, value -> 현재값, delta -> 변화량(증가면 초록, 감소면 빨강)
col1.metric("Temperature", '70 F', '1.2 F')
col2.metric('Wind', '9 mph', '-8%')
col3.metric('Humidity', '86%', '4%')

'# :blue[Streamlit 그래프]'
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20,3),  # 표준정규분포(평균 0, 표준편차 1) 를 따르는 20행 3열 짜리 난수 행렬
    columns=['a','b','c']
)

'#### :orange[st.area_chart()]'
st.area_chart(chart_data)

'#### :orange[st.line_chart()]'
st.line_chart(chart_data)

'#### :orange[st.bar_chart()]'
st.bar_chart(chart_data)

'#### :orange[st.scatter_chart()]'
st.scatter_chart(chart_data)

'#### :orange[st.map()]'
df = pd.DataFrame(
    np.random.randn(100,2) / [100,100] + [37.55, 126.92],
    columns=['lat','log']
)
st.map(df)