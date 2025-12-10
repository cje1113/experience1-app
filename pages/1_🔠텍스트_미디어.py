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

'### 코드 블록: st.code()'
st.code('print("Hello, World!")', language='python', line_numbers=True)

'### 코드 + 결과: st.echo()'
with st.echo():
    name = 'habao'
    st.write("Hello, Streamlit!", name)

'### Latex 수식 작성: st.latex()'
st.latex(r'\int_a^b f(x)dx')

st.divider()

'# 🔠: Streamlit Magic' # python 코드 그대로 사용 가능

'''
### 마크다운 헤더3
- 마크다운 목록1. **굵게** 표시
- 마크다운 목록2. *기울임* 표시

### 마크다운 링크
- [네이버](https://naver.com)
- [구글](https://google.com)

### 마크다운 인용
> 인용문: "Streamlit은 데이터 앱을 쉽게 만들 수 있는 프레임워크입니다."

### 마크다운 표
| 헤더1 | 헤더2 |
|------|------|
| 데이터1 | 데이터2 |

### 마크다운 코드 블록
``` python
def hello_world():
    print("Hello, World!")
```
'''