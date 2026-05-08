# Series, DataFrame 연산

# 【사용 데이터 1 】 --------------------------------------------------------------------- 
# 다음 조건에 맞게 midterm Series와 final Series를 생성하세요. 

import pandas as pd

# midterm : 중간고사 점수를 저장합니다. 
# 인덱스 값
# 김민수 80
# 이서연 90
# 박지훈 75
# 최유진 88

data1 = { '김민수' : 80 , 
         '이서연' : 90 ,
         '박지훈' : 75 ,
         '최유진' : 88}

midterm = pd.Series(data1)
print('-' * 15)
print(midterm)

# final : 기말고사 점수를 저장합니다. 
# 인덱스 값
# 김민수 85
# 이서연 92
# 박지훈 78
# 최유진 95
# 조건: midterm과 final은 모두 학생 이름을 인덱스로 갖는 Series로 생성하세요. 

data2= { '김민수' : 85 , 
         '이서연' : 92 ,
         '박지훈' : 78 ,
         '최유진' : 95}

final = pd.Series(data2)
print('-' * 15)
print(final)

# -------------------------------------------------------------------------------------- 

# 문제 01) midterm과 final을 더하여 학생별 총점을 출력하세요.
print('문제01') 
print(midterm + final)
print('-' * 15)

# 문제 02) final에서 midterm을 빼서 기말고사 점수 변화량을 출력하세요.
print('문제02')  
print(final - midterm)
print('-' * 15)

# 문제 03) midterm과 final을 이용하여 학생별 평균 점수를 출력하세요. 
print('문제03') 
print((midterm + final) / 2)
print('-' * 15)

# 문제 04) midterm의 모든 점수에 5점을 더한 결과를 출력하세요. 
print('문제04') 
print(midterm + 5)
print('-' * 15)

# 문제 05) final 점수가 90점 이상인 학생을 True/False로 출력하세요. 
print('문제05') 
print(final>=90)
print('-' * 15)

# 문제 06) final 점수가 90점 이상인 학생의 점수만 출력하세요.
print('문제06') 
print(final[final>=90])
print('-' * 15)

# 【사용 데이터 2 】 --------------------------------------------------------------------- 
# 다음 조건에 맞게 class_a DataFrame과 class_b DataFrame을 생성하세요. 
# class_a : 아래 학생별 과목 점수를 저장합니다. 

# 이름 국어 영어 수학
# 김민수 80 85 90
# 이서연 90 88 95
# 박지훈 75 79 70

# 조건: 학생 이름을 인덱스로 갖는 DataFrame으로 생성하세요.

data_a = {
           '국어' : [80,90,75],
           '영어' : [85,88,79],
           '수학' : [90,95,70]
           }

class_a = pd.DataFrame(data_a,index=['김민수', '이서연', '박지훈'])
print('class_a') 
print(class_a)
print('-' * 15)

# class_b : 아래 학생별 과목 점수를 저장합니다.
#  
# 이름 국어 영어 수학
# 최유진 88 90 93
# 정하늘 76 82 80
# 한지민 92 85 96

# 조건: 학생 이름을 인덱스로 갖는 DataFrame으로 생성하세요. 

data_b = { 
           '국어' : [88,76,92],
           '영어' : [90,82,85],
           '수학' : [93,80,96]
           }

class_b = pd.DataFrame(data_b,index=['최유진', '정하늘', '한지민'])
print('class_b') 
print(class_b)
print('-' * 15)

# -------------------------------------------------------------------------------------- 
# 문제 07) class_a DataFrame의 모든 점수에 10점을 더한 결과를 출력하세요.
print('문제07')  
print(class_a[['국어', '영어' ,'수학']] + 10)
print('-' * 15)

# 문제 08) class_a DataFrame에 총점 열을 추가하세요. 총점은 국어 + 영어 + 수학으로 계산합니다.
print('문제08')
class_a['총점'] = class_a['국어'] +  class_a['영어'] + class_a['수학']
print(class_a)
print('-' * 15)

# 문제 09) class_a DataFrame에 평균 열을 추가하세요. 평균은 총점 / 3으로 계산합니다.
print('문제09')
class_a['평균'] = class_a['총점'] / 3
print(class_a)
print('-' * 15)

# 문제 10) class_a DataFrame에서 각 점수가 80점 이상인지 True/False로 출력하세요. 
print('문제10')
print(class_a>=80)
print('-' * 15)

# 문제 11) class_a DataFrame에서 수학 점수가 80점 이상인 학생만 출력하세요
print('문제11')
print(class_a[class_a['수학']>=80])
print('-' * 15)

# 문제 12) class_a와 class_b를 행 방향으로 연결하여 all_students DataFrame을 생성하세요.
print('문제12')
all_students = class_a.add(class_b,fill_value=0)
print(all_students)
print('-' * 15)

# 문제 13) all_students DataFrame에 총점과 평균 열을 추가하세요.
print('문제13')
all_students['총점'] = all_students['국어'] +  all_students['영어'] + all_students['수학']
all_students['평균'] = all_students['총점'] / 3
print(all_students)
print('-' * 15)

# 문제 14) 다음 두 Series를 생성한 후 더하세요. 
# 조건
# - s1과 s2는 모두 문자열 인덱스를 갖는 Series로 생성하세요. 
# - s1 Series의 인덱스는 A, B, C 이고 데이터는 10, 20, 30
# - s2 Seires의 인덱스는 B, C, D 이고 데이터는 1, 2, 3

print('문제14')
data1 = {
    'A' : 10,
    'B' : 20,
    'C' : 30
}

s1 = pd.Series(data1)
print(s1)

data2 = {
    'B' : 1,
    'C' : 2,
    'D' : 3
}

s2 = pd.Series(data2)
print(s2)
print('-' * 15)

# 문제 15) 다음 조건을 모두 수행하세요.
print('문제15') 
# → midterm과 final을 이용하여 exam DataFrame을 생성하세요. 
exam = pd.DataFrame([midterm,final]).T
print(exam)
print('-' * 15)

# → exam DataFrame의 컬럼명은 중간, 기말로 지정하세요.
exam = exam.rename(columns={0:'중간', 1:'기말'})
print(exam)
print('-' * 15)

# → 총점 열을 추가하세요. 
exam['총점'] = exam['중간'] + exam['기말']
print(exam)
print('-' * 15)

# → 평균 열을 추가하세요. 
exam['평균'] = exam['총점'] / 2
print(exam)
print('-' * 15)

# → 기말 점수가 90점 이상인 학생만 출력하세요.
print(exam[exam['기말']>=90])
print('-' * 15)
 
# → 평균 점수가 높은 순서대로 정렬하세요.
ndf = exam['평균'].sort_values(ascending=False)
print(ndf)
print('-' * 15)
