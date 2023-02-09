"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW04.1
* 프로그램의 목적 및 기본 기능 :
* -Big Endian과 Little Endian 방식에 따른 저장결과를 확인하는 프로그램
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.07
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.07	v1.0	최초 작성
"""


def main():
    d = 0xABCDEF01
    d_bytes_BE = int.to_bytes(d, length=4, byteorder='big')  # big endian
    d_bytes_LE = int.to_bytes(d, length=4, byteorder='little')  # little endian
    print("d = 0x{:X}".format(d))
    print("d_bytes_BE = ", d_bytes_BE)
    print("d_bytes_LE = ", d_bytes_LE)


if __name__ == "__main__":
    main()