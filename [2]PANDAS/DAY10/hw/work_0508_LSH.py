# # 1
# Pandas 함수로 2개 데이터 파일을 읽고 합쳐서 1개의 데이터프레임 변수명 df에 할당하는 코드를 작성하세요.
#  - heart_failure_a.json파일을 읽어 데이터프레임 변수명 df_a에 할당하세요.
#  - heart_failure_b.json 파일을 읽어 데이터 프레임 변수명 df_b에 할당하세요.
#  - df_a, df_b를 합쳐서 하나의 데이터프레임으로 만드세요. 판다스의 merge를 활용하세요
#     - 기준 열 (on) : 'person_id'
#     - 합치는 방법(how) : 'inner'

# df_a, df_b에는 존재하지만 df를 만들면서 사라진 데이터는 몇 개인지를 dropped_num 변수에 저장하세요.


import pandas as pd
import os

# 현재 스크립트 파일 기준으로 경로 잡기
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

df_a = pd.read_json(os.path.join(BASE_DIR, 'heart_failure_a.json'))
df_b = pd.read_json(os.path.join(BASE_DIR, 'heart_failure_b.json'))  # 다른 파일도 같은 방식

df = pd.merge(df_a, df_b, on='person_id', how='inner')
dropped_num = len(df_a) - len(df) + len(df_b) - len(df)

set(df_a['person_id']) - set(df['person_id'])

set(df_b['person_id']) - set(df['person_id'])

# # 1
# 박출계수와 나이의 상관관계를 위해 jointplot 그래프를 그리세요.
#  - seaborn의 jontplot을 활용
#  - x축 : ejection_fraction
#  - y축 : age
#  - 색상(hue) : DEATH_EVENT

# 그대로 streamlit으로 구현
# import seaborn as sns
# sns.jointplot(df, x='ejection_fraction', y='age', hue='DEATH_EVENT')

import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.title("박출계수와 나이의 상관관계")

fig = sns.jointplot(data=df, x='ejection_fraction', y='age', hue='DEATH_EVENT')
st.pyplot(fig.figure)