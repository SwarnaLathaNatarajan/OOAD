class mainClass:

    only_instance = None

    @staticmethod
    def getInstance():
        if not mainClass.only_instance:
            mainClass()
        return mainClass.only_instance

    def __init__(self):
        if mainClass.only_instance:
            print("Instance already created ")
        else:
            mainClass.only_instance = self

if __name__ == '__main__':
    obj = mainClass()
    print(mainClass.getInstance())
    print(obj)
