# semi_project_sales

> 강남구 상권 내 편의점의 예상 매출액을 구하고 이를 Streamlit으로 시각화하는 프로젝트입니다.

## 서비스 링크​
* https://procspredictor.streamlit.app/

## Requirements
* language : Python 3.11.5
* Python library
  * streamlit == 1.24.1
  * pandas == 2.0.3
  * numpy == 1.25.2
  * matplotlib == 3.7.2
  * seaborn == 0.12.2
  * plotly == 5.9.0
  * scikit-learn == 1.3.0
  * lightgbm == 1.2.0
  * shapley
  * streamlit_option_menu
  * folium
  * polygon
  * pyproj

### Architecture

* data : 필요데이터
  * 골목_model용.csv : 골목상권 최종 train data
  * 비골목상권_model용.csv : 비골목상권 최종 train data
* streamlit : 스트림릿 폴더
  * data : streamlit 구현에 필요한 데이터
  * models : 각 상권 별 최종 모델의 바이너리 파일
* models_gol.py ; 골목상권 모델
* models_ngol.py : 비골목상권 모델
* Geopandas_230906.ipynb : 앱 내 지도 시각화
* map.html : 시각화 저장 파일


