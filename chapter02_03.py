# Chapter02-03
# class method, instance method, static method

class Car() :
    """
    Car class
    Author : Kim
    Date : 2026.01.22
    Description : Class, Static, Instance Method
    """

    # 클래스 변수 (모든 인스턴스가 공유)
    # : 클래스 변수는 해당 클래스로부터 생성된 모든 인스턴스가 공유하는 값
    # : 인스턴스 변수는 각 객체만의 고유한 값 저장
    price_per_raise = 1.0

    def __init__(self, company, details) :
        self._company = company
        self._details = details

    def __str__(self) :     # 사용자 레벨에서 간단하게 문자열을 확인할 떄
        return 'str : {} - {}'.format(self._company, self._details)
    
    def __repr__(self) :    # 엔지니어 레벨에서 자세한 문자열을 확인할 떄
        return 'repr : {} - {}'.format(self._company, self._details)
    
    # Instance Method
    # Self : 객체의 고유한 속성 값을 사용 
    def detail_info(self) :
        print('Current Id : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

    # Instance Method
    def get_price(self) :
        return 'Before Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price'))
    
    # Instance Method
    def get_price_culc(self) :
        return 'After Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price')  * Car.price_per_raise)

    # Class Method
    # 클래스 메서드는 첫번째 파라미터로 cls(클래스)를 받음
    @classmethod
    def raise_price(cls, per) :
        if per <= 1 :
            return print('Please Enter 1 Or More')
        cls.price_per_raise = per
        print('Succeed! Price increased.')

    # Static Method
    @staticmethod
    def is_bmw(inst) :
        if inst._company == 'Bmw' :
            return 'OK! This car is {}.'.format(inst._company)
        return 'Sorry. This car is not Bmw.'

    
# Self 의미
car1 = Car('Ferrari', {'color' : 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw'    , {'color' : 'Black', 'horsepower': 270, 'price': 5000})

# 전체 정보
car1.detail_info()
print('----------')

# 가격 정보 (직접 접근)
print(car1._details.get('price'))
print(car1._details['price'])
print('----------')

# 가격 정보 (인상 전)
print(car1.get_price())
print(car2.get_price())
print('----------')

# 가격 인상 (클래스 메서드 미사용)
Car.price_per_raise = 1.4   # 직접 접근하는 방법은 좋지 않음 (값 변경 때문)

# 가격 정보 (인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())
print('----------')

Car.raise_price(1)
# 가격 인상 (클래스 메서드 사용)
Car.raise_price(1.6)

# 가격 정보 (인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())
print('----------')

# Bmw 여부 체크
# Static Method 사용 시, Class와 Instance 모두 접근 가능
# Class로 호출
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))

# Instance로 호출
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))