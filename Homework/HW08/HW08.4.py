"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW08.4
* 프로그램의 목적 및 기본 기능 :
* -
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.09
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.09	v1.0	최초 작성
"""
import pandas as pd


def main():
    Temp_DG = pd.read_csv("ta_20230209132713.csv")
    print("Temp_DG = \n", Temp_DG)
    # Avg_temp_DG = Temp_DG['Avg']
    # print("Avg_Temp_DG =\n“, Avg_temp_DG)
    print("Temp_DG.describe() =")
    print(Temp_DG.describe())
    temp_DG_highest = Temp_DG['High'].max()     # 최댓값
    print("temp_DG_highest = ", temp_DG_highest)
    temp_DG_lowest = Temp_DG['Low'].min()       # 최솟값
    print("temp_DG_lowest = ", temp_DG_lowest)
    Temp_DG_highest_day = Temp_DG[Temp_DG.High >= temp_DG_highest]
    print("Temp_DG_highest_day =\n", Temp_DG_highest_day)
    Temp_DG_lowest_day = Temp_DG[Temp_DG.Low <= temp_DG_lowest]
    print("Temp_DG_lowest_day =\n", Temp_DG_lowest_day)

if __name__ == "__main__":
    main()
