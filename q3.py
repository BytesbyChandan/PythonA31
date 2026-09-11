class engine:
    def start(self):
        print("Engine started")
    def stop(self):
        print("Engine stopped")
class electric_system:
    def start(self):
        print("Electric system started")
    def stop(self):
        print("Electric system stopped")

class hybrid_car(engine, electric_system):
    def start(self):
        engine.start(self)
        electric_system.start(self)
    def stop(self):
        engine.stop(self)
        electric_system.stop(self)

hybrid = hybrid_car()
hybrid.start()
hybrid.stop()