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