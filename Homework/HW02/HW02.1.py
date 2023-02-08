"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW02.1
* 프로그램의 목적 및 기본 기능 :
* -0~255 범위의 숫자를 출력 포맷에 맞추어 출력하는 프로그램
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.06
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.06	v1.0	최초 작성
"""

def main():
    for i in range(0, 50):
        print("=", end="")
    print("\nDecimal      Bit Octal Hexadecimal")
    for i in range(0, 50):
        print("-", end="")
    print()
    for i in range(256):
        print("{:7} {:08b} {:#05o} {:#04X}".format(i, i, i, i))
if __name__ == "__main__":
    main()