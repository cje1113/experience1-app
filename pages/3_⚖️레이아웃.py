'### :orange[컬럼: st.columns()]'
import streamlit as st
# 1:2:1 비율로 컬럼을 나눔
col_1, col_2, col_3 = st.columns([1,2,1])

# with col_1: 이 아래 모든 UI는 col_1 컬럼 안에 들어간다
with col_1:
    st.write('## 1번 컬럼')
    st.checkbox('이것은 1번 컬럼에 속한 체크박스 1')
    st.checkbox('이것은 1번 컬럼에 속한 체크박스 2')

with col_2:
    st.write('## 2번 컬럼')
    st.radio('2번 컬럼의 라디오 버튼', ['radio 1', 'radio 2', 'radio 3'])

col_3.write('## 3번 컬럼')
col_3.selectbox('3번 컬럼의 셀렉트박스', ['select 1', 'select 2', 'select 3'])

'### :orange[탭: st.tabs()]'

# 탭 인스턴스 3개 생성
tab_1, tab_2, tab_3 = st.tabs(['Python', 'R', 'Julia'])
with tab_1:
    st.write(
        '''
        ``` python
        import pandas as pd

        df = pd.DataFrame(
            {'id': [1,2,3,],
            'name': ['Alice', 'Bob', 'Charlie'],
            'age': [24, 34, 45]
            }
        )
        ```
        '''
    )

with tab_2:
    st.write(
        '''
        ``` r
        df <- data.frame(
            id = c(1,2,3),
            name = c('Alice', 'Bob', 'Charlie'),
            age = c(24, 34, 45)
        )
        ```
        '''
    )

tab_3.write(
    '''
    ``` julia
    using DataFrames

    df = DataFrame(
        id = [1,2,3],
        name = ['Alice', 'Bob', 'Charlie'],
        age = [24, 34, 45])
    ```
    '''
)

'### :orange[확장 레이아웃: st.expander()]'
with st.expander('🔍 확장 레이아웃'):
    st.write('이곳은 확장 레이아웃입니다.')
    st.write('확장 레이아웃은 특정 컨텐츠를 숨기거나 보여줄 때 사용됩니다.')