# 가장 큰 수
def solution(numbers):
    # 주어진 숫자를 문자열로 변환하여 새로운 리스트에 저장
    numbers = list(map(str, numbers))

    # 숫자를 비교하기 위해 정렬 기준을 사용자 정의 함수로 설정
    # 두 숫자를 합쳐보고 더 큰 수를 반환
    numbers.sort(key=lambda x: x * 3, reverse=True)

    # 리스트의 원소들을 이어붙여 가장 큰 수를 생성
    largest_number = ''.join(numbers)

    # 생성한 가장 큰 수를 반환
    return largest_number

