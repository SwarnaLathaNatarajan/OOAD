class ClassA:
    def __init__(self):
        self.members = {"A":1,"B":2,"C":3}

    def methodA(self,input):
        return self.members[input]

class ClassB:
    def __init__(self):
        self.members = {"A":2,"E":2,"F":3}

    def methodB(self,input):
        return self.members[input]

class ClassC:
    def __init__(self):
        self.members = {"A":3,"H":2,"I":3}

    def methodC(self,input):
        return self.members[input]

def Factory(class_name):
    classes = {
        "ClassA" : ClassA,
        "ClassB" : ClassB,
        "ClassC" : ClassC
    }
    return classes[class_name]()

if __name__ == '__main__':
    a = Factory("ClassA")
    b = Factory("ClassB")
    c = Factory("ClassC")
    print(a.methodA("A"))
    print(b.methodB("A"))
    print(c.methodC("A"))
