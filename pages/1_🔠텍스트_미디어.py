import streamlit as st

'## 🔠: 일반 텍스트'

st.title('제목: st.title()')
st.header('헤더: st.header()')
st.subheader('서브헤더: st.subheader()')
st.text('본문 텍스트: st.text()')
st.markdown('## 마크다운: st.markdown()')
st.caption('캡션(작고 흐린 글씨로 표현됨) : st.caption()')

'# 🔠: st.write()'
st.write('# 마크다운 H1: st.write()')
st.write('### 마크다운 H3: st.write()')
st.write('')    # 빈 줄 추가

'# 🔠: 색상이 있는 텍스트'
st.write(':red[빨간색 텍스트]')
st.write(':blue[파란색 텍스트]')