def fahr_to_celsius (temp_fahrenheit):
    """Данная функция переводит температуру по Фаренгейту в температуру по Цельсию.
        Input: Argument: temp_fahrenheit - температура по Фаренгейту (float или int)
        Return: Температура по Цельсию
        """
    return ((temp_fahrenheit - 32 ) / 1.8)

class weather():
    def __init__(self, temp_celsius, type_of_weather=None, value = None): 
        """Класс для описания погоды по температуре"""
        self.temp_celsius = temp_celsius
        self.type_of_weather = type_of_weather
        self.value = value

    def classifier(self):
        """Присваивание индекса и типа погоды, в зависимости от температуры"""
        if (self.temp_celsius) < -2: # Как и написано сверху - абсолютная копия из ex.3
            #Однако добавил две строчки снизу
            self.type_of_weather = "cold"
            self.value = 0
        elif (self.temp_celsius) >= -2 and self.temp_celsius<2:
            self.type_of_weather = "slippery"
            self.value = 1
        elif self.temp_celsius  >= 2 and self.temp_celsius<15:
            self.type_of_weather = "comfortable"
            self.value = 2
        elif self.temp_celsius >= 15:
            self.type_of_weather = "warm"
            self.value = 3
            
def temp_classifier(temp_celsius): # Просто присваиваю число к классу, выполняю метод и "вытаскиваю" только индекс из класса
    """Данная функция возвращает инндекс, который соответсвует одному из 4
    состояний погоды, по указанной пользователем температуре
        Input: Argument: temp_celsius - температура по Цельсию (float или int)
        Return: индекс погоды"""
    temp_celsius = weather(temp_celsius)
    temp_celsius.classifier()
    return temp_celsius.value