class MercedesCar:
    def __init__(self, model, lights,):
        self.model = model
        self.lights = lights
        self.fuel = 50 #заправляем машину
        # Проверяем тип фар и автоматически ставим цвет подсветки
        if self.lights == "Neon":
            self.led_color = "Blue"
        elif self.lights == "Laser":
            self.led_color = "purple"
        elif self.lights == "Premium":
            self.led_color = "Gold"
        elif self.lights == "Fire":
            self.led_color = "orange"
        else:
            self.led_color = "White"
          # метод для поездки
    def drive (self,distance):
        #Если топливо >0 , то машина едет
      if self.fuel > 0:
          self.fuel = self.fuel - distance # трата бензина(Допустим 1 литр = 1 км)
          print (f"You drove {distance} km. Fuel left:{self.fuel}L.")  
          #Ниже проверим, что будет если топливо закончиться
          if self.fuel >=0:
             self.fuel = 0
             print("Oh! Out of fuel.The car has stopped.")
          else:
              print ("The cat cannot drive,the tank is empty!") # Это если машина работает от батореи 
          #---Тест драйв!---
          # надо создать новую машину Мерседес
          
my_car = MercedesCar("E-Class", "Neon")
#Параметры нашей машины
print(f"Car model:{ my_car.model}")
print (f"Ambient Light Color:{my_car.led_color}")
print("-----------------")

# Поехали!
my_car.drive(20)
my_car.drive(40)
#В итоге  мне показало,что она проехала 20 км и потратила 30л топлива
