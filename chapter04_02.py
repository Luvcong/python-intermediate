# Chapter04-02
# 시퀀스형
#   컨테이너(Container : 서로 다른 자료형 ([List, Tuple, Collections.deque])
#   플랫(Flat : 한 개의 자료형[str, bytes, bytearrats, array, memoryview])
#   가변형(list, byteArray, array.array, memoryview, deque)
#   불변형(tuple, str, bytes)

# 리스트 및 튜플 고급
# 3) Tuple Adbanced
# unpacking
#   - * 미사용
#   - 고정 개수 변수에 요소를 1:1로 할당

# extended unpacking
#   - * 사용
#   - 가변 개수 요소를 하나의 변수로 수집
#   - *rest는 남은 요소를 모두 수집하여 list로 반환

# b, a = a, b   => temp와 같은 변수를 사용하지 않아도 바로 교체 대체 가능
print(divmod(100, 9))   # (11, 1) - 목과 나머지 출력
print(divmod(*(100, 9)))
print(*(divmod(100, 9)))
print('----------')

x, y, *rest = range(10)
print(x, y, rest)   # 0 1 [2, 3, 4, 5, 6, 7, 8, 9]

x, y, *rest = range(2)  
print(x, y, rest)   # 0 1 []

x, y, *rest = 1, 2, 3, 4, 5
print(x, y, rest)   # 0 1 [3, 4, 5]
print('----------')

# 4) Mutable(가변) vs Immutable(불변)
l = (15, 20, 25)
m = [15, 20, 25]

print(l, id(l))
print(m, id(m))
print('----------')

# 재할당 (위와 ID 값이 상이)
l = l * 2
m = m * 2

print(l, id(l))
print(m, id(m))
print('----------')

# 불변형은 한번 ID가 할당되면 값 수정이 불가하기 때문에 새로운 객체가 생성
# 가변형은 값 수정이 가능하므로 본인 객체를 수정
l *= 2
m *= 2
print(l, id(l))
print(m, id(m)) # ID 값 동일
print('----------')

# 5) 정렬
# sort vs sorted
# reverse, key=Len, key-str.lower, key=func ...등

# 5-1) sorted : 정렬 후 새로운 객체 반환 (원본 유지 -> 새로운 객체 반환)
f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']
# 오름차순 정렬
print('sorted : ', sorted(f_list))  # ['apple', 'coconut', 'lemon', 'mango', 'orange', 'papaya', 'strawberry']

# 역순 정렬
print('sorted : ', sorted(f_list, reverse=True))  # ['strawberry', 'papaya', 'orange', 'mango', 'lemon', 'coconut', 'apple']

# key 길이 순서대로 정렬
print('sorted : ', sorted(f_list, key=len))  # ['apple', 'mango', 'lemon', 'orange', 'papaya', 'coconut', 'strawberry']

# 마지막 글자 기준으로 정렬
print('sorted : ', sorted(f_list, key=lambda x : x[-1]))  # ['papaya', 'orange', 'apple', 'lemon', 'mango', 'coconut', 'strawberry']

# 마지막 글자 기준으로 정렬 후 역순 정렬
print('sorted : ', sorted(f_list, key=lambda x : x[-1], reverse=True))  # ['strawberry', 'coconut', 'mango', 'lemon', 'orange', 'apple', 'papaya']

# 원본 (정렬 함수를 사용했음에도 마지막 출력 시, 원본 그대로 유지되어 출력됨)
print('sorted original : ', f_list)  # ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut'] -> 원본 유지
print('----------')


# 5-2) sort : 정렬 후 객체 직접 변경 (원본 직접 사용)
# 반환 값 None (원본 자체를 수정하기 때문에 반환 값이 없음)
print('sort : ', f_list.sort(), f_list)  # None ['apple', 'coconut', 'lemon', 'mango', 'orange', 'papaya', 'strawberry']
print('sort : ', f_list.sort(reverse=True), f_list)  # None ['strawberry', 'papaya', 'orange', 'mango', 'lemon', 'coconut', 'apple']
print('sort : ', f_list.sort(key=len), f_list)   # None ['mango', 'lemon', 'apple', 'papaya', 'orange', 'coconut', 'strawberry']
print('sort : ', f_list.sort(key=lambda x: x[-1]), f_list)   # None ['papaya', 'apple', 'orange', 'lemon', 'mango', 'coconut', 'strawberry']
print('sort : ', f_list.sort(key=lambda x: x[-1], reverse=True), f_list) # ['strawberry', 'coconut', 'mango', 'lemon', 'apple', 'orange', 'papaya']
print('sort original : ', f_list)

# List vs Array
# 리스트 기반 : 융통성, 다양한 자료형, 범용적 사용
# 숫자 기반 : 배열 (리스트와 거의 호환)