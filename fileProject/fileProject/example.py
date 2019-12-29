
class Student():
    s_number = ''       #学号
    name = ''           #姓名
    # __selectedCourse = [] #已选课程

    def __init__(self,s_number,name):
        self.s_number = s_number
        self.name = name
        self.__selectedCourse = []

    def course_detail(self):
        return self.__selectedCourse

    def add_course(self,cour_info):
        self.__selectedCourse.append(cour_info)

    def __str__(self):
        return 'name：{}，s_number：{}'.format(self.name,self.s_number)


class Teacher():
    t_number = ''       #教师编号
    name = ''           #教师名称
    phone_number = ''   #手机号码

    def __init__(self,t_number,name,phone_number):
        self.t_number = t_number
        self.name = name
        self.phone_number = phone_number

    def __str__(self):
        return 't_number: {},name: {}'.format(self.t_number,self.name)


class Course():
    c_number = ''       #课程编号
    name = ''           #课程名称
    teacher = None      #授课老师

    def __init__(self,c_number,name):
        self.c_number = c_number
        self.name = name

    def binding(self,teacher):
        if teacher:
            self.teacher = teacher
            d = {'课程名称':self.name,'教师名称':self.teacher.name}
            return d
        else:
            return None
