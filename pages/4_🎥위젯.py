'# :blue[사용자 입력]'

'### :orange[텍스트 입력]'
import streamlit as st
text = st.text_input('여기에 텍스트를 입력하세요')
st.write(f'입력된 텍스트: {text}')

'### :orange[숫자 입력]'
number = st.number_input('여기에 숫자를 입력하세요')
st.write(f'입력된 숫자: {number}')

"### :orange[날짜 입력]"
date = st.date_input('날짜를 입력하세요')
st.write(f'선택된 날짜: {date}')

'### :orange[시간 입력]'
time = st.time_input('시간을 선택하세요')
st.write(f'선택된 시간: {time}')

'### :orange[파일 업로드]'
file = st.file_uploader('파일을 업로드하세요')

# 파일 임시적으로 사용하는 방법
if file:
    st.write(f'업로드된 파일: {file}')

# 파일 별도로 저장하는 방법
import os
if file:
    # 파일 저장 경로 지정
    file_path = os.path.join('../data/', file.name)
    # 파일 저장
    with open(file_path, 'wb') as f:    # 'wb': 바이너리 쓰기 모드 => 파일을 텍스트가 아니라 ‘순수한 0과 1의 데이터’ 그대로 저장
        f.write(file.getbuffer())   # file.getbuffer(): 이 파일의 내용을 바이트 단위 그대로 가져오는 함수
    st.success(f'파일이 저장되었습니다: {file_path}')

'# 🏋️ :blue[버튼]'

'### :orange[기본 버튼: st.button()]'
button = st.button('일반 버튼')
if button:
    st.write('버튼이 클릭되었습니다.')

primary_button = st.button('주요 버튼', type='primary')
if primary_button:
    st.write('주요 버튼이 클릭됐습니다.')

'### :orange[다운로드 버튼: st.download_button()]'
with open("./data/mysql.png", 'rb') as file:
    st.download_button(
        label = '이미지 파일 다운로드',
        data = file,
        file_name = 'image.png',
        mime = 'image/png'
    )

'### :orange[피드백 버튼: st.feedback()]'
sentiment_mapping = ['one', 'two', 'three', 'four', 'five']
selected = st.feedback('stars')
if selected is not None:
    st.markdown(f'당신은 {sentiment_mapping[selected]} star(s)을 선택했습니다.')

sentiment_mapping = [':material/thumb_down:', ':material/thumb_up:']
selected = st.feedback('thumbs')
if selected is not None:
    st.markdown(f'당신은 {sentiment_mapping[selected]}을 선택했습니다.')

'### :orange[링크 버튼: st.link_button()]'
st.link_button('갤러리 링크', 'https://streamlit.io/gallery')

'### :orange[멀티 셀렉트 박스]'
multi = st.multiselect('여기에서 여러 값을 선택하세요', ['선택1', '선택2', '선택 3'])
st.write(f'{type(multi) = }, {multi}가 선택됐습니다.')