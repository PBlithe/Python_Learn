import example


def introduction(str):
    print('********************{}********************'.format(str))


#创建课程信息初始化，并以列表形式返回所创建的8门课程对象
def prepare_course():
    d = {"01":"网络爬虫","02":"数据分析","03":"人工智能","04":"机器学习",
         "05":"云计算","06":"大数据","07":"图像识别","08":"Web开发"}
    l = []
    for item in d:
        course = example.Course(item, d[item])
        l.append(course)
    return l

#创建教师信息初始化，并以列表形式返回所创建的8名教师对象
def create_teacher():

    teachers = { "01":["T1", "张亮", "13301122001"],
                 "02":["T2", "王朋", "13301122002"],
                 "03":["T3", "李旭", "13301122003"],
                 "04":["T4", "黄国发", "13301122004"],
                 "05":["T5", "周勤", "13301122005"],
                 "06":["T6", "谢富顺", "13301122006"],
                 "07":["T7", "贾教师", "13301122007"],
                 "08":["T8", "杨教师", "13301122008"]
                 }
    l = []
    for t in teachers.values():
        teacher = example.Teacher(*t) #序列传参
        l.append(teacher)
    return l

#实现课程与教师逐一绑定（每一课程信息绑定倒叙的每一老师信息），
# 并以列表形式返回所课程与教师的绑定结果
def course_to_teacher():
    l = []
    ls_course = prepare_course()
    ls_teacher = create_teacher()
    for i in range(0,8):
        d = ls_course[i].binding(ls_teacher[-1*i-1])
        l.append(d)
    return l

#创建学生信息初始化，并以列表形式返回所创建的8名学生对象
def create_student():
    ls_student = [ "小亮", "小明", "李红", "小丽", "Jone", "小彤", "小K", "慕慕"]
    l = []
    for i in range(1000,1008):
        student = example.Student(i,ls_student[1007-i])
        l.append(student)
    return l

if __name__ == '__main__':
    ctt = course_to_teacher()
    students = create_student()
    introduction('慕课学院(1)班学生信息')
    for student in students:
        print('name: {}, s_number: {}'.format(student.name, student.s_number))
    introduction('慕课学院(1)班选课结果')
    for c in range(len(ctt)):
        students[c].add_course(ctt[c])
    for s in students:
        print('name: {}, Selected: {}'.format(s.name,s.course_detail()))
