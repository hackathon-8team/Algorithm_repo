# k번째수
def solution(array, commands):
    answer = []

    for command in commands:
        # 각각의 명령 반복
        i, j, k = command

        # 명령에서 값을 추출
        # i는 시작 인덱스, j는 종료 인덱스, k는 추출할 숫자의 위치이다

        sliced_array = array[i - 1:j]
        # 명령 값에 따라 배열을 슬라이싱
        # 배열의 i-1부터 j까지의 부분 배열을 가져온다

        sorted_array = sorted(sliced_array)
        # 슬라이싱한 배열을 정렬하여 sorted_array에 저장

        answer.append(sorted_array[k - 1])
        # 정렬된 배열에서 k번째 수를 추출하여 answer 리스트에 추가

    return answer
