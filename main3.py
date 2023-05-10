class ExceptionEmailSendData(Exception):  # Создание класса исключения
    def __init__(self, msg=None):  # Объявление конструктора класса
        if msg is None:  # Проверка наличия текста сообщения
            self.message = "Ошибка при отправке по почте"
        else:
            self.message = msg

    def __str__(self):  # Объявление метода преобразования объекта в строку
        return f"Exception: {self.message}"


class EmailData:  # Создание класса EmailData
    def __init__(self, emailAddress):  # Объявление конструктора класса
        self.email = emailAddress

    def sendEmail(self, data):  # Объявление метода отправки сообщения по email
        try:  # Начало блока try-except
            self.sendData(data)
            print(f"Успешно отправлено на {self.email}: {str(data)}")
        except ExceptionEmailSendData as e:
            print(e)

    def sendData(self, data):  # Объявление метода отправки данных
        if not self.sendToEmail(data):  
            raise ExceptionEmailSendData("Отправленные данные не корректны")  # Exception: смс с ошибкой
            # raise ExceptionEmailSendData() # Ошибка: Ошибка при отправке по почте

    def sendToEmail(self, data):  # Объявление метода отправки данных на email
        # Имитация ошибки при отправке
        if data == "смс с ошибкой":
            return False
        return True

if __name__ == '__main__':
    newEmail = EmailData("example@example.com")

    newEmail.sendEmail("Пришли новый документ плз")
    newEmail.sendEmail("Получил текст спс")
    newEmail.sendEmail("смс с ошибкой")
