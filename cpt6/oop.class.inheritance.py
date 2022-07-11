class Engine(object):
    def start(self):
        pass

    def stop(self):
        pass


class ElectricEngine(Engine):
    pass


class V8Engine(Engine):
    pass


class Car(object):
    engine_cls = Engine

    def __init__(self) -> None:
        self.engine = self.engine_cls()

    def start(self):
        print(
            'Starting engine {0} for {1}... Wroom, wroom!'
            .format(
                self.engine.__class__.__name__,
                self.__class__.__name__)
        )
        self.engine.start()

    def stop(self):
        self.engine.stop()


class RaceCar(Car):  # Is-A Car
    engine_cls = V8Engine


class CityCar(Car):  # Is-A Car
    engine_cls = ElectricEngine


class F1Car(RaceCar):  # Is-A RaceCar and also Is-A Car
    pass  # engine_cls same as parent


car = Car()
racecar = RaceCar()
citycar = CityCar()
f1car = F1Car()
cars = [car, racecar, citycar, f1car]
for car in cars:
    car.start()
