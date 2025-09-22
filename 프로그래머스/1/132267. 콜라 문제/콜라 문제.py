"""
n개의 콜라를 가지고있을 때, 마트에 a개의 빈병을 가져다 주면, b개의 콜라를 준다.

계산식을 만들어 놓고 반복적으로(재귀적) 계산
마트에서 새로 받을 수 있는 콜라 갯수 next_n = (n//a)*b
  if) (찌꺼기가 생길 경우) n%a : 
sum에는 계산식의 결과인 next_n을 계속 더해준다.
그리고 찌꺼기가 있다면 n에 더해 다음 연산에서 써먹어준다.

n//a가 0이되면 종료 -> n으로 a를 나눌 수 있을때까진 계속 반복
"""        
def solution(a, b, n):
    sum = 0
    while (n >= a) :
        next_n = (n//a)*b
        keeping_cola = n%a
        
        sum += next_n
        n = next_n + keeping_cola
    return sum