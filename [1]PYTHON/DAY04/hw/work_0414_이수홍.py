# 12.1 딕셔너리 만들기

# 딕셔너리는 {} 중괄호 안에 키:값 형식으로 저장하며 각 키와 값은 ,(콤마)로 구분

lux = {'health' : 490, 'mana' : 334, 'melee' : 550, 'armor' : 18.72}
lux

# 1. 키 이름이 중복되는 경우
# 딕셔너리에 키와 값을 저장할 떄 키가 중복되면 가장 뒤에 있는 값만 사용함
# 따라서 중복되는 키는 저장되지 않음

# 2. 딕셔너리 키의 자료형
# 딕셔너리 키는 문자열, 정수, 실수, 불 연산 가능
# 딕셔너리 값에는 리스트, 딕셔너리 등을 포함하여 모든 자료형을 사용할 수 있음

x = {100 : 'hundred', False : 0, 3.5 : [3.5, 3.5]}
x

# 3. 빈 딕셔너리 만들기
x = {}
x

y = dict()
y

# 4. dict로 딕셔너리 만들기

# 1) 키 = 값 형식
lux1 = dict(health = 490, mana = 334, melee = 550, armor= 18.72)
lux1

# 2) zip 함수 이용하여 키 리스트와 값 리스트를 묶음
lux2 = dict(zip(['health', 'mana', 'melee', 'armor'], [490, 334, 550, 18.72]))
lux2

# 3) 리스트 안에 키와 값 형식의 튜플을 나열하는 방법
lux3 = dict([('health', 490), ('mana', 334), ('melee', 550), ('armor', 18.72)])
lux3

# 4) dict 안에서 중괄호로 딕셔너리를 생성하는 방법
lux4 = dict({'health' : 490 , 'mana' : 334, 'melee' : 550, 'armor' : 18.72})
lux4


# 12.2 딕셔너리의 키에 접근하고 값 할당하기

# 딕셔너리의 키에 접근할 떄는 딕셔너리 뒤에 []대괄호를 사용하며 [] 안에 키를 지정해주면 됨
lux = {'health' : 490 , 'mana' : 334, 'melee' : 550, 'armor' : 18.72}
lux['health']

lux['armor']

lux = {'health' : 490 , 'mana' : 334, 'melee' : 550, 'armor' : 18.72}
lux['health'] = 2037 # 키 'health'의 값을 2037로 변경
lux['mana'] = 1184 # 키 'mana'의 값을 1184로 변경
lux

# 1. 딕셔너리의 키에 값 할당하기
# 딕셔너리는 없는 키에 값을 할당하면 해당 키가 추가되고 값이 할당됨

lux['mana_regen'] = 3.28 
lux

# 딕셔너리는 없는 키에서 값을 가저오려고 하면 에러가 발생

# 2. 딕셔너리에 키가 있는지 확인하기
# in 연산자

lux = {'health' : 490 , 'mana' : 334, 'melee' : 550, 'armor' : 18.72}
'health' in lux
'attack_speed' in lux

# 특정 키가 없는지 확인
'attack_speed' not in lux
'health' not in lux

# 3. 딕셔너리의 키 개수 구하기
lux = {'health' : 490 , 'mana' : 334, 'melee' : 550, 'armor' : 18.72}
len(lux)

len({'health' : 490 , 'mana' : 334, 'melee' : 550, 'armor' : 18.72})


## 12.3 퀴즈

#1. 다음 중 딕셔너리를 만드는 방법으로 올바르지 않은 것을 고르세요.
# a, x = {'a' : 10, 'b' : 20}
# b, x = {'a'=10, 'b'=20}
# c, x = dict()
# d, x = dict(a=10, b=20)
# e. x = dict({'a' : 10, 'b' : 20})

# 정답 : b

#2. 딕셔너리 x = {10 : 'Hello', 'world' : 30} 에서 키 10의 값을 출력하는 방법으로 올바른 것을 고르세요
# a. print(x.Hello)
# b. print(x('hello'))
# c. print(x[Hello])
# d. print(x['Hello'])
# e. print(x[10])

# 정답: e

#3. 다음 코드를 실행했을 때 출력 결과로 올바른 것을 고르세요
fruits = {'apple' : 1500, 'pear' : 3000 , 'grape' : 1400}
fruits['orange'] = 2000
print(fruits['apple'], fruits['orange'])

# 정답: c (1500 2000)

#4. 다음 중 print(len({10:0, 20:1, 30:2, 40:3, 50:4, 60:7}))의 출력 결과로 올바른 것을 고르세요
# a. 12
# b. 0
# c. {10:0, 20:1, 40:3, 50:4, 60:7}
# d. 6
# e. 7

# 정답: d

##=================================================
## 12.4 연습문제: 딕셔너리에 게임 캐릭터 능력치 저장하기
## ================================================

#1. 다음 소스 코드를 완성하여 게임 캐릭터의 체력(health)과 이동 속도(movement speed)가 출력 되게 만드세요

camille = {
    'health' : 575.6,
    'health_regen' : 1.7,
    'mana' : 338.8,
    'mana_regen' :1.63,
    'melee' : 125,
    'attack_damage' : 60,
    'attack_speed' : 0.625,
    'armor' : 26,
    'magic_resistance' : 32.1,
    'movement_speed' : 340
}

print(camille['health'])
print(camille['movement_speed'])

##=================================================
## 12.5 심사 문제 : 딕셔너리에 게임 캐릭터 능력치 저장하기
## ================================================

#2. 표준 입력으로 문자열 여러 개와 숫자(실수) 여러 개가 두 줄로 입력됩니다. 입력된 첫 번째 줄은 키, 두 번째 줄은 값으로 하여
# 딕셔너리를 생성한 뒤 딕셔너리를 출력하는 프로그램을 만드세요. input().split()의 결과를 변수 한 개에 저장하면 리스트로 저장됩니다.

keys = input().split()
values = input().split()

d = {}
for i in range(len(keys)):
    d[keys[i]] = float(values[i])

print(d)


# 24. 문자열 응용하기

# 24.1 문자열 조작하기

# 1. 문자열 바꾸기
s = 'Hello, world!'.replace('world', 'Python')
print(s)

# 2. 문자 바꾸기
table = str.maketrans('aeiou', '12345')
s = 'apple'.translate(table)
print(s)

# 3. 문자열 분리하기
lst = 'apple pear grape pineapple orange'.split()
print(lst)

lst = 'apple, pear, grape, pineapple, orange'.split(', ')
print(lst)

# 4. 구분자 문자열과 문자열 리스트 연결하기
s = ' '.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])
print(s)

s = '-'.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])
print(s)

# 5. 소문자를 대문자로 바꾸기 
s = 'python'.upper()
print(s)

# 6. 대문자를 소문자로 바꾸기 
s = 'python'.lower()
print(s)

# 7. 왼쪽 공백 삭제하기
s = '    Python   '.lstrip()
print(s)

#8. 오른쪽 공백 삭제하기
s = '    Python   '.rstrip()
print(s)

# 9. 양쪽 공백 삭제하기
s = '    Python   '.strip()
print(s)

# 10. 왼쪽의 특정 문자 삭제하기
s = ',  Python.'.lstrip(',.')
print(s)

# 11. 오른쪽의 특정 문자 삭제하기
s = ',  Python.'.rstrip(',.')
print(s)

# 12. 양쪽의 특정 문자 삭제하기
s = ',  Python.'.strip(',.')
print(s)

# 13. 문자열을 왼쪽 정렬하기
s = 'python'.ljust(10)
print(s)

# 14. 문자열을 오른쪽 정렬하기
s = 'python'.rjust(10)
print(s)

# 15. 문자열을 가운데 정렬하기
s = 'python'.center(10)
print(s)

# 16. 메서드 체이닝
s = 'python'.rjust(10).upper()  # 오른쪽 정렬 후 대문자 
print(s)

# 17. 문자열 왼쪽에 0 채우기
s = '35'.zfill(4)  # 숫자 앞에 0 채움
print(s)

s = '3.5'.zfill(6) # 숫자 앞에 0 채움
print(s)

s = 'hello'.zfill(10) # 문자열 앞에 0 채움
print(s)

# 18. 문자열 위치 찾기
s = 'apple pineapple'.find('pl')
print(s)

s = 'apple pineapple'.find('xy')
print(s)

# 19. 오른쪽에서부터 문자열 위치 찾기
s = 'apple pineapple'.rfind('pl')
print(s)

s = 'apple pineapple'.rfind('xy')
print(s)

# 20. 문자열 위치 찾기
s = 'apple pineapple'.index('pl')
print(s)

# 21. 오른쪽에서부터 문자열 위치 찾기
s = 'apple pineapple'.rindex('pl')
print(s)

# 22. 문자열 개수 세기
s = 'apple pineapple'.count('pl')
print(s)

# 24.2 문자열 서식 지정자와 포메팅 사용하기

# 1. 서식 지정자로 문자열 넣기
s = 'I am %s.' % 'james'
print(s)

# 2. 서식 지정자로 숫자 넣기
s = 'I am %d years old.' %20
print(s)

# 3. 서식 지정자로 소수점 표현하기
s = '%f' % 2.3
print(s)

s = '%.2f' % 2.3 # 소수점 둘째자리까지
print(s)

s = '%.3f' % 2.3 # 소수점 셋째자리까지
print(s)

# 4. 서식 지정자로 문자열 정렬하기
s = '%10s' % 'python' # 문자열 길이 10, 오른쪽 정렬
print(s)

s = '%-10s' % 'python' # 문자열 길이 10, 왼쪽 정렬
print(s)

# 5. 서식 지정자로 문자열 안에 값 여러 개 넣기
s = 'Today is %d %s.' % (3, 'April')
print(s)

# 6. format 메서드 사용하기
s = 'Hello, {0}'.format('world!')
print(s)

s = 'Hello, {0}'.format(100)
print(s)

# 7. format 메서드로 값을 여러 개 넣기
s = 'Hello, {0} {2} {1}'.format('Python', 'Script', 3.6)
print(s)

# 8. format 메서드로 같은 값을 여러 개 넣기
s = '{0} {0} {1} {1}'.format('Python' , 'Script')
print(s)

# 9. format 메서드에서 인덱스 생략하기
s = 'Hello, {} {} {}'.format('Python', 'Script', 3.6)
print(s)

# 10. format 메서드에서 인덱스 대신 이름 지정하기
s = 'Hello, {language} {version}'.format(language = 'Python' , version = '3.6')
print(s)

# 11. 문자열 포매팅에 변수를 그대로 사용하기
language = 'Python'
version = '3.6'
print(f'Hello, {language} {version}')

# 12. format 메서드로 문자열 정렬하기
s = '{0:<10}'.format('python')  # 왼쪽 정렬
print(s)

s = '{0:>10}'.format('python') # 오른쪽 정렬
print(s)

# 13. 숫자 개수 맞추기
s = '%03d' % 1 # 세자리수
print(s)

s = '{0:03d}'.format(35) # 세자리수
print(s)

'%08.2f' % 3.6
'{0:08.2f}'.format(150.37) # 총 길이, 소수점 이하 자리수

# 14. 채우기와 정렬을 조합해서 사용하기
s = '{0:0<10}'.format(15) # 길이 10, 왼쪽으로 정렬하고 남는 공간은 0으로 채움
print(s)

s = '{0:0>10}'.format(15) # 길이 10, 오른쪽으로 정렬하고 남는 공간은 0으로 채움
print(s)

s = '{0:0>10.2f}'.format(15) # 길이 10, 오른쪽으로 정렬하고 남는 공간은 0으로 채우고 소수점 자리수는 2자리
print(s)

s = '{0: >10}'.format(15) # 남는 공간을 공백으로 채움
print(s)

s = '{0:>10}'.format(15) # 채우기 부분을 생략하면 공백이 들어감
print(s)

s = '{0:x>10}'.format(15) # 남는 공간을 문자 x로 채움
print(s)

## 24.3 퀴즈

#1. 다음 중 문자열 메서드에 대한 설명으로 잘못된 것을 모두 고르세요.
# a, count는 문자열의 전체 문자 개수를 구한다.  -> count는 특정 문자열의 개수 반환
# b, find는 문자열에서 왼쪽부터 문자열을 찾아서 인덱스를 반환한다.
# c, replace는 문자열 안의 문자열을 다른 문자열로 바꾼다.
# d, split는 문자열을 공백 또는 기준 문자열을 기준으로 분리한다.
# e. index는 문자열의 오른쪽에서부터 문자열을 찾아서 인덱스를 반환한다.

# 정답 : a,e

#2. 다음 코드를 실행했을 때 출력 결과를 고르세요.
# print('Python'.lower().replace('on', 'ON').ljust(10))
# a. '    Python'
# b. 'Python    '
# c. 'PythON    '
# d. 'pythON    '
# e. '    PYTHON'

# 정답: d (-> 전체 lower + on -> ON + 왼쪽 정렬)

#3. 다음 중 문자열 'Hello, Python 3.6'을 만드는 방법으로 올바른 것을 모두 고르세요.
# a. 'Hello, %d 3.6' % 'Python'
# b. '%s, %s 3.6' %('Hello' , 'Python')
# c. '{0}, Python {1}'.format('Hello')
# d. '{hello}, {language} 3.6'.format(hello='Hello', language = 'Python')
# e. '%s%s%s' % ('Hello', 'Python', '3.6')

# 정답: b,d

#4. 다음 중 문자열 '   1675.3000'을 만드는 방법으로 올바른 것을 모두 고르세요. 이 문자열의 길이는 12이고 소수점 이하
#   자릿수는 4자리 입니다. 또한, 오른쪽으로 정렬되어 있고 남은 공간은 공백으로 채워져 있습니다.
# a. '{0:>12.2f}'.format(1675.3)
# b. '{0:>12}'.format(1675.3)
# c. '{0:>12.4f}'.format(1675.3)
# d. '{:>12.4f}'.format(1675.3)
# e. '{:0>12.4f}'.format(1675.3)

# 정답: c,d

##=================================================
## 24.4 연습문제: 파일 경로에서 파일명만 가져오기
## ================================================

#1. 다음 소스 코드를 완성하여 파일 경로에서 파일명만 출력되게 만드세요. 단, 경로에서 폴더의 깊이가 달라지더라도
#   파일명만 출력할 수 있어야 합니다.

path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'
x = path.split("\\")
filename = x[-1]

print(filename)

##=================================================
## 24.5 심사 문제 : 특정 단어 개수 세기
## ================================================

# 표준 입력으로 문자열이 입력됩니다. 입력된 문자열에서 'the'의 개수를 출력하는 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다.)
# 단, 모든 문자가 소문자인 'the'만 찾으면 되며 'them', 'there', 'their' 등은 포함하지 않아햐 합니다.

i = input("")
num = i.split().count('the')
print(num)

##=================================================
## 24.6 심사 문제 : 높은 가격 순으로 출력하기
## ================================================

# 표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있습니다. 입력된
# 가격을 높은 가격순으로 출력하는 프로그램을 만드세요 (input에서 안내 문자열은 출력하지 않아야 합니다.). 이때 
# 가격은 길이를 9로 만든 뒤 오른쪽으로 정렬하고 천단위로 ,(콤마)를 넣으세요.

line = input()
prices = list(map(int,line.split(";")))

sorted_prices = sorted(prices,reverse=True)
price = sorted_prices

for price in sorted_prices:
    print(f"{price:>9,}")


