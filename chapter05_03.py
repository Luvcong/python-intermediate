# Chapter05-03
# 클로저(Closure) 심화
# 외부에서 호출된 함수의 변수 값, 상태(reference) 복사 후 저장 -> 저장 후 접근(엑세스) 가능

# Closure 사용
def closure_ex1() :
    # Free variable
    # 클로저 영역
    series = []
    def averager(v) :
        series.append(v)
        print('inner >>> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)
    return averager

avg_closure1 = closure_ex1()
print(avg_closure1(10))
print(avg_closure1(20))
print(avg_closure1(30))

print('----------')


# function inspection
print(dir(avg_closure1))
print('----------')
print(dir(avg_closure1.__code__))
print('----------')
print(avg_closure1.__code__.co_freevars)    # 자유변수(Free Variable) 출력
print('----------')
print((avg_closure1.__closure__[0].cell_contents))  # 자유변수 값 출력
print('----------')

# 잘못된 클로저 사용
def closure_ex2() :
    # Free variable
    cnt = 0
    total = 0
    def average(v) :
        cnt += 1
        total += v
        return total / cnt
    return average

avg_closure2 = closure_ex2()
# print(avg_closure2(10)) # 예외 발생 (UnboundLocalError: local variable 'cnt' referenced before assignment)

def closure_ex3() :
    # Free variable
    cnt = 0
    total = 0
    def average(v) :
        nonlocal cnt, total
        cnt += 1
        total += v
        return total / cnt
    return average

avg_closure3 = closure_ex3()
print(avg_closure3(15))
print(avg_closure3(35))
print(avg_closure3(40))