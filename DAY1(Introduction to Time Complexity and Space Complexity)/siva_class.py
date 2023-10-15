class Siva:
    def __init__(self, mango2=None):
        print("default constructor")
        if mango2 is not None:
            print("2 parameter constr", mango2)

s = Siva(100)
