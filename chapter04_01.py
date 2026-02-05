# Chapter04-01
# 시퀀스형 : 순서가 있고(index로 접근 가능), 반복(iteration)이 가능한 자료형
#   컨테이너(Container : 서로 다른 자료형 ([List, Tuple, Collections.deque])
#   플랫(Flat : 한 개의 자료형[str, bytes, bytearrats, array, memoryview])
#   가변형(list, byteArray, array.array, memoryview, deque)
#   불변형(tuple, str, bytes)

# 리스트 및 튜플 고급
# 1) 지능형 리스트(comprehending Lists)
chars = '+_)(*&^%$#@!)' # 불변형
code_list1 = []

for c in chars :
    # 유니코드 리스트
    code_list1.append(ord(c))

print(code_list1)
print('----------')

# Comprehending Lists (for~append보다 comprehending list의 속도가 약간 더 우세)
code_list2 = [ord(c) for c in chars]
print(code_list2)
print('----------')

# Comprehending Lists + Map, Filter
code_list3 = [ord(c) for c in chars if ord(c) > 40]
code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))
print(code_list3)
print(code_list4)
print('----------')
print([chr(c) for c in code_list1])
print([chr(c) for c in code_list2])
print([chr(c) for c in code_list3])
print([chr(c) for c in code_list4])

# 2) Generator 생성
import array    # array는 플랫 형태의 가변형

# Generator : 한 번에 한 개의 항목을 생성(메모리 유지X)
tuple_g = (ord(c) for c in chars)
print(type(tuple_g))
print(next(tuple_g))
print(next(tuple_g))
print(next(tuple_g))
# ... next()로 값을 꺼낼 수 있음
print('----------')

array_g = array.array('I', (ord(c) for c in chars))
print(type(array_g))
print(array_g.tolist()) # toList() : array -> list로 변환하여 출력
print('----------')


# 추가 예제
print(('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)))
for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)) :
    print(s)
print('----------')

# 리스트 주의 **
marks1 = [['~'] * 3 for n in range(4)]
marks2 = [['~'] * 3] * 4
print(marks1)
print(marks2)

# 수정
marks1[0][1] = 'X'  # [['~', 'X', '~'], ['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']]
marks2[0][1] = 'X'  # [['~', 'X', '~'], ['~', 'X', '~'], ['~', 'X', '~'], ['~', 'X', '~']]
print(marks1)
print(marks2)

# 증명
print([id(i) for i in marks1])  # 4개 모두 다른 ID 값
print([id(i) for i in marks2])  # 4개 모두 동일한 ID 값