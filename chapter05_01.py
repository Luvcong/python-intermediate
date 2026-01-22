# Chapter05-01
# 일급 함수(일급 객체, First Class)
# Python 함수 특징
# 1) 런타임 초기화 (실행 시점에 초기화)
# 2) 변수 할당 가능
# 3) 함수 인수 전달 가능
# 4) 함수 결과 반환 가능 (return)


# 함수 객체
def factorial(n) :
    '''Fectorial Function -> n : int'''
    if n == 1 : # n < 2
        return 1
    return n * factorial(n-1)

class A :
    pass

print(factorial(5))
print(type(factorial), type(A)) # <class 'function'> <class 'type'>

# 함수 객체만 갖고 있는 순수 속성들
# {'__qualname__', '__name__', '__closure__', '__kwdefaults__', '__annotations__', '__defaults__', '__call__', '__globals__', '__code__', '__get__'}
print(set(sorted(dir(factorial))) - set(sorted(dir(A))))
print(factorial.__name__)
print(factorial.__code__)
print('----------')

# 변수 할당 가능 여부 증명
var_func = factorial
print(var_func)
print(var_func(5))
print(list(map(var_func, range(1, 6))))
print('----------')

# 함수 인수 전달 및 반환 가능 여부 증명 => 고위 함수 (Higher-order function)
# map, filter, reduce

# map, filter
print(list(map(var_func, filter(lambda x : x % 2, range(1, 6)))))   # [1, 6, 120]
print([var_func(i) for i in range(1, 6) if i % 2])                  # [1, 6, 120]
print('----------')

# reduce : 값을 지워나가면서 해당 값을 누적 합산 처리
from functools import reduce
from operator import add

print(reduce(add, range(1, 11)))
print(sum(range(1, 11)))
print('----------')

# 익명함수(Lamda)
# 가급적 주석 작성하고, 익명함수보다는 일반 함수 형태로 작성 권장
# 일반 함수 형태로 함수명 설정 권장
print(reduce(lambda x, t : x + t, range(1, 11)))
print('----------')

# Callable : 호출 연산자 (메서드 형태로 호출 가능한지 확인)
# 호출 가능 확인
print(callable(str), callable(A))
print(callable(str), callable(list), callable(var_func), callable(var_func), callable(3.14))
print('----------')

# Inspect
from inspect import signature

sg = signature(var_func)

print(sg)
print(sg.parameters)
print('----------')

# partial : 인수 고정 -> 콜백 함수에 사용
from operator import mul
from functools import partial

print(mul(10, 10))

# 인수 고정
five = partial(mul, 5)  # 함수를 인자로 전달, 5 고정
print(five(10))
print('----------')

# 고정 추가
six = partial(five, 6)
print(five(10))
print(six())    # 이미 six()안에 2가지 인수가 들어가 있기 때문에 별도의 파라미터를 전달하지 않아도 됨
print([five(i) for i in range(1, 11)])
print(list(map(five, range(1, 11))))