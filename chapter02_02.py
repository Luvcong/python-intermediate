# Chapter02-02
# 객체 지향 프로그래밍 (OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
# 규모가 큰 프로젝트(프로그램)
#   : 함수 중심   -> 데이터 방대 -> 복잡
#   : 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car() :
    """
    Car class
    Author : Kim
    Date : 2026.01.21
    """

    # 클래스 변수 (모든 인스턴스가 공유)
    car_count = 0

    def __init__(self, company, details) :
        self._company = company
        self._details = details
        Car.car_count += 1

    def __str__(self) :     # 사용자 레벨에서 간단하게 문자열을 확인할 떄
        return 'str : {} - {}'.format(self._company, self._details)
    
    def __repr__(self) :    # 엔지니어 레벨에서 자세한 문자열을 확인할 떄
        return 'repr : {} - {}'.format(self._company, self._details)
    
    def __del__(self) :
        Car.car_count -= 1
    
    def detail_info(self) :
        print('Current Id : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

# Self 의미
car1 = Car('Ferrari', {'color' : 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw'    , {'color' : 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi'   , {'color' : 'Silver', 'horsepower': 300, 'price': 6000})

# ID 값 확인
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company)   # False

# dir & __dict__ 확인
print(dir(car1))
print(dir(car2))
print('----------')

print(car1.__dict__)
print(car2.__dict__)
print('----------')

"""
1) dir : 리스트 형태로 출력 (포괄적으로 상속받는 데이터 확인 가능)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_company', '_details

2) __dict__ : 딕셔너리 형태로 실제 값 출력
{'_company': 'Bmw', '_details': {'color': 'Black', 'horsepower': 270, 'price': 5000}}
"""

# Docstring 확인
print(Car.__doc__)
print('----------')

car1.detail_info()      # 인스턴스를 통해 메서드 호출 **
Car.detail_info(car2)   # 클래스에서 함수를 직접 호출하여 인스턴스 전달
print('----------')

# 비교
# class 자체는 1개이기 떄문에 동일한 객체
print(car1.__class__, car2.__class__)
print(id(car1.__class__) == id(car3.__class__)) # True
print('----------')

# 에러 발생 : Self 파라미터를 넘기지 않았기 떄문에
# Car.detail_info()

# {'_company': 'Ferrari', '_details': {'color': 'White', 'horsepower': 400, 'price': 8000}}
#
# 공유 확인
print(car1.__dict__)    # 클래스변수(car_count) 확인 안됨
print(car1.car_count)   # car_count 값 출력
print(dir(car1))        # car_count 확인 가능
# => 클래스 변수를 확인할 때는 dir 명령어를 사용

# 접근
print(Car.car_count)
print(car1.car_count)   # 3

del car2                # del 실행
print(Car.car_count)    # 2
print(car1.car_count)   # 2 (del 메서드 실행되어 car_count 차감)


# 인스턴스 네임스페이스에 없으면 상위에서 검색 -> 상위 검색 시에도 없으면 에러 발생
# 즉, 동일한 이름으로 변수 생성 가능 (인스턴스 검색 후 -> 상위 (클래스 변수, 부모 클래스 변수))