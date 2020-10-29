class Subject():
    def __init__(self):
        self.observers = []

    def addObserver(self,observer):
        self.observers.append(observer)

    def removeObserver(self,observer):
        self.observers.remove(observer)

    def something(self):
        for obs in self.observers:
            obs.update()

class Observer:
    def __init__(self,id):
        self.id = id

    def update(self):
        print(self.id,"Event occurred")

if __name__=='__main__':
    subj = Subject()
    obs1,obs2 = Observer(1),Observer(2)
    subj.addObserver(obs1)
    subj.addObserver(obs2)
    subj.something()