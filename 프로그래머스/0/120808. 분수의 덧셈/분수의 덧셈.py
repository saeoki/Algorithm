def gcd (x, y) : # 최대공약수 구하는 유클리드 호제법 알고리즘
    while y :
        x, y = y, x%y
    return x

def solution(numer1, denom1, numer2, denom2):
    numer = (numer1 * denom2) + (numer2 * denom1)
    denom = denom1 * denom2
    g = gcd(numer, denom)
    return [numer//g, denom//g] # 정수값을 반환하도록 //연산