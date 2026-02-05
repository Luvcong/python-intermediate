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


# frozenset() : set의 특성(순서없음, 중복제거)을 유지하면서 불변 + 해시 가능하게 만든 집합 타입

# set        : 가변 객체 -> 해시 불가능
# fronzenset : 불변 객체 -> 해시 가능
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

# frozenset() : set의 특성(순서없음, 중복제거)을 유지하면서 불변 + 해시 가능하게 만든 집합 타입

# set        : 가변 객체 -> 해시 불가능
# fronzenset : 불변 객체 -> 해시 가능

s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}
s2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'])
s3 = {3}
s4 = set()  # 원소가 하나도 없는 경우 {} 라고 선언하는게 아니라 set()으로 선언
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'})

s1.add('Melon') # 가능
print(s1)

# s5.add('Melon') # 에러 발생 (추가 불가)

# hash 값 확인
# print(hash(s1)) # 에러 발생 (set은 가변 객체로 해시 불가)

frozen_hash = frozenset(s1)
print(hash(frozen_hash))


# frozenset을 이용해서 set의 조합을 key로 사용할 수 있음
roles = {
    frozenset({'READ'}) : 'user',
    frozenset({'READ', 'WRITE'}) : 'editor',
    frozenset({'READ', 'WRITE', 'DELETE'}) : 'admin'
}

user_permissions = {'WRITE', 'READ'}

role = roles.get(frozenset(user_permissions))
print('role : ', role)  # role :  editor

# 선언 최적화
# byte 코드 -> python 인터프리터 실행
# └ python byte code를 사람이 읽을 수 있게 보여주는 디스어셈블러
from dis import dis

print(dis('{10}'))
print('----------')
print(dis('set([10])'))
print('----------')

# 지능형 집합 (Comprehending Set)
from unicodedata import name

# 0 ~ 255까지의 유니코드 문자 이름을 중복 없이 set으로 수집하여 출력
print({name(chr(i), '') for i in range(0, 256)})

print('----------')