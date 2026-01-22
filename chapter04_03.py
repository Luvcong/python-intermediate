# Chapter04-03
# 시퀀스형
#   컨테이너(Container : 서로 다른 자료형 ([List, Tuple, Collections.deque])
#   플랫(Flat : 한 개의 자료형[str, bytes, bytearrats, array, memoryview])
#   가변형(list, byteArray, array.array, memoryview, deque)
#   불변형(tuple, str, bytes)

# 해시테이블(hashtable)
# Key에 Value를 저장하는 구조 (Key 값의 연산 결과에 따라 직접 접근이 가능한 구조)
# key 값을 해싱 함수 -> 해시 주소 -> key에 대한 value 참조

# Dict : Key 중복 허용 X
# Set  : 중복 허용 X 

# Hash 값 확인 (Hash 값이 있다는 건, 고유하다는 의미)
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print(hash(t1))
# print(hash(t2)) # 예외발생
print('----------')

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