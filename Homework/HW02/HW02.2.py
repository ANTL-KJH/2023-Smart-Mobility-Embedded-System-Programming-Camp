"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW02.2
* 프로그램의 목적 및 기본 기능 :
* -10개의 실수 데이터를 입력받고 최대값, 최소값, 평균값을 찾는 프로그램
* 프로그램 작성자 : 김재현(2191283)
* 최초 프로그램 작성일 : 2023.02.06
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.06	v1.0	최초 작성
"""

def main():
    L = list(input("input 10 float data in one line (separated in space) = ").split())
    print("float_strings = {}".format(L))
    L = list(map(float, L))
    print("L_float_data = ", L)

    print("L_max = ({}), L_min = ({}), L_avg = ({:.3f})".format(max(L), min(L), sum(L)/10))
if __name__ == "__main__":
    main()