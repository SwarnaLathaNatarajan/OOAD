class Builder:
    def getBody(self): pass
    def getWheels(self): pass
    def getEngine(self): pass

class JeepBuilder(Builder):
    def getBody(self):
        body = Body("SUV")
        return body
    def getWheels(self):
        wheels = Wheels(12)
        return wheels
    def getEngine(self):
        engine = Engine(1000)
        return engine

class Body:
    def __init__(self,type):
        self.type = type

class Wheels:
    def __init__(self,n):
        self.n = n

class Engine:
    def __init__(self,power):
        self.power = power

class Car:
    def __init__(self):
        self.body = None
        self.wheels = []
        self.engine = None

    def setBody(self,body):
        self.body=body

    def attachWheel(self,wheels):
        self.wheels = wheels

    def setEngine(self,engine):
        self.engine=engine

    def rep(self):
        print(self.body.type,self.engine.power,self.wheels[0].n)

class Director:
    builder = None

    def setBuilder(self,builder):
        self.builder = builder

    def getCar(self):
        car = Car()
        body = self.builder.getBody()
        engine = self.builder.getEngine()
        wheels = self.builder.getWheels()
        car.setBody(body)
        car.setEngine(engine)
        car.attachWheel([self.builder.getWheels()]*4)
        return car

if __name__=='__main__':
    director = Director()
    jb = JeepBuilder()
    director.setBuilder(jb)
    car = director.getCar()
    car.rep()