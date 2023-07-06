# H-Index
def solution(citations):
    # 논문 인용 횟수를 내림차순으로 정렬
    citations.sort(reverse=True)

    # 논문 인용 횟수를 순회하면서 H-Index를 계산
    for i in range(len(citations)):
        # 현재 논문 인용 횟수보다 인용된 논문의 개수가 크거나 같을 때,
        # H-Index를 반환
        if citations[i] <= i:
            return i

    # 모든 논문을 다 순회한 후에도 H-Index를 찾지 못한 경우,
    # 논문의 개수(len(citations))를 H-Index로 반환
    return len(citations)
