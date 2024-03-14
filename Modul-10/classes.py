class cars:
    def __init__(self, make, model):
        self.make = [make]
        self.model = [model]

while True:
    model = input("Skriv ett bil märke: ")
    make = input("Skriv modellen: ")
    car = cars(model, make)
    print(car.make, car.model)


