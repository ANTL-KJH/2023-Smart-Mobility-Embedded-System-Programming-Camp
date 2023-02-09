"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW02.4
* 프로그램의 목적 및 기본 기능 :
* -사용자로부터 복소수를 입력받아 다양한 연산결과를 출력하는 프로그램
* 프로그램 작성자 : 김재현(2191283)
* 최초 프로그램 작성일 : 2023.02.06
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.06	v1.0	최초 작성
"""

def main():
    string = input("input c1 (in complex, re + imj): ")
    string = string[1:len(string)-2]        # remove (, j)
    real, imag = map(int, string.split(sep="+"))
    c1 = complex(real, imag)
    print("c1 = {}".format(c1))
    c2 = c1.conjugate()
    print("c2 = conjugate of c1 = {}".format(c2))
    print("c1 + c2 = {}".format(c1+c2))
    print("c1 - c2 = {}".format(c1-c2))
    print("c1 * c2 = {}".format(c1*c2))
    print("c1 / c2 = {}".format(c1/c2))

if __name__ == "__main__":
    main()