"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW01.2
* 프로그램의 목적 및 기본 기능 :
* -넓이와 높이를 입력받고 넓이와 둘레를 계산사여 출력하는 프로그램
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.06
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.06	v1.0	최초 작성
"""

def main():
    width, length = map(int,(input("width, length = ").split()))
    print("Rectangle of width({}) and length({}) : area({}), perimeter({:.1f})".format(width, length, width*length, width*2+length*2))

if __name__ == "__main__":
    main()