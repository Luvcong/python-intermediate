# Chapter04-04
# 시퀀스형
# 해시테이블(hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict : Key 중복 허용 X
# Set  : 중복 허용 X 

# Dict 및 Set 심화

# 1) Immutable Dict
from types import MappingProxyType

d = {'key1' : 'value1'}

# Read Only 설정
d_frozen = MappingProxyType(d)

print(d, id(d))
print(d_frozen, id(d_frozen))
print('----------')

# 수정 불가
# d_frozen['key2'] = 'value2'

# 수정 가능
d['key2'] = 'value2'



s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}
s2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'])
s3 = {3}
s4 = set()  # 원소가 하나도 없는 경우 {} 라고 선언하는게 아니라 set()으로 선언
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'})

s1.add('Melon')
print(s1)

# s5.add('Melon') # 에러 발생 (추가 불가)
# print(s5)

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5))
print('----------')

# 선언 최적화
# byte 코드 -> python 인터프리터 실행
from dis import dis

print(dis('{10}'))
print('----------')
print(dis('set([10])'))
print('----------')

# 지능형 집합 (Comprehending Set)
from unicodedata import name

print({name(chr(i), '') for i in range(0, 256)})

print('----------')