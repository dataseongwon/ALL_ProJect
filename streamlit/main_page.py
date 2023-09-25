import streamlit as st
import joblib
import numpy as np
import pandas as pd
# 모델 불러오기
model1 = joblib.load("models/gm_model.pkl")
model2 = joblib.load("models/ngm_model.pkl")

# 데이터 프레임 불러오기
df = pd.read_csv('data/전체_수정_streamlit용.csv')
df1 = pd.read_csv('data/골목_streamlit용.csv')
df2 = pd.read_csv('data/비골목_streamlit용.csv')

# side bar 
with st.sidebar:
    # Select market
    unique_market = df['상권_코드_명'].unique().tolist()
    selected_feature1 = st.selectbox("상권을 선택하세요", unique_market)
    
    # Select quarter
    unique_quarter = ['1분기', '2분기', '3분기', '4분기']
    selected_feature3 = st.selectbox("분기를 선택하세요!", unique_quarter)
    
# 상권 타입 지정 
type = df[df['상권_코드_명'] == selected_feature1]['상권_구분_코드_명'].tolist()[0]
if type == '골목상권' :
    type_code = 0 # 골목상권
else:
    type_code = 1 # 비골목상권


## 지도 영역


## 변수 영역
feature_names_gol = df1.iloc[:, 13:].columns.tolist() 
feature_names_ngol = df2.iloc[:, 13:].columns.tolist() 

# ----------------------------------------------------- 시간대, 분기 값 리스트의 앞에 넣기------------------------------------------------------
time1, time2, time3, time4, time5, quarter1, quarter2, quarter3 = 0, 0, 0, 0, 0, 0, 0, 0

if selected_feature3 == unique_quarter[0]:
    quarter1 = 1
    quarter2 = 0
    quarter3 = 0
    quarter_type = 1
elif selected_feature3 == unique_quarter[1]:
    quarter1 = 0
    quarter2 = 1
    quarter3 = 0
    quarter_type = 2
elif selected_feature3 == unique_quarter[2]:
    quarter1 = 0
    quarter2 = 0
    quarter3 = 1
    quarter_type = 3
else :
    quarter1 = 0
    quarter2 = 0
    quarter3 = 0
    quarter_type = 4

numeric_user_inputs = []
for i in range (6) :
    user_input_i = [time1, time2, time3, time4, time5, quarter1, quarter2, quarter3]
    numeric_user_input_i=[]
    if i <= 4 :
        user_input_i[i] = 1
    if type_code == 0 : 
        filter_df = df1[(df1['상권_코드_명'] == selected_feature1) & (df1['분기'] == quarter_type) & (df1['기준_년_코드'] == 2022)]
    else :
        filter_df = df2[(df2['상권_코드_명'] == selected_feature1) & (df2['분기'] == quarter_type) & (df2['기준_년_코드'] == 2022)]
    filter_list_i = filter_df.iloc[i, 7:].tolist()
    user_input_i.extend(filter_list_i)
    for value in user_input_i :
        try:
            numeric_value = float(value)
            numeric_user_input_i.append(numeric_value)
        # 예외처리
        except ValueError:
            st.error(f"입력값 '{value}'은(는) 숫자로 변환할 수 없습니다.")
    numeric_user_inputs.append(numeric_user_input_i)


# 예측
feature_array = np.array(numeric_user_inputs)
st.write(feature_array)
if st.button('예측') :
    predictions = model1.predict(feature_array)
    st.write(predictions)
