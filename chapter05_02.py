# Chapter05-02
# 클로저(Closure) 기초

# Python 변수 범위

# ex 1)
def func_v1(a) :
    print(a)
    print(b)
print('----------')
# 예외
# func_v1(10)

# ex 2)
b = 20  # global 변수

def func_v2(a):
    print(a)
    print(b)

func_v2(10)
print('----------')

# ex 3)
c = 30

def func_v3(a):
    global c    # global 선언하면 global 값 참조
    # c = 40
    print(a)
    print(c)    # 40 : global 변수를 참조하지 않음
    # c = 40    # 예외 발생 : global 변수에 동일한 변수명이 있더라도 local변수가 있으면 해당 값을 참조하려고 함
    c = 40

print('>> : ' , c)
func_v3(10)
print('>>> : ' , c)
print('----------')

# 클로저(Closure) 사용 이유
# 서버 프로그래밍 -> 동시성(Concurrency) 제어 -> 메모리 공간에 여러 자원이 접근 -> 교착상태(Dead Lock)
# 메모리를 공유하지 않고, 메시지 전달로 처리하기 위한 Erlang
# 클로저는 공유하되, 변경되지 않는(Immutable, Read Only) 구조를 적극적으로 사용 -> 함수형 프로그래밍과 연결됨
# 즉, 클로저는 불변자료구조 및 atom, STM -> 멀티스레드(Coroutine) 프로그래밍에 강점
a = 100
print(a + 100)
print(a + 1000)
print('----------')

# 결과 누적 (함수사용)
print(sum(range(1, 51)))
print('----------')

class Averager() :
    def __init__(self) :
        self._series = []

    def __call__(self, v) :
        self._series.append(v)
        print('inner >> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)
    
# 인스턴스 생성
averager_cls = Averager()

print(averager_cls(10))
print(averager_cls(30))
print(averager_cls(50)) # 누적되고 있는 것을 확인할 수 있음
