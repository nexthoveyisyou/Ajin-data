## ===============================================================
## 예제 3-1) 데이터 살펴보기
## ===============================================================
import pandas as pd

df = pd.read_csv('./DATA/auto_mpg.csv')

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 
              'acceleration', 'model year', 'origin', 'name']

print(df.head())

# 마지막 5개 행
print(df.tail())

# df의 모양과 크기 확인 : (행의 개수, 열의 개수)를 튜플로 반환
print(df.shape)

# 데이터프레임 df의 내용 확인
print("\n")
df.info()

# 데이터프레임 df의 자료형 확인
print("\n")
print(df.dtypes)

# 시리즈 (mog 열)의 자료형 확인
print("\n")
print(df['mpg'].dtypes)

# 데이터프레임 df의 요약 통계정보 확인
print("\n")
print(df.describe())    # 숫자형 데이터에 대해서만 요약 통계가 출력됨

# 데이터프레임의 모든 열(숫자열, 문자열 등)을 포함
print("\n")
print(df.describe(include = 'all'))

# 숫자형 데이터(int,float)만을 포함
print("\n")
print(df.describe(include='number'))

# 문자열(object)만을 포함
print("\n")
print(df.describe(include='object'))

# 특정 자료형을 포함하는 열만을 선택 => 숫자형과 문자열로 구성된 열을 대상
print("\n")
print(df.describe(include = ['number', 'object']))

## ===============================================================
## 예제 3-2) 데이터 개수 확인
## ===============================================================

# 데이터프레임 df의 각 열이 가지고 있는 원소 개수 확인
print("\n")
print(df.count())

# df.count() 가 반환하는 객체 타입 출력
print("\n")
print(type(df.count()))

# 데이터프레임 df의 특정 열이 가지고 있는 고유값의 개수 확인
print("\n")
unique_values = df['origin'].value_counts()
print(unique_values)

# 데이터프레임 df의 특정 열이 가지고 있는 고유값의 비율을 확인 
print("\n")
unique_values_ratio = df['origin'].value_counts(normalize=True) # 고유값의 상대적인 비율을 확인 : normalize
print(unique_values_ratio)

# 데이터프레임 df의 특정 열이 가지고 있는 고유값의 비율을 확인 (백분율로 변환)
print("\n")
unique_values_percentage = (df['origin'].value_counts(normalize=True) * 100).round(1) # round(1) 메소드를 적용하여 소수점 이하 첫째 자리로 반올림
print(unique_values_percentage)

## ===============================================================
## 예제 3-3) 통계 함수
## ===============================================================

# 평균값
print('\n')
print(df.mean(numeric_only=True))
print('\n')
print(df['mpg'].mean())
print(df.mpg.mean())
print('\n')
print(df[['mpg','weight']].mean())

# 중앙값
print('\n')
print(df.median(numeric_only=True))
print('\n')
print(df['mpg'].median())

# 최댓값
print('\n')
print(df.max(numeric_only=True))
print('\n')
print(df['mpg'].max())

# 최솟값
print('\n')
print(df.min(numeric_only=True))
print('\n')
print(df['mpg'].min())

# 표준편차
print('\n')
print(df.std(numeric_only=True))
print('\n')
print(df['mpg'].std())

# 상관계수
print('\n')
print(df.corr(numeric_only=True))
print('\n')
print(df[['mpg','weight']].corr())


## ===============================================================
## 예제 5-1) 누락 데이터 확인
## ===============================================================
import seaborn as sns

#titanic 데이터셋 가져오기
df = sns.load_dataset('titanic')

# 첫 5행 출력
print('\n')
print(df.head())

# 데이터프레임 개요
print('\n')
df.info()

# deck 열의 NaN 개수 계산하기
print('\n')
print(df['deck'].value_counts(dropna=False))

# isnull() 메소드로 누락 데이터 찾기
print('\n')
print(df.head().isnull())
print('\n')

# notnull() 메소드로 누락 데이터 찾기
print('\n')
print(df.head().notnull())
print('\n')

# isnull() 메소드로 누락 데이터 개수 구하기
print('\n')
print(df.head().isnull().sum(axis=0))
print('\n')

# ## missingno 라이브러리 활용
import missingno as msno
import matplotlib.pyplot as plt

# # 매트릭스 그래프
# msno.matrix(df)
# plt.show()

# # 막대 그래프
# msno.bar(df)
# plt.show()

# # 히트맵
# msno.heatmap(df)
# plt.show()

# # 덴드로그램
# msno.dendrogram(df)
# plt.show()

# 기존 방식(np.nan): 정수형 자료가 float로 변환됨
print('\n')
ser1 = pd.Series([1,2,None])
print(ser1)

# Nullable 자료형 : 정수형이 그대로 유지됨(결측값은 pd.NA로 표현)
print('\n')
ser2 = pd.Series([1,2,None], dtype="Int64")
print(ser2)

## ===============================================================
## 예제 5-2) 누락 데이터 제거
## ===============================================================

# isnull() 메소드를 합계로 집계하여 각 열의 NaN 개수 계산하기
print('\n')
print(df.isnull().sum())

# NaN 값이 500개 이상인 열을 모두 삭제 - deck 열 (891개 중 688개의 NaN 값)
print('\n')
df_thresh = df.dropna(axis=1, thresh=500)
print(df_thresh.columns)

# age 열에 나이 데이터가 없는 모든 행 삭제 - age 열(891개 중 177개의 NaN 값)
print('\n')
df_age = df.dropna(subset=['age'], how='any', axis = 0)
print(len(df_age))

# age 열, deck 열 양쪽 모두 데이터가 없는 행 삭제
print('\n')
df_age_deck = df.dropna(subset=['age','deck'], how='all', axis=0)
print(len(df_age_deck))

## ===============================================================
## 예제 5-3) 평균으로 누락 데이터 바꾸기
## ===============================================================

# age 열의 첫 10개 데이터 출력(5행에 NaN 값)
print('\n')
print(df['age'].head(10))

# age 열의 NaN값을 다른 나이 데이터의 평균으로 변경하기
mean_age = df['age'].mean(axis=0)    # age 열의 평균 계산(NaN 값 제외)
df['age'] = df['age'].fillna(mean_age) 

# age 열의 첫 10개 데이터 출력(5 행에 NaN 값이 평균으로 대체)
print('\n')
print(df['age'].head(10))

## ===============================================================
## 예제 5-4) 가장 많이 나타나는 값으로 바꾸기
## ===============================================================

# embark_town 열의 829행의 NaN 데이터 출력
print('\n')
print(df['embark_town'][825:830])

# embark_town 열의 최빈값(승선도시 중에서 가장 많이 출현한 값) 찾기
print('\n')
most_freq = df['embark_town'].value_counts(dropna=True).idxmax()
print(most_freq)

# embark_town 열의 최빈값(승선도시 중에서 가장 많이 출현한 값) 찾기
most_freq2 = df['embark_town'].mode()[0]
print(most_freq2)

# embark_town 열의 NaN값을 최빈값으로 대체하기
print('\n')
df['embark_town'] = df['embark_town'].fillna(most_freq)

# embark_town 열 829행의 NaN 데이터 출력 (NaN 값이 most_freq 값으로 대체)
print(df['embark_town'][825:830])

# 데이터프레임 복제하기
df2 = df.copy()

## ===============================================================
## 예제 5-5) 이웃하고 있는 값으로 바꾸기
## ===============================================================

# embark_town 열의 829행의 NaN 데이터 출력
print('\n')
print(df['embark_town'][825:831])

# embark_town 열의 NaN값을 바로 앞에 있는 828행의 값으로 변경하기
df['embark_town'] = df['embark_town'].ffill()
print('\n')
print(df['embark_town'][825:831])

# embark_town 열의 NaN값을 바로 뒤에 있는 831행의 값으로 변경하기
df2['embark_town'] = df2['embark_town'].bfill()
print('\n')
print(df2['embark_town'][825:831])

## ===============================================================
## 예제 5-6) 중복 데이터 확인
## ===============================================================

df = pd.DataFrame({'c1' : ['a', 'a', 'b', 'a', 'b'],
                   'c2' : [1,1,1,2,2],
                   'c3':  [1,1,2,2,2]})

print('\n')
print(df)

# 데이터프레임 전체 행 데이터 중에서 중복값 찾기(기본값, keep='first')
# 2개의 중복행 중에서 가장 처음에 나오는 0행은 중복이 아니라고 판정, 이후에 나오는 중복행들을 모두 True로 표시

df_dup_first = df.duplicated()
print('\n')
print(df_dup_first)

# 데이터프레임 전체 행 데이터 중에서 중복값 찾기(기본값, keep='last')
df_dup_last = df.duplicated(keep='last')
print('\n')
print(df_dup_last)

# 데이터프레임 전체 행 데이터 중에서 중복값 찾기(keep=False)
df_dup_false = df.duplicated(keep=False)
print('\n')
print(df_dup_false)

# 데이터프레임의 특정 열 데이터에서 중복값 찾기
col_dup = df['c2'].duplicated()
print('\n')
print(col_dup)

# 데이터프레임의 특정 열 데이터에서 중복값 찾기
col_dup2 = df.duplicated(subset=['c2'])
print('\n')
print(col_dup2)

## ===============================================================
## 예제 5-7) 중복 데이터 제거
## ===============================================================

# 데이터프레임에서 중복 행을 제거(기본값, keep = 'first')
df2 = df.drop_duplicates()
print('\n')
print(df2)

# 데이터프레임에서 중복 행을 제거(keep='last')
df3 = df.drop_duplicates(keep='last')
print('\n')
print(df3)

# 데이터프레임에서 중복 행을 제거(keep='False')
df4 = df.drop_duplicates(keep=False)
print('\n')
print(df4)

# c2,c3 열을 기준으로 중복 행을 제거
df5 = df.drop_duplicates(subset=['c2', 'c3'])
print('\n')
print(df5)

# c2,c3 열을 기준으로 중복 행을 제거(중복 데이터를 모두 제거)
df6 = df.drop_duplicates(subset=['c2', 'c3'],keep=False)
print('\n')
print(df6)