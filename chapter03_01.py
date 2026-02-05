# Chapter03-01
# Special Method(Magin Method)
# https://docs.python.org/3/reference/datamodel.html#special-method-names
# Python의 핵심 : 시퀀스(Sequnce), 반복(Iterator), 함수(Functions), 클래스(Class)
# 클래스 안에 정의할 수 있는 특별한(Built-in) 메서드

# 기본형
print(int)      # <class 'int'>
print(float)    # <class 'float'>
print('----------')

# 모든 속성 및 메서드 출력
print(dir(int))
print('----------')

n = 10
print(type(n))  # <class 'int'>
print('----------')

# + 사용시 -> 내부적으로 __add__사용
print(n + 100)
print(n.__add__(100))
# print(n.__doc__)

print(n.__bool__(), bool(n))
print(n * 100, n.__mul__(100))
print('----------')

# 클래스 예제 1)
class Fruit :
    def __init__(self, name, price) :
        self._name = name
        self._price = price

    def __str__(self):
        return 'Fruit Class Info : {} , {}'.format(self._name, self._price)
    
    def __add__(self, x) :
        print('Called >> __add__')
        return self._price + x._price

    def __sub__(self, x) :
        print('Called >> __sub__')
        return self._price - x._price
    
    def __le__(self, x) :
        print('Called >> __le__')
        if self._price <= x._price :
            return True
        else :
            return False
    
    def __ge__(self, x) :
        print('Called >> __ge__')
        if self._price >= x._price :
            return True
        else :
            return False

# 인스턴스 생성
s1 = Fruit('Orange', 7500)
s2 = Fruit('Banana', 3000)

# Magic Method 출력
print(s1 + s2)  # Fruit에서 구현한 __add__ Method가 호출됨
print('----------')

print(s1 >= s2)
print(s1 <= s2)
print('----------')

print(s1 - s2)
print(s2 - s1)
print('----------')

print(s1)
print(s2)