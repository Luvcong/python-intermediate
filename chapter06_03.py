# Chapter06-03
# 병행성 (Concurrency) : 한 컴퓨터가 여러 작업을 동시에 수행 -> 단일 프로그램 안에서 여러 작업을 쉽게 해결 
# 병렬성 (Parallelism) : 여러 컴퓨터가 여러 작업을 동시에 수행 -> 속도
# 코루틴(Coroutine)

# 코루틴 : 런타임/컴파일러, 단일(싱글) 스레드, stack을 기반으로 동작하는 비동기 작업
# 스레드 : OS에서 관리, CPU 코어에서 실시간, 시분할 비동기 작업 -> 멀티스레드

# yield, send : 메인 <-> 서브
# 코루틴 제어, 상태, 양방향 전송

# 서브루틴 : 메인루틴 호출 -> 서브루틴 수행(흐름제어)
# 코루틴 : 루틴 실행 중 중지 -> 동시성 프로그래밍 (스레드에 비해 오버헤드 감소)
# 스레드 : 싱글스레드 -> 멀티스레드 -> 복잡 -> 공유되는 자원 -> 교착 상태 발생 가능성, 컨텍스트 스위칭 비용 발생, 자원 소비 가능성 증가
# python3.5 이상부터 : def -> async / yield -> await로 사용 가능 

# 코루틴 ex 1)
def coroutine1() :
    print('>>> coroutine started.')
    i = yield
    print('>>> coroutine received : {}'.format(i))

# 메인 루틴
# 제너레이터 선언
cr1 = coroutine1()
print(cr1, type(cr1))

# yield 지점까지 서브루틴 수행
# next(cr1)
# next(cr1)
# 기본 전달 값은 None

# send() : 값 전송 (다음 yield 지점으로 값을 밀어 넣는 명령어)
# cr1.send(100)   # next() 없이 바로 send()는 불가
print('----------')


# 코루틴 ex 2)

# 코루틴 상태 값 키워드
# 1) GEN_CREATED : 처음 대기 상태
# 2) GEN_RUNNING : 실행 상태
# 3) GEN_SUSPENDED : Yield 대기 상태
# 4) GEN_CLOSED : 실행 완료 상태

def coroutine2(x) :
    print('>>> coroutine startd : {}'.format(x))
    y = yield x     # => yield는 값을 받는 지점이 아니라 '값을 내보내고 멈추는 지점'
    print('>>> coroutine received : {}'.format(y))
    z = yield x + y
    print('>>> coroutine received : {}'.format(z))

cr3 = coroutine2(10)    # generator 객체 생성 (GEN_CREATED) / x = 10

from inspect import getgeneratorstate

print(getgeneratorstate(cr3))   # GEN_CREATED

# 아직 y에는 값이 없는 상태 (x만 반환)
print(next(cr3))    # 10 (x 값)

print(getgeneratorstate(cr3))

cr3.send(15)    # 20 (y 값)
# cr3.send(30)  # 30 (z 값) , 종료
print('--------------------')

# 코루틴 ex 3)
# 3.5 이상부터 StopIteration 자동 처리 (awiat)
# 중첩 코루틴 처리

def generator1() :
    for x in 'AB' :
        print('x : {}'.format(x))
        yield x
    for y in range(1, 4) : 
        print(f'y : {y}')
        yield y

t1 = generator1()
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
# print(next(t1))   # 예외 발생
print('----------')

t2 = generator1()
print(list(t2))
print('----------')

# yield from : Iterable한 데이터를 순차적으로 끝까지 출력
def generator2() :
    yield from 'AB'
    yield from range(1, 4)

t3 = generator2()
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
# print(next(t3))   # 예외 발생