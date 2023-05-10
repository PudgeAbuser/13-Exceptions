# Объявление функции sum() с получением двух именованных аргументов.
# Аргументы number1 и number2 должны быть целочисленными.
def sum(*, number1: int, number2: int):
    return number1 + number2


# Объявление функции test1().
def test1():
    newArray = [1, 2, 3, 4]
    # Получение пятого элемента списка, которого не существует, и вызовет исключение IndexError.
    element = newArray[5]
    print(element)

    # Вызов функции sum() с передачей в нее второго и четвертого элемента списка как именованных аргументов.
    resultSum = sum(number1=newArray[1], number2=newArray[3])
    # Вывод результата выполнения функции на экран.
    print(resultSum)


# Проверяем, если текущий модуль является главным, то вызываем функцию test1().
if __name__ == '__main__':
    test1()

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
                print('оценка больше минимальной!')   
        except Exception