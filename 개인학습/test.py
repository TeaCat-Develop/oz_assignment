"""

Python Escape 08번 문제

signal 변수에 42, 15, 8, 23, 16을 할당하고 최종 출력값을 구하세요.
* 출력값 그대로 입력해주세요!
* 기존 코드를 변경할 필요는 없습니다!

"""

signal='42,15,8,23,16'

decoded = [int(x) * 2 for x in signal.split(",") if int(x) % 2 == 0]
print(sum(decoded))