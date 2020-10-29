class MainClass:

    only_instance = None

    @staticmethod
    def getInstance():
        if not MainClass.only_instance:
            MainClass()
        return MainClass.only_instance

    def __init__(self):
        if MainClass.only_instance:
            print("Instance already created ")
        else:
            MainClass.only_instance = self

if __name__ == '__main__':
    obj = MainClass()
    print(MainClass.getInstance())
    print(obj)
