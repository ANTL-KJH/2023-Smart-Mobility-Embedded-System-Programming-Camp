"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW05.4
* 프로그램의 목적 및 기본 기능 :
* -Fibonacci calculation with Dynamic Programming
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.08
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.08	v1.0	최초 작성
"""
memo = dict()   # memo for dynamic programming


def dynFibo(n):
    if n in memo:
        return memo[n]
    elif n <= 1:
        memo[n] = n
        return n
    else:
        fibo_n = dynFibo(n - 1) + dynFibo(n - 2)
        memo[n] = fibo_n
    return fibo_n


def main():
    start, stop, step = map(int,input("input start, stop, step of Fibonacci series : ").split())
    for n in range(start, stop + 1, step):
        print("dynFibo({:3d}) : {:25}".format(n, dynFibo(n)))


if __name__ == "__main__":
    main()
