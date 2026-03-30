##ex16_oop.py 객체지향 클래스

class Dog:
    def __init__(self,name): #첫번째 파라미터 self
        self.name = name

    def bark(self): E 
        print(f'{self.name}이 짖습니다. 멍멍!')

    

    poppy = Dog('뽀삐')
    poppy.bark()

    choco = Dog('초코')
    choco.bark()