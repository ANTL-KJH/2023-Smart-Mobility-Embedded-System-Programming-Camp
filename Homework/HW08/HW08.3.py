"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW08.3
* 프로그램의 목적 및 기본 기능 :
* -genRandList with MyList and sys module
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.09
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.09	v1.0	최초 작성
"""
import myClassMtrx

def fgetMtrx(mtrx_name, f_in):
    n_row, n_col = map(int, f_in.readline().split())
    #print("getMtrx :: n_row = {}, n_col = {}".format(n_row, n_col))
    L_A = []
    for i in range(n_row):
        L_row = list(map(float, f_in.readline().split()))
        #print("L_row : ", L_row)
        for j in range(n_col):
            L_A.append(L_row[j])
    mtrx = myClassMtrx.Mtrx(mtrx_name, n_row, n_col, L_A)
    return mtrx

def main():
    file_input = open("matrix_data.dat", "r")
    mA = fgetMtrx("mA", file_input)
    print(mA)

    mB = fgetMtrx("mB", file_input)
    print(mB)


    file_input.close()

    mC = mA + mB
    mC.setName("mC = mA + mB")
    print(mC)

    mD = mA - mB
    mD.setName("mD = mA - mB")
    print(mD)

    mE = mA * mB
    mE.setName("mE = mA * mC")
    print(mE)


if __name__ == "__main__":
    main()
