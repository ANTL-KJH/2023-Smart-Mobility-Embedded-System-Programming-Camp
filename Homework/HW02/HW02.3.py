"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW02.3
* 프로그램의 목적 및 기본 기능 :
* -3개의 16진수를 입력받고 연산 결과를 출력하는 프로그램
* 프로그램 작성자 : 김재현(2191283)
* 최초 프로그램 작성일 : 2023.02.06
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.06	v1.0	최초 작성
"""

def main():
    x = int(input("hexadecimal x = "), 16)
    y = int(input("hexadecimal y = "), 16)
    z = int(input("hexadecimal z = "), 16)
    print(" x = {:4d} in decimal, {:#15b} in bits".format(x, x))
    print(" y = {:4d} in decimal, {:#15b} in bits".format(y, y))
    print(" z = {:4d} in decimal, {:#15b} in bits".format(z, z))

    print(" x & y  = in hex({:#7x}), in bin({:#15b})".format(x & y, x & y))
    print(" x | y  = in hex({:#7x}), in bin({:#15b})".format(x | y, x | y))
    print(" x ^ y  = in hex({:#7x}), in bin({:#15b})".format(x ^ y, x ^ y))
    print(" ~x     = in hex({:#7x}), in bin({:#15b})".format(~x, ~x))
    print(" x << 2 = in hex({:#7x}), in bin({:#15b})".format(x << 2, x << 2))
    print(" y >> 2 = in hex({:#7x}), in bin({:#15b})".format(y >> 2, y >> 2))
    print(" z >> 2 = in hex({:#7x}), in bin({:#15b})".format(z >> 2, z >> 2))

if __name__ == "__main__":
    main()