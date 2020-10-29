class MakeMeal:
    def prep(self): pass
    def cook(self): pass
    def eat(self): pass

    def go(self):
        self.prep()
        self.cook()
        self.prep()

class MakeCoffee(MakeMeal):
    def prep(self):
        print("Prepping Coffee")

    def cook(self):
        print("Cooking Coffee")

    def eat(self):
        print("Drinking Coffee")


class MakeTea(MakeMeal):
    def prep(self):
        print("Prepping Tea")

    def cook(self):
        print("Cooking Tea")

    def eat(self):
        print("Drinking Tea")

if __name__=="__main__":
    c = MakeCoffee()
    t = MakeTea()
    c.go()
    t.go()