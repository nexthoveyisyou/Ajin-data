## =============================================================================
##                          DataFrame에서 행/열 선택
## =============================================================================
## [1] 모듈 로딩
import pandas as pd

## [2] DataFrame 인스턴스 생성
dataDF1 = pd.DataFrame( [[10, 20, 30, 40.],
[11, 22, 33, 44.]])

dataDF2 = pd.DataFrame( [[10, 20, 30, 40.],[11, 22, 33, 44.]],
                        columns=['영','일','이','삼'],
                        index=['row0', 'row1'])

## => 생성된 인스턴스 확인
print("\n dataDF1", dataDF1, sep='\n')
print("\n dataDF2", dataDF2, sep='\n')


## [3] 열 선택 -------------------------------------------------------
## [3-1] 1개 열 선택
one_col = dataDF2['일']             #라벨 인덱스
print("\n one_col", one_col, sep='\n')

# one_col = dataDF2[1]                #위치 인덱스    => 오류
# print("\n one_col", one_col, sep='\n') 

one_col = dataDF1[1]                #위치 인덱스    => 가능
print("\n one_col", one_col, sep='\n')   

## [3-2] 2개 이상 열 선택 - 인덱스 리스트
two_cols = dataDF2[['삼','일']]          #라벨 인덱스
print("\n two_cols", two_cols, sep='\n')

# two_col = dataDF2[[3,1]]               #위치 인덱스   <=== 지정된 컬럼 이름만 가능!!(오류)
two_cols = dataDF1[[3,1]]
print("\n two_cols", two_cols, sep='\n')    


## [3-3] 2개 이상 열 선택 - 인덱스 슬라이싱  - iloc, loc 둘 다 가능!
##       df변수명.loc[행선택, 시작라벨인덱스 : 끝라벨인덱스]
two_cols = dataDF2.loc[ :, '일':'삼']             #라벨 인덱스  ## 일, 이, 삼
print("\n two_cols", two_cols, sep='\n')

two_cols = dataDF2.loc[ :, '일':'삼' : 2]         #라벨 인덱스  ## 일, 삼  (2칸 간격)
print("\n two_cols", two_cols, sep='\n')

##       df변수명.iloc[행선택, 시작위치인덱스 : 끝위치인덱스]
two_cols = dataDF2.iloc[:,1:]                       #위치 인덱스  ## 1<= ~ <4(끝까지)
print("\n two_cols", two_cols, sep='\n')