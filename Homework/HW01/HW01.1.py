"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW01.1
* 프로그램의 목적 및 기본 기능 :
* -반지름을 입력받고 원의 넓이와 둘레를 계산하여 출력하는 프로그램
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.06
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.06	v1.0	최초 작성
"""

def main():
    PI = 3.141592
    radius = int(input("radius = "))
    print("Circle of radius ({}) : area({:.4f}), circumference({:.6f})".format(radius, radius * radius*PI, 2*PI*radius))

if __name__ == "__main__":
    main()