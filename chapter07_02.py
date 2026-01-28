# Chapter07-02
# AsyncIO
# 비동기 I/O Coroutine 작업
# Generator -> 반복적인 객체를 사용해서 return 사용
# Non-bloking 비동기 처리

# Blocking I/O : 호출된 함수가 자신의 작업이 완료될 때까지 제어권을 갖고 있음 (타 함수 대기)
# Non Bloking I/O : 호출된 함수가(서브루틴) return 후 호출한 함수(메인루틴)에 제어권 전달 -> 타 함수는 일 지속

# 스레드 단점 : 디버깅 어려움, 자원 접근 시 레이스컨디션(경쟁상태), 데드락(Dead Lock) -> 고려 후 코딩 필요
# 코루틴 장점 : 하나의 루틴만 실행(단일스레드) -> Lock(락) 관리 필요 없음 -> 제어권으로 실행 -> 
#        단점 : 사용 함수가 비동기로 구현이 되어있어야 하거나 직접 비동기로 구현해야함

# Asyncio 웹 스크리핑 실습 (Beautiful Soup 추가)
import asyncio
import timeit
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import threading
from bs4 import BeautifulSoup

# 실행 시작 시간
start = timeit.default_timer()
print(f'start_time : {start}')
urls = ['https://naver.com', 'https://blog.naver.com']

async def fetch(url, excutor) :
    # Thread명 출력
    print(f'Thread Name : {threading.current_thread().name}, Start {url}')

    # 실행
    response = await loop.run_in_executor(excutor, urlopen, url)
    soup = BeautifulSoup(response.read(), 'html.parser')

    print(f'Thread Name : {threading.current_thread().name}, Done {url}')
    # print(soup.prettify())
    result_data = soup.title

    # 결과 반환
    return result_data
    
async def main() :
    # Thread 풀 생성
    executor = ThreadPoolExecutor(max_workers=10)

    # future 객체를 모아서 gather에서 실행
    futures = [asyncio.ensure_future(fetch(url, executor)) for url in urls]

    # 결과 취합
    result = await asyncio.gather(*futures)
    
    print('----------')
    print('result : ', result)

# 메인 함수 진입점
if __name__ == '__main__' :
    # 루프 초기화
    loop = asyncio.get_event_loop()
    # 작업 완료까지 대기
    loop.run_until_complete(main())
    # 수행 시간 계산
    duration = timeit.default_timer() - start
    # 총 실행 시간
    print('Total Running Time : ', duration)