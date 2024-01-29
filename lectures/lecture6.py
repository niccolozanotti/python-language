'''
Homework among the slides of Lecture6
'''

class Student:
    def __init__(self, registration_number, name, year):
        self.reg_no = registration_number
        self.name = name
        self.year = year # 1,2,3,4,5
    def show(self):
        print(self.reg_no,self.name,self.year)
    def pass_class(self):
        self.year += 1

People = [Student(i**2,'c'+str(i),i) for i in range(1,6)]

    
    