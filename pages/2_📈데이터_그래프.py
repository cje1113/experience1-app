'### :orange[Pandas 데이터프레임]'
import pandas as pd
df = pd.DataFrame(
    {'id': [1,2,3],
     'name': ['Alice', 'Bob', 'Charlie'],
     'age': [24, 34, 45]}
)
df # 데이터프레임 출력

'### :orange[지표(Metric)]'
import steamlit as st
col1, col2, col3 = st.columns(3)    # 3개 컬럼 생성
# st.metric(label -> 무엇, value -> 현재값, delta -> 변화량(증가면 초록, 감소면 빨강)
col1.metric("Temperature", '70 F', '1.2 F')
col2.metric('Wind', '9 mph', '-8%')
col3.metric('Humidity', '86%', '4%')