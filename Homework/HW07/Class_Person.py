"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW07.1, Class_Person
* 프로그램의 목적 및 기본 기능 :
* -Class_Person
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.08
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.08	v1.0	최초 작성
"""


class Person:
    def __init__(self, name, reg_id, age):
        self.setName(name)
        self.setRegID(reg_id)
        self.setAge(age)

    def getName(self):
        return self.name

    def getRegID(self):
        return self.reg_id

    def getAge(self):
        return self.age

    def setName(self, nm):
        self.name = nm

    def setRegID(self, rg_id):
        self.reg_id = rg_id

    def setAge(self, ag):
        if 0 <= ag < 250:
            self.age = ag
        else:
            print("*** Error in setting age (name:{}, age:{})".format(self.name, ag))
            self.age = 0  # default value

    def __str__(self):
        return "Person({}, {}, {})".format(self.getName(), self.getRegID(), self.getAge())
