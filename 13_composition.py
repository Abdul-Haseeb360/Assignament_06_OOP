class Engine():
    def start(self):
        print("Engine Started!")


class Car():
    def __init__(self, engin):
        self.engin = engin

    def start_car(self):
        self.engin.start()


engin = Engine()
car = Car(engin)
car.start_car()
