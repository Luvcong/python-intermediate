# Chapter06-05
# Futures (동시성)
# 비동기 작업 실행
# 지연시간(Block) CPU 및 리소스 낭비 방지 -> File, Newtork I/O 관련 등 작업 시, 동시성 활용 권장
# 비동기 작업과 적합한 프로그램일 경우 압도적으로 성능 향상

# Futures : 비동기 실행을 위한 API를 고수준으로 작성 -> 사용하기 쉽도록 개선하여 나온 기능
# concurrent.futures
# 1) 멀티스레딩/멀티프로세싱 API가 통일되어 매우 쉽게 사용 가능
# 2) 실행중인 작업 취소, 완료 여부 체크, 타임아웃 옵션, 콜백 추가, 동기화 코드 매우 쉽게 작성 가능 -> Promise 개념

# 2가지 패턴 실습
# 1) concurrent.futures map
# 2) concurrent.futures wait, as_completed

# GIL (Global Interpreter Lock)
# : 두 개 이상의 스레드가 동시에 실행될 때 하나의 자원을 엑세스 하는 경우
#   -> 문제점을 방지하기 위해 GIL이 실행됨 (리소스 전체에 락이 걸림) -> Context Switch (문맥 교환) 비용 발생

# GIL 우회 : 멀티프로세싱 사용 / CPython 사용 등..

import os
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait, as_completed

WORK_LIST = [100000, 1000000, 10000000, 10000000]

# 동시성 합계 계산 메인 함수
# 누적 합계 함수 (generator)
def sum_generator(n) :
    return sum(n for n in range(1, n +1))

def main() :
    # Worker Count
    worker = min(10, len(WORK_LIST))

    start_tm = time.time()
    
    # futures
    futures_list = []

    # 결과 건 수
    # ThreadPoolExecutor
    # with futures.ThreadPoolExecutor() as excutor :
    #     # map : 작업 순서를 유지하고, 직접 실행
    #     result = excutor.map(sum_generator, WORK_LIST)

    # ProcessPoolExecutor
    with ProcessPoolExecutor() as excutor :
        for work in WORK_LIST :
            # futures 반환 (실행되는 것이 아니라 반환만)
            # submit : 작업을 즉시 실행하지 않고, 실행 큐에 등록하는 함수
            future = excutor.submit(sum_generator, work)
            # 스케줄링
            futures_list.append(future)
            # 스케줄링 확인
            print(f'Scheduled for {work} : {future}')
            print('----------')
        
        # 1) wait 결과 출력
        # result = wait(futures_list, timeout = 7)
        # # 성공
        # print(f'Completed Task : {str(result.done)}')
        # # 실패
        # print(f'Pending ones after waitingfor 7 seconds : {str(result.not_done)}')
        # # 결과 값 출력
        # print([future.result() for future in result.done])

        # 2) as_completed 결과 출력
        for future in as_completed(futures_list) :
            result = future.result()    # 결과가 나올 때까지 대기
            done = future.done()
            cancelled = future.cancelled

            # 결과 룰력
            print(f'Future Result : {result}, Done : {done}')
            print(f'Future cancelled : {cancelled}')

    end_tm = time.time() - start_tm

    msg = '\n Time : {:.2f}s'
    print(msg.format(end_tm))

# 실행 (해당 코드가 있어야 실행됨)
if __name__ == '__main__' :
    main()