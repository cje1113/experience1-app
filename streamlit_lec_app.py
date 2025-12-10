import streamlit as st

st.title('스트림릿 실습 👋')

# 페이지 설정
st.set_page_config(
    page_title = '하교수의 Streamlit',  # 페이지 tab 타이틀
    page_icon = '👋',   # 페이지 tab의 아이콘
    layout = 'wide',    # 페이지 전체 폭: centered(기본값, 콘텐츠가 가운데 정렬), wide(화면 전체 폭을 넓게 사용)
    # 사이드바 초기 상태(스트림릿 실행 시 사이드바를 기본으로 어떻게 표시): auto, collapsed(실행 시 접혀 있음), expanded(실행하자마자 사이드바가 펼쳐짐)
    initial_sidebar_state = 'expanded',
    # 페이지 오른쪽 상부 메뉴에 추가할 메뉴 항목
    menu_items={
        'Get help':'https://ie.hongik.ac.kr/ie/index.do',
        'Report a bug': 'https://ie.hongik.ac.kr/ie/index.do',
        'About': '### 하정훈 교수 \n - [홍익대학교 산업데이터공학과] (https://ie.hongik.ac.kr/ie/index.do)'
    }
)

st.sidebar.title('다양한 사이드바 위젯들')
st.sidebar.checkbox('고령인구 포함')
st.sidebar.divider()
st.sidebar.radio('데이터 타입', ['전체', '남성', '여성'])
st.sidebar.slider('나이', 0, 100, (20,50))
st.sidebar.selectbox('지역', ['서울','경기','인천','대전','대구','부산','광주'])