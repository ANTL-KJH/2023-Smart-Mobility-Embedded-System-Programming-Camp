"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW03.3
* 프로그램의 목적 및 기본 기능 :
* -사용자로부터 시, 분, 초를 입력받고 지난 자정, 다가오는 자정까지의 시간을 출력하는 프로그램
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.07
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.07	v1.0	최초 작성
"""


def main():
    while True:
        hour, min, sec = map(int, input("input hour min sec : ").split())
        if hour < 0 or min < 0 or sec < 0:
            break
        print("Input time : ({}:{}:{})".format(str(hour).zfill(2), str(min).zfill(2), str(sec).zfill(2)))
        elapsedSec = sec
        elapsedSec += min * 60
        elapsedSec += hour * 3600
        print("Elapsed seconds from last midnight = {}".format(elapsedSec))
        print("Remaining seconds to next-midnight = {}".format(86400 - elapsedSec))


if __name__ == "__main__":
    main()
