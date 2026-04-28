## ================================================================
## Unit 34. 클래스 사용하기
## ================================================================

# 객체(object)   : 특정한 개념이나 모양으로 존재하는 것
# 클래스(class)  : 프로그래밍으로 객체를 만들 때 사용하는 것
# 속성(attribute) : 게임 캐릭터의 체력, 마나, 물리 공격력, 주문력 등의 데이터
# 메서드(method) : 게임 캐릭터의 베기, 찌르기 등의 기능

# => 객체지향(object oriented) 프로그래밍

## ----------------------------------------------------------------
## 34.1 클래스와 메서드 만들기
## ----------------------------------------------------------------

# 형식 : class 클래스이름:
#     def 메서드(self):
#         코드

# 클래스는 특정 개념을 표현만 할뿐 사용을 하려면 인스턴스를 생성해야 합니다.

## 34.1.1  메서드 호출하기

# 메서드는 클래스가 아니라 인스턴스를 통해 호출합니다.

## 34.1.3  인스턴스와 객체의 차이점?

# 인스턴스와 객체는 같은 것을 뜻합니다. 보통 객체만 지칭할 때는 객체(object)라고 부릅니다. 
# 하지만 클래스와 연관지어서 말할 때는 인스턴스(instance)라고 부릅니다.

# 내용이 없는 빈 클래스를 만들 때는 코드 부분에 pass를 넣어줍니다.

## ----------------------------------------------------------------
## 34.2 속성 사용하기
## ----------------------------------------------------------------

# 속성(attribute)을 만들 때는 __init__ 메서드 안에서 self.속성에 값을 할당

# 형식 : class 클래스이름:
#    def __init__(self):
#        self.속성 = 값

class Person:
    def __init__(self):             # 인스턴스(객체)를 초기화합니다.
        self.hello = '안녕하세요.'
 
    def greeting(self):
        print(self.hello)
 
james = Person()
james.greeting()    # 안녕하세요.

## 34.2.1  self의 의미

#  self는 인스턴스 자기 자신을 의미합니다.

## 34.2.2  인스턴스를 만들 때 값 받기

#  형식 : class 클래스이름:
#    def __init__(self, 매개변수1, 매개변수2):
#        self.속성1 = 매개변수1
#        self.속성2 = 매개변수2

class Person:
    def __init__(self, name, age, address):
        self.hello = '안녕하세요.'
        self.name = name
        self.age = age
        self.address = address
 
    def greeting(self):
        print('{0} 저는 {1}입니다.'.format(self.hello, self.name))
 
maria = Person('마리아', 20, '서울시 서초구 반포동')
maria.greeting()    # 안녕하세요. 저는 마리아입니다.
 
print('이름:', maria.name)       # 마리아
print('나이:', maria.age)        # 20
print('주소:', maria.address)    # 서울시 서초구 반포동

## ----------------------------------------------------------------
## 34.3 비공개 속성 사용하기
## ----------------------------------------------------------------

## 비공개 속성 : 이름이 밑줄 2개로 시작해야 함 __속성
## 형식 : class 클래스이름:
##    def __init__(self, 매개변수)
##        self.__속성 = 값

# class Person:
#     def __init__(self, name, age, address, wallet):
#         self.name = name
#         self.age = age
#         self.address = address
#         self.__wallet = wallet    # 변수 앞에 __를 붙여서 비공개 속성으로 만듦
#  
# maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
# maria.__wallet -= 10000    # 클래스 바깥에서 비공개 속성에 접근하면 에러가 발생함

class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet    # 변수 앞에 __를 붙여서 비공개 속성으로 만듦
 
    def pay(self, amount):
        self.__wallet -= amount   # 비공개 속성은 클래스 안의 메서드에서만 접근할 수 있음
        print('이제 {0}원 남았네요.'.format(self.__wallet))
 
maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.pay(3000)

## 비공개 속성은 클래스 바깥으로 드러내고 싶지 않은 값에 사용함

## ----------------------------------------------------------------
## 34.4 퀴즈
## ----------------------------------------------------------------

## ================================================================
## 1. 다음 클래스의 greeting 메서드를 호출하기 위한 방법으로 올바른 것을 고르세요.
##  class Person:
##    def greeting(self):
##        print('Hello')
## ================================================================
## a, Person.greeting()
## b, greeting()
## c, maria = Person
##    maria.greeting()
## d, maria = Person()
##    maria.greeting()
## e, Person(greeting)

## 정답 : d

## ================================================================
## 2. 클래스로 인스턴스를 만들 때 호출되는 메서드는 무엇인가요? 
## (메서드 뒤의 괄호는 생략하고 메서드 이름만 입력)
## ================================================================

## 정답 :  __init__

## ================================================================
## 3. 다음과 같이 Person 클래스가 있습니다. 클래스에서 다른 메서드를 만들었을 때 
##    인스턴스 속성 name에 접근하기 위한 방법으로 올바른 것을 고르세요.
##    class Person:
##     def __init__(self, name):
##        self.name = name
## ================================================================
## a, name
## b, self
## c, Person.name
## d, self[name]
## e, self.name

## 정답 : e

## ================================================================
## 4. 클래스의 메서드 def __init__(self):에서 속성을 만들려고 합니다. 
##    다음 중 비공개 속성을 고르세요.
## ================================================================
## a, self.name
## b, self._name
## c, self.__name
## d, self.__name__
## e, self.name__

## 정답 : c

## ----------------------------------------------------------------
## 34.5 연습문제: 게임 캐릭터 클래스 만들기
## ----------------------------------------------------------------
## 다음 소스 코드에서 클래스를 작성하여 게임 캐릭터의 능력치와 '베기'가 출력되게 만드세요.
                                            
class Knight :
        def __init__(self,health,mana,armor):
            self.health = health
            self.mana = mana
            self.armor = armor
        
        def slash(self):
            print('베기')

x = Knight(health=542.4, mana=210.3, armor=38)
print(x.health, x.mana, x.armor)
x.slash()

## ----------------------------------------------------------------
## 34.6 심사문제: 게임 캐릭터 클래스 만들기
## ----------------------------------------------------------------
## 표준 입력으로 게임 캐릭터 능력치(체력, 마나, AP)가 입력됩니다. 
## 다음 소스 코드에서 애니(Annie) 클래스를 작성하여 티버(tibbers) 스킬의 피해량이 출력되게 만드세요. 
## 티버의 피해량은 AP * 0.65 + 400이며 AP(Ability Power, 주문력)는 마법 능력치를 뜻합니다.


class Annie:
    def __init__(self,health,mana,ability_power):
        self.health = health
        self.mana = mana
        self.ability_power = ability_power
    
    def tibbers(self):
        self.damage = self.ability_power * 0.65 + 400
        print(f"티버: 피해량 {self.damage}")

health, mana, ability_power = map(float, input().split())
 
x = Annie(health=health, mana=mana, ability_power=ability_power)
x.tibbers()

## ================================================================
## Unit 35. 클래스 속성과 정적, 클래스 메서드 사용하기
## ================================================================-

## ----------------------------------------------------------------
## 35.1 클래스 속성과 인스턴스 속성 알아보기
## ----------------------------------------------------------------
## 인스턴트 속성  : __init__ 메서드
## 클래스 속성 : class 클래스이름:
##                 속성 = 값

## 35.1.1  클래스 속성 사용하기

class Person:
    bag = []   # 속성 = 값
 
    def put_bag(self, stuff):
        Person.bag.append(stuff)
 
james = Person()
james.put_bag('책')
 
maria = Person()
maria.put_bag('열쇠')
 
print(james.bag)
print(maria.bag)

## ['책', '열쇠']
## ['책', '열쇠']

## 클래스 속성은 클래스에 속해 있으며 모든 인스턴스에서 공유합니다.


## 35.1.2  인스턴스 속성 사용하기
class Person:
    def __init__(self):
        self.bag = []
 
    def put_bag(self, stuff):
        self.bag.append(stuff)
 
james = Person()
james.put_bag('책')
 
maria = Person()
maria.put_bag('열쇠')
 
print(james.bag)
print(maria.bag)

## ['책']
## ['열쇠']

## 클래스 속성: 모든 인스턴스가 공유. 인스턴스 전체가 사용해야 하는 값을 저장할 때 사용
## 인스턴스 속성: 인스턴스별로 독립되어 있음. 각 인스턴스가 값을 따로 저장해야 할 때 사용

## 35.1.3  비공개 클래스 속성 사용하기
## 형식 : class 클래스이름:
##    __속성 = 값    # 비공개 클래스 속성

class Knight:
    __item_limit = 10    # 비공개 클래스 속성
 
    def print_item_limit(self):
        print(Knight.__item_limit)    # 클래스 안에서만 접근할 수 있음
 
 
x = Knight()
x.print_item_limit()    # 10
 
# print(Knight.__item_limit)    # 클래스 바깥에서는 접근할 수 없음

## 비공개 클래스 속성은 클래스 바깥으로 드러내고 싶지 않은 값에 사용합니다.

## ----------------------------------------------------------------
## 35.2 정적 메서드 사용하기
## ----------------------------------------------------------------
## 정적 메서드 : 정적 메서드는 매개변수에 self를 지정하지 않습니다.
## 형식 : class 클래스이름:
##    @staticmethod   # @ : 데코레이터
##    def 메서드(매개변수1, 매개변수2):
##        코드

class Calc:
    @staticmethod
    def add(a, b):
        print(a + b)
 
    @staticmethod
    def mul(a, b):
        print(a * b)
 
Calc.add(10, 20)    # 클래스에서 바로 메서드 호출
Calc.mul(10, 20)    # 클래스에서 바로 메서드 호출

## 정적 메서드는 self를 받지 않으므로 인스턴스 속성에는 접근할 수 없습니다. 
## 그래서 보통 정적 메서드는 인스턴스 속성, 인스턴스 메서드가 필요 없을 때 사용합니다.

## ----------------------------------------------------------------
## 35.3 클래스 메서드 사용하기
## ----------------------------------------------------------------
## 클래스 메서드 : 클래스 메서드는 첫 번째 매개변수에 cls를 지정해야 합니다
## 형식 : class 클래스이름:
##    @classmethod
##    def 메서드(cls, 매개변수1, 매개변수2):
##        코드

class Person:
    count = 0    # 클래스 속성
 
    def __init__(self):
        Person.count += 1    # 인스턴스가 만들어질 때
                             # 클래스 속성 count에 1을 더함
 
    @classmethod
    def print_count(cls):
        print('{0}명 생성되었습니다.'.format(cls.count))    # cls로 클래스 속성에 접근
 
james = Person()
maria = Person()
 
Person.print_count()    # 2명 생성되었습니다.

## 클래스 메서드는 메서드 안에서 클래스 속성, 클래스 메서드에 접근해야 할 때 사용합니다.

## ----------------------------------------------------------------
## 35.4 퀴즈
## ----------------------------------------------------------------

## ================================================================
## 1. 다음 중 클래스 바깥에서 클래스 속성 x에 접근하는 방법으로 올바른 것을 고르세요.
##  class Person:
##    x = {}
## ================================================================
## a, Person.x
## b, Person(x)
## c, x
## d, self.x
## e, Person['x']

## 정답 : a

## ================================================================
## 2. 다음 중 정적 메서드로 올바른 것을 고르세요.
## ================================================================
## a, def print_count(self):
##    print(self.count)
## b, @staticmethod
## def sub(self, a, b):
##     print(a - b)
## c, @staticmethod
## def div(a, b):
##     print(a / b)
## d, @staticmethod
## def add(cls, a, b)
##     print(a + b)
## e, def print_count(cls):
##     print(cls.count)

## 정답 : c

## ================================================================
## 3. 다음 중 클래스 메서드에 대한 설명으로 잘못된 것을 고르세요.
## ================================================================
## a, 클래스 메서드는 클래스.메서드() 형식으로 호출한다.
## b, 클래스 메서드는 위에 @classmethod를 붙여서 만든다.
## c, 클래스 메서드의 첫 번째 매개변수는 self이며 현재 인스턴스가 들어온다.
## d, 클래스 메서드는 인스턴스 없이 호출할 수 있다.   ----★
## e, 클래스 메서드는 위에 @staticmethod를 붙여서 만든다.

## 정답 : c,e

## ----------------------------------------------------------------
## 35.5 연습문제: 날짜 클래스 만들기
## ----------------------------------------------------------------
## 다음 소스 코드에서 Date 클래스를 완성하세요. 
## is_date_valid는 문자열이 올바른 날짜인지 검사하는 메서드입니다. 
## 날짜에서 월은 12월까지 일은 31일까지 있어야 합니다.

class Date:
    @staticmethod   # 정적 메서드
    def is_date_valid(date_string):
        year, month, day = map(int,date_string.split('-'))
        return month <=12 and day <= 31   # 월, 일 반환 (연도는 조건 없음)

if Date.is_date_valid('2000-10-31'): 
    # 클래스에 직접 접근 보다는 문자열이 올바른 형식인지만 검사하면 됨 (정적 메서드)
    print('올바른 날짜 형식입니다.')
else:
    print('잘못된 날짜 형식입니다.')

## ----------------------------------------------------------------
## 35.6 심사문제: 시간 클래스 만들기
## ----------------------------------------------------------------
## 표준 입력으로 시:분:초 형식의 시간이 입력됩니다. 
## 다음 소스 코드에서 Time 클래스를 완성하여 시, 분, 초가 출력되게 만드세요. 
## from_string은 문자열로 인스턴스를 만드는 메서드이며 is_time_valid는 문자열이 올바른 시간인지 검사하는 메서드입니다. 
## 시간은 24시까지, 분은 59분까지, 초는 60초까지 있어야 합니다. 
## 정답에 코드를 작성할 때는 class Time:에 맞춰서 들여쓰기를 해주세요.

class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    # from_string은 문자열로 인스턴스를 만드는 메서드 (클래스)
    @classmethod
    def from_string(cls,time_string):
        hour, minute, second = map(int,time_string.split(':'))
        return cls(hour,minute,second)

    # is_time_valid는 문자열이 올바른 시간인지 검사하는 메서드 (정적)
    @staticmethod   # 정적 메서드
    def is_time_valid(time_string):
        hour, minute, second = map(int,time_string.split(':'))
        return hour <=24 and minute <=59 and second <=60

time_string = input()
 
if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')

