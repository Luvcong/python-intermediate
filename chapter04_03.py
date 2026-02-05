# Chapter04-03
# 시퀀스형
#   컨테이너(Container : 서로 다른 자료형 ([List, Tuple, Collections.deque])
#   플랫(Flat : 한 개의 자료형[str, bytes, bytearrats, array, memoryview])
#   가변형(list, byteArray, array.array, memoryview, deque)
#   불변형(tuple, str, bytes)

# 해시테이블(hashtable)
# Key에 Value를 저장하는 구조 (Key 값의 연산 결과에 따라 직접 접근이 가능한 구조)
# key 값을 해싱 함수로 계산해서 나온 숫자를 배열의 인덱스로 사용 -> 그 위치에 저장된 Value를 꺼내오는 구조
# └ Key → 해시 함수 → 주소 계산 → 그 주소로 바로 접근
# └ 해싱함수(Hash Function) : 임의의 Key를 정해진 범위의 숫자로 변환하는 함수

# Dict : Key 중복 허용 X
# Set  : 중복 허용 X 

# Hash 값 확인 (Hash 값이 있다는 건, 고유하다는 의미)
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print(hash(t1))
# print(hash(t2)) # 예외발생
"""
메모)
t1 해시 가능 (hashable) 
t2 해시 불가능 (unhashable)

- 둘 다 <class 'tuple'> type인데, t1만 해시 가능한 이유 ?
- 튜플 안에 들어있는 요소의 가변성 떄문

t1 : tuple -> int, int -> tuple -> int, int, int
t2 : tuple -> int, int -> list  -> int, int, int
** tuple 자체는 불변 객체이나 t2에는 가변 객체인 list가 포함되어 있으므로 해시 불가
** python에서는 값이 바뀔 수 있는 객체를 Key로 허용하면 아래와 같은 문제가 생기기 떄문에 막아두었음
    - 해시 값 변경
    - 저장된 위치를 다시 찾을 수 없음
    - 자료구조 깨짐
"""
print('----------')

# Dict Setdefault : Key가 없으면 기본 값을 넣고, 있으면 그 값을 그대로 반환하는 딕셔너리 메서드 (주로 조건문 없이 값 누적 시 사용)
# Dict Setdefault 예제
source = (
    ('k1', 'val11'),
    ('k1', 'val12'),
    ('k2', 'val13'),
    ('k2', 'val14'),
    ('k2', 'val15'))

new_dict1 = {}
new_dict2 = {}

# No Use Setdefault
for k, v in source:
    print(f'k : {k}, v : {v}')
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print(new_dict1)
print('----------')

# Use Setdefault
for k, v in source :
    new_dict2.setdefault(k, []).append(v)

print(new_dict2)
print('----------')

# 주의
new_dict3 = {k : v for k , v in source}
print(new_dict3)    # {'k1': 'val12', 'k2': 'val15'} => key가 중복되면 덮어씌워지므로 주의