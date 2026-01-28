# Chapter06-02
# 병행성 (Concurrency) : 한 컴퓨터가 여러 작업을 동시에 수행 -> 단일 프로그램 안에서 여러 작업을 쉽게 해결 
# 병렬성 (Parallelism) : 여러 컴퓨터가 여러 작업을 동시에 수행 -> 속도

# Generator Ex 1)
def generator_ex1() :
    print('Start')
    yield 'A Point'    # 중단위치 (해당 위치를 저장하고 있음)
    print('Continue')
    yield 'B Point'
    print('End')

# temp = iter(generator_ex1())  # generator
temp = generator_ex1()  # generator (generator 객체가 이미 iterable 객체 이므로 iter로 감싸지 않아도 가능)

# print(temp) # generator 인 것을 확인할 수 있음
# print(next(temp))
# print(next(temp))
# print(next(temp))

# iterable이기 떄문에 for문 사용 가능
for v in generator_ex1() :
    pass
    # print(v)

# Generator Ex 2)
# 리스트 컴프리핸션이 만들어지는 순간 이미 전부 실행됨
temp2 = [x * 3 for x in generator_ex1()]    # list
temp3 = (x * 3 for x in generator_ex1())    # generator
print('---------- 1)')
# print(temp2) / print(temp3) 와 같은 코드가 없어도 아래 값은 모두 콘솔에 출력되어 표시됨
# Start
# Continue
# End
# Start
# Continue
# End
# ---------- 1)

""" 메모 )
[ ... for ... ] -> list comprehension
{ ... for ... } -> set / dict comprehension
( ... for ... ) -> generator expression

- 컴프리핸션 문법에는 tuple이 없음
    (comprehension : 반복문과 조건식을 한 줄 표현식으로 작성하여 새로운 collection으로 생성하는 문법)

- temp3의 타입이 tuple이 아닌, generator인 이유는 컴프리핸션 문법을 사용했기 때문!
    : tuple(x * 3 for x in generator_ex1())
        : 명시적으로 tuple 형변환을 해주어야 tuple 타입으로 생성됨
"""

print('temp2', temp2)   # generator를 실행하는 것이 아니라, 이미 만들어진 결과를 출력하므로 start, continue, end..는 출력되지 않음
# 출력 결과
# A PointA PointA Point
# B PointB PointB Point
""" 
result = []
for x in generator_ex1():   # generator에서 하나 꺼냄
    result.append(x * 3)    # 그 값으로 x * 3 계산

-> 하나의 yield 값이 완전히 소비된 다음에 다음 yield로 넘어감
"""

print('temp3', temp3)
print('---------- 2)')

for i in temp2 :
    print(i)

print('----------')

for i in temp3 :
    print(i)

# Generator Ex3 ) 중요 함수
# count, takewhile, filterfalse, accumulate, chain, product, groupby ...등

import itertools

gen1 = itertools.count(1, 2.5)  # .count(시작값, 증가값) : 무한으로 증가 가능
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
# ... 무한으로 출력 가능

# 조건
gen2 = itertools.takewhile(lambda x : x < 1000, itertools.count(1, 2.5))
for v in gen2 :
    pass
    # print(v)  # 조건에 맞는 수만큼 출력

# 조건 반대 값 출력
gen3 = itertools.filterfalse(lambda x : x < 3, [1, 2, 3, 4, 5])

for v in gen3 :
    print(v)    # 3, 4, 5

print('----------')

# 누적 합계
gen4 = itertools.accumulate([x for x in range(1, 101)])

for v in gen4 :
    print(v)

print('----------')

# 연결 1)
gen5 = itertools.chain('ABCDE', range(1, 11, 2))    # .chain(A, B) : A와 B 값 모두 하나의 리스트로 반환
print(list(gen5))   # ['A', 'B', 'C', 'D', 'E', 1, 3, 5, 7, 9]

# 연결 2)
gen6 = itertools.chain(enumerate('ABCDE'))  # enumerate : 인덱스 값을 붙여서 반환
print(list(gen6))   # [(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D'), (4, 'E')] - 튜플형 리스트로 반환

# 개별
gen7 = itertools.product('ABCDE')   # 개별로 분리해서 튜플형 리스트로 반환
print(list(gen7))   # [('A',), ('B',), ('C',), ('D',), ('E',)]

# 경우의 수
gen8 = itertools.product('ABCDE', repeat=4) # 설정한 repeat 숫자만큼 문자 출력
print(list(gen8))

# 그룹화
gen9 = itertools.groupby('AAAABBCCCCDDEEE')
print(list(gen9))

for chr, group in gen9 :
    print(chr, ' : ', list(group))
    # A  :  ['A', 'A', 'A', 'A']
    # B  :  ['B', 'B']
    # C  :  ['C', 'C', 'C', 'C']
    # D  :  ['D', 'D']
    # E  :  ['E', 'E', 'E']