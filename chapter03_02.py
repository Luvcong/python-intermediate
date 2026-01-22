# Chapter03-02
# Special Method(Magin Method)
# https://docs.python.org/3/reference/datamodel.html#special-method-names
# Python의 핵심 : 시퀀스(Sequnce), 반복(Iterator), 함수(Functions), 클래스(Class)
# 클래스 안에 정의할 수 있는 특별한(Built-in) 메서드

# 클래스 예제 2)
# 벡터(x, y) (5, 2)
# (5, 2) + (4, 3) = (9, 5)
# (10, 3) * 5 = (50, 15)
# Max((5, 10)) = 10

class Vector() :
    def __init__(self, *args) :
        ''' Create a Vector, example : v = Vector(5, 10) '''
        if len(args) == 0 :
            self._x, self._y = 0, 0
        else :
            self._x, self._y = args
    
    def __repr__(self):
        ''' Return the Vector infomations. '''
        return 'Vector(%r, %r)' % (self._x, self._y)
    
    def __add__(self, other) :
        '''Return the Vector addtion of self and other'''
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, y) :
        return Vector(self._x * y, self._y * y)
    
    def __bool__(self) :
        return bool(max(self._x, self._y))


print(Vector.__init__.__doc__)  # class가 아닌 method에 doc를 작성했기 때문에 메서드 접근해서 __doc__를 사용해야 함

# Vector 인스턴스 생성
v1 = Vector(5, 7)
v2 = Vector(23, 35)
v3 = Vector()
print(v1, v2, v3)
print('----------')

# Magic Method 출력
print(v1 + v2)  # Vector(28, 42)
print(v1 * 3)   # Vector(15, 21)
print(v2 * 10)  # Vector(230, 350)
print(bool(v1), bool(v2), bool(v3)) # True True False