import streamlit as st

st.title('제목 입력')
st.header('헤더 입력')
st.subheader('서브헤더 입력')
st.caption('캡션이에요')
st.write('일반 글 입니다')

# 코드 입력
code = '''
print(hello)
'''
st.code(code, language = 'python')

# 마크다운 문법
st.markdown('마크다운 *문법* 가능')
st.markdown(':green[색깔을 입힐 text]') # 색깔 지원 : green, red, orange...

# 밑줄    
st.divider()
    
# 이모지
st.write('커피가 보인다:coffee:')    
    
# 유용해보이는 바탕색 들
st.success('성공한듯한 초록 바탕')
st.warning('문제가있는듯한 노랑바탕')
st.info('아무튼 파랑바탕')
st.error('오류가 발생한듯한 빨간 바탕')    
