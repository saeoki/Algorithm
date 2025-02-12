def solution(N, stages):
    fail_list = []
    total_player = len(stages)
    for i in range(1, N+1) :
        count = stages.count(i)
        if total_player == 0 : # 항상 나눗셈을 할 때는 분모가 0이 되는 케이스를 유의할 것!
            fail_percent = 0
        else :
            fail_percent = count / total_player
        fail_list.append((i, fail_percent))
        total_player -= count
        
    fail_list.sort(key = lambda x: (-x[1], x[0]))
    return [stage[0] for stage in fail_list]


"""
실패율 분자 = stages 안의 i와 같은 수의 개수 = count
실패율 분모 = 남아있는 stages 개수
스테이지 업이되면 해당 스테이지를 삭제
하는 걸로 초기 구상을 잡았지만 스테이지를 삭제한 리스트를 계속 만들어내는 것은 시간복잡도 제한에 걸려서
플레이어 수로 계산 하는 것으로 변경 (스테이지 업이되면 count 수만큼 total player에서 뺌)

각 스테이지마다 실패율을 스테이지 번호와 함께 리스트로 리스트에 저장
첫번째 원소 : 스테이지 번호, 두번째 원소 : 실패율
실패율을 기준으로 정렬한 뒤 스테이지번호를 리스트로 만들어서 반환
"""
