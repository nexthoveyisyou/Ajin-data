## ==========================================================
##                    상속 (Inheritance)
##  -> 다중 상속
##     * 파이썬은 다중 상속 허용함
##     * 형식 : 자식 클래시 이름 ( 부모 클래스 1, 부모 클래스 2, ... , 부모클래스 n)
##     * 규칙
##       - 메서드/속성 사용 시 실행규칙
##       - (1) 자신의 클래스 안에서 메서드와 속성을 찾기
##       - (2) 자신의 클래스에 존재하지 않으면 부모 클래스1
##       - (3) 부모 클래스 1번에 없으면 부모 클래스 2번으로
##       - (4) 부모 클래스 n번에 없으면 에러 발생 
## ==========================================================

class Animal:
    def hello(self):
        print("안녕! 나는 Animal이야!!")


class Dog(Animal):
    ## 상속 관계 메서드를 재정의 : 오버라이딩
    def hello(self):
        print("안녕! 나는 Dog!!")

class Cat(Animal):
    ## 상속 관계 메서드를 재정의 : 오버라이딩
    def hello(self):
        print("안녕! 나는 Cat!!")

class NewAnimal(Dog, Cat): # 다중 상속
    pass

## ==========================================================
## 인스턴스 생성 및 사용
## ==========================================================
## => 인스턴스 생성
dog  = Dog()
cat  = Cat()
data = list()
new_ani = NewAnimal()

## => 부모 자식 관계 검사 issubclass(자식 클래스 이름, 부모 클래스 이름)
print(f" issubclass(Dog,Animal)  : {issubclass(Dog,Animal)}")
print(f" issubclass(Cat,Animal)  : {issubclass(Cat,Animal)}")
print(f" issubclass(Cat,Dog)     : {issubclass(Cat,Dog)}")

 

## => 메서드 사용
cat.hello()
dog.hello()
new_ani.hello()

## _ _ dict _ _ : 속성, 메서드 리스트 추출
print(new_ani.__dict__)
print(NewAnimal.__dict__)

print(cat.__dict__)
print(Cat.__dict__)

## 메서드 호출 순서를 알려주는 함수 mro
print("Cat.mro()=>", Cat.mro())
print("NewAnimal.mro()=>", NewAnimal.mro())