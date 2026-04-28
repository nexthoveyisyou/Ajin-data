## -------------------------------------
## 부모 클래스
## -------------------------------------
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"저는 {self.name}예요."

## -------------------------------------
## 자식 클래스들 — 같은 speak()를 각자 다르게 구현
## -------------------------------------
class Dog(Animal):
    def speak(self):
        return f"멍멍! 저는 {self.name}예요."

class Cat(Animal):
    def speak(self):
        return f"야옹! 저는 {self.name}예요."

class Cow(Animal):
    def speak(self):
        return f"음메! 저는 {self.name}예요."

## -------------------------------------
# 다형성 핵심: 어떤 클래스인지 몰라도 같은 코드로 처리
## -------------------------------------
animals = [Dog("바둑이"), Cat("나비"), Cow("누렁이")]

for animal in animals:
    print(animal.speak())