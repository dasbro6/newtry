# class roster:
#     "students and teacher class"
#     teacher = ""
#     students = []
#     def __init__(self,tn='mayun'):
#         self.teacher=tn
#     def add(self, sn):
#         self.students.append(sn)
#     def remove(self, sn):
#         self.students.remove(sn)
#     def print_all(self):
#         print("Teacher:",self.teacher)
#         print("Students:",self.students)
#
# ros = roster('other')
# print(ros)
# ros.add('liuyun')
# ros.print_all()


#BMI 例子

class BMI:
    def __init__(self,height,weight):
        self.bmi = weight/height**2
    def printBMI(self):
        print("Your BMI is {:.1f}".format(self.bmi))

class ChinaBMI(BMI):
    def printBMI(self):
        print("您的BMI是{:.1f}".format(self.bmi))
        list = [18.5, 24, 28]
        if self.bmi>=list[2]:
            print('fat')
        elif self.bmi>=list[1]:
            print('overweight')
        elif  self.bmi>=list[0]:
            print('normal')
        else:
            print('thin')

h = float(input('height= '))
w = float(input('weight= '))
x = ChinaBMI(h,w)
x.printBMI()