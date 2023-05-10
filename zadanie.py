class Student():
    def __init_(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        grade = 5
    def mediumGrade(self):
        try:
            minimalgrade = 3
            if self.grade > minimalgrade:
                print('Оценка больше минимальной!')   
        except Exception as ex:
            print("Оценка ниже проходного балла!", ex)

if __name__ == '__main__':
    student1 = Student()
    student1.mediumGrade()
