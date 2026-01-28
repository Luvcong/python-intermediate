# Chapter06-01
# 병행성 (Concurrency)
# Iterator, Generator

# Python 반복 가능 타입
# for, collections, text, file, list, dict, set, tuple, unpacking, *args : iterable

t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('__iter__' in dir(t)) # print(hasattr(t, '__iter__'))
for c in t :
    print(c)

print('----------')

w = iter(t)

while True :
    try :
        print(next(w))
    except Exception :
        break

print('----------')

# 반복형 확인 11)
print(hasattr(t, '__iter__'))   

# 반복형 확인 2)
from collections import abc
print(isinstance(t, abc.Iterable))
print('----------')

# next 사용
class WordSplitter :
    def __init__(self, text) :
        self._idx = 0
        self._text = text.split(' ')

    def __next__(self) :
        try :
            word = self._text[self._idx]
        except Exception :
            raise StopIteration('Stopped Iteration')    # raise : 의도적으로 예외 발생 처리
        self._idx += 1
        return word
    
    """ 메모 )
    next() 호출 시
    - 다음 값이 있으면 반환
    - 더 이상 없으면 StopIteration 발생

    Exception 대신 raise를 사용하는 이유 ?
    - Exception은 오류 발생을 의미
    - rasie StopIteration은 정상적인 반복 종료를 의미
    """

    def __repr__(self) :
        return 'wordSplit(%s)' % (self._text)

# next 패턴
wi = WordSplitter('Do today what you could do tomorrow')
print(wi)

""" 메모)
print(wi)를 실행했을 때, __repr__이 실행되는 이유 ?
- print()가 객체를 문자열로 바꾸는 우선순위 규칙 떄문
- __repr__ -> __str__ 순서로 문자열 표현을 찾음
- 현재 구현한 wordSpliter에서는 __str__이 없기 때문에 __repr__이 사용
"""

print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
# print(next(wi))

""" 메모)
next() <-> __next__와 1:1 매핑
- 클래스 구현 없이 내부 C레벨에서 구현된 __next__를 사용하는 경우 ?
- 예시 :

test = 'hi my name is 공주'
print(next(test))   # 예외 발생 (str은 iterrable / iterator가 아니기 때문)
    - iterable : __iter__가 존재 => 즉, iterator로 만들 수 있는 객체라는 뜻 (iter()를 적용할 수 있음)
    - iterator : __iter__ 와 __next__가 존재 => next()를 통해 값을 하나씩 순차적으로 반환하는 객체
                호출될 떄마다 다음 값을 반환하다가 반복이 끝나면 StopIteration을 발생시키는 객체

iterTest = iter(test)   # 기존의 str 객체를 iterator한 객체로 생성
print(hasattr(iterTest, '__next__'))    # True
print(next(iterTest))   # 출력 (예외 발생 x)

# while, for, next() 등을 사용해서 값 출력 가능
for t in iterTest :
    print(t)    # 반복 순환 가능하여 값 출력
"""

print('----------')

# Generator 패턴
# 1) 지능형 리스트, 딕셔너리, 집합 -> 데이터 양 증가 후 메모리 사용량 증가 -> 제너레이터 사용 권장
# 2) 단위 실행 가능한 코루틴(corotine)구현과 연동
# 3) 작은 메모리 조각 사용

""" 메모 )
generator는 함수 실행 상태 자체를 저장 
-> 코드의 실행 위치(yield 위치) + 지역 변수 + 스택 상태를 한 덩어리로 저장하여 기억하고 있음

iterator : 다음에 반환할 요소의 위치가 저장 -> 해당 위치의 값을 반환
gnerator : 현재까지 실행한 위치가 저장      -> 그 이후부터 실행

"""
class WordSplitGenerator :
    def __init__(self, text) :
        self._text = text.split(' ')
    
    def __iter__(self) :
        for word in self._text :
            yield word  # 제너레이터
        return  # return이 없어도 가능
    
    def __repr__(self) :
        return 'worldSplitGenerator(%s)' % (self._text)


wg = WordSplitGenerator('Do today what you could do tomorrow')
wt = iter(wg)

print(wt, wg)
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
# print(next(wt))   # 예외 발생

print('----------')