## ===========================================================
##               객체지향프로그래밍 언어 -> 파이썬
##
## -> 모든 데이터 관련 자료형 --- 클래스로 구현
## -> 객체지향언어 특징      --- 정보 은닉, 다형성, 상속 
## ===========================================================
## -> 정보 은닉 특징
##    [기본] 속성과 메서드를 숨기기/감추기
##          공개용 속성과 메서드가 따로 존재
## -> 숨겨진 속성을 사용하는 방법 : Getter/Setter 메서드
## ===========================================================

class Car:

    # 자동차 인스턴스/객체의 속성 초기화 메서드
    def __init__(self, user, number,ckey):
        self.user   = user 
        self.number = number
        self.__ckey = ckey     ## 비공개 속성 저장 : 클래스 내에서만 사용 가능
    # 인스턴스 메서드
    def forward(self):
        print("forward() 호출") 
        print(f"{self.number} 번호 자동차가 앞으로 전진한다.")
        print(f'cKey => {self.__ckey}')

    ##Getter/Setter 메서드 : 비공개 속성의 외부 접근 가능 메서드
    def get_ckey(self):
        return self.__ckey
    
    def set_ckey(self,nkey):
        self.__ckey = nkey
## ----------------------------------------------------------- 
## 객채 즉, Car 인스턴스 생성  :  변수명 = 클래스이름()
## -> 생성자 메서드 : 클래스이름() ==> 연결 ==>_ _init_ _()
## ----------------------------------------------------------- 
myCar   = Car('홍길동', '12가 1212', '998877')

# ## 자동차 인스턴스의 메서드 사용
myCar.forward()

# ## 자동차 인스턴스/객체의 속성 읽기 
print("나의 자동차 번  호 : ", myCar.number)
print("나의 자동차 소유자 : ", myCar.user)
# print("나의 자동차 키 : ", myCar.__ckey)   ## 비공개 속성이기 때문에 class 밖에서 사용 x
print("나의 자동차 키 : ", myCar.get_ckey()) ## 간접 접근

# ## 자동차 인스턴스/객체의 속성 변경
myCar.user = "나의차"
myCar.__ckey = '111111'                      ## <= 새로운 __ckey 변수 생성해버림!!

myCar.set_ckey("새로운 키")                   ## <= 비공개 속성 변수값 변경됨

print("나의 자동차 소유자 : ", myCar.user)
print("나의 자동차 키    : ", myCar.__ckey)
print(myCar.__dict__)

youCar = Car("마징가", "1111", "998877")
print("너의 자동차 소유자 : ", youCar.user)
#print("너의 자동차 키    : ", youCar.__ckey)
print(myCar.__dict__)