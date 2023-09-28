# 🚲 서울시 따릉이 대여 / 반납량 예측 모형 도출

<br>
</br>

## 💡 소개
- 주제 : 서울시 따릉이의 대여소별 대여량 및 반납량을 예측하여 효율적인 운영 방안 제시
- 일정 : 2023년도 1학기 / 데이터마이닝 강의 학기 프로젝트
- 특이점
  - **R**을 활용한 프로젝트
  - GridSearchCV, RandomSearchCV 등 하이퍼파라미터 탐색을 위한 함수들을 사용하지 않고, 탐색(Train error, Val error 분석을 통한 최적 파라미터 선정)
  - 각 모델 성능에 대한 공정한 비교 환경 보장

<br>
</br>

## 💡 프로젝트 요약


- **예측 단위 별 최적 모델 도출** : 개별 대여소, 동 단위, 구 단위로 예측할 때 가장 최고의 성능을 보여주는 모델 도출

- **현실적인 모델링 방안** : 모델 전개 이후, 유지보수 소요를 고려하였을 때 모델의 ACC와 Resource 간의 trade-off 관계 확인  

<br>
</br>

## 💡 기대효과

- 수요에 맞는 따릉이의 효율적 배치를 통한 수익 증대 및 운영 비용 감소

---

<br>
</br>

## 진행과정

### 1. 데이터 수집

<br>
</br>

## 📦 아키텍쳐

```
📦ConvenienceStore_Sales_Forecast
 ┣ 📂code
 ┃ ┣ 📂crawling
 ┃ ┣ 📂feature engineering
 ┃ ┣ 📂modeling
 ┃ ┣ 📂preprocessing
 ┣ 📂rawdata
 ┃ ┣ 📂business_district
 ┃ ┣ 📂public_transport
 ┣ 📂streamlit
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📂data
 ┃ ┣ 📂models
 ┗ ┗ 📂pages
```


