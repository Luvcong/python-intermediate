# Chapter03-03
# 데이터 모델(Data Model)
# https://docs.python.org/3/reference/datamodel.html
# Python의 핵심 : 시퀀스(Sequnce), 반복(Iterator), 함수(Functions), 클래스(Class)

# 1) Namedtuple

# 객체 : python의 데이터를 추상화
# 모든 객체 -> id, type -> value

# 일반적인 튜플
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt

l_leng1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)
print(l_leng1)
print('----------')

# namedTuple 사용
from collections import namedtuple

# namedTule 선언 1)
Point = namedtuple('Point', 'x y')          # 공백으로 구분

pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

l_leng2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2)
print(l_leng2)

# namedTule 선언 2)
Point1 = namedtuple('Point', ['x', 'y'])    # 리스트로 구분
Point2 = namedtuple('Point', 'x, y')        # , 쉼표로 구분
Point3 = namedtuple('Point', 'x y')         # 공백으로 구분

# Point4 = namedtuple('Point', 'x y x class') # 중복 및 예약어는 변수로 구분 값으로 사용 불가
Point4 = namedtuple('Point', 'x y x class', rename=True)    # rename=True 옵션을 주는 경우 중복 및 예약어로 변수 사용 가능 (But, 난수로 변수 생성됨)

# 값 확인
print(Point1, Point2, Point3, Point4)

# Dict to Unpacking
temp_dict = {'x': 75, 'y': 55}


# 객체 생성
p1 = Point1(x = 10, y = 35)
p2 = Point2(20, 40)
p3 = Point3(45, y = 20)
p4 = Point4(10, 20, 30, 40)
p5 = Point3(**temp_dict)

print('----------')
print(p1)
print(p2)
print(p3)
print(p4)   # Point(x=10, y=20, _2=30, _3=40) => x, class 와 같이 중복 및 예약어 변수를 사용해서 임의로 변수 생성됨
print(p5)
print('----------')

# 사용
print(p1[0] + p2[1])    # index로 접근 (비권장)
print(p1.x + p2.y)      # key로 접근!
print('----------')

# Unpacking
x, y = p3
print(x, y)
print('----------')


# namedTyple Method
temp = [52, 38]
# _make() : 새로운 객체 생성
p4 = Point1._make(temp)
print(p4)   # 리스트 형태의 temp가 tuple 형태로 출력

# _fields : 필드 이름 확인
print(p1._fields, p2._fields, p3._fields)

# _asdict() : OrderedDict 반환
print(p1._asdict())
print(p4._asdict())
print('----------')

# 실 사용 실습
# 반에 20명 학생 / 4개의 반 (A, B, C, D)

Classes = namedtuple('Classes', ['rank', 'number'])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)]
ranks = 'A B C D'.split()
print('numbers : {}', numbers)
print('ranks : {}', ranks)
print('----------')

# List Comprehenstion
students = [Classes(rank, number) for rank in ranks for number in numbers]
print(len(students))
print('----------')
print(students)
print('----------')


# List Comprehenstion 보다 권장하는 방법
students2 = [Classes(rank, number)
             for rank in 'A B C D'.split()
                for number in [str(n) for n in range(1, 21)]]
print(len(students2))
print('----------')
print(students2)
print('----------')

# 출력
for s in students2 :
    print(s)