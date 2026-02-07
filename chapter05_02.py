# Chapter05-02
# 클로저(Closure) 기초
# 클로저 : 자신이 정의된 스코프 변수를 기억해서 그 스코프가 끝난 이후에도 사용할 수 있는 함수 (= 외부 변수를 기억하는 함수)

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
"""
Erlang : 메모리 공유 자체를 제거
- 프로세스 간 메모리를 공유하지 않음
- 오직 메시지 전달만 사용
- 각 프로세스는 완전히 독립된 힙 사용
"""

# 클로저는 공유하되, 변경되지 않는(Immutable, Read Only) 구조를 적극적으로 사용 -> 함수형 프로그래밍과 연결됨
# 즉, 클로저의 기본 컬렉션은 모두 불변자료구조 (map, vector, set, list .. 등 모두 수정 불가)
""" 메모)
- Race Condition : 실행 순서에 따라 결과가 달라짐
- Dead Lock : 서로 락을 기다리며 영원히 멈춤
- Lock 비용 증가 : 성능 저하 및 코드 복잡도 증가
"""
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
    
# 인스턴스 생성 (Averager에서 _series 빈 리스트 객체 생성됨)
averager_cls = Averager()

print(averager_cls(10))
print(averager_cls(30))
print(averager_cls(50)) # 누적되고 있는 것을 확인할 수 있음 (함수가 아니라 averager_cls 객체가 상태를 기억하고 있기 때문)

def avg(v):
    series = []
    series.append(v)
    return sum(series) / len(series)

# 위 코드처럼 되어있다면 함수를 호출할 때마다 리스트 객체가 생성되어 누적되지 않음
