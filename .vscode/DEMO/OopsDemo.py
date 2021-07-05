# class are user defined blueprint
# classes will have methods,class variables , instance variables and constructor etc.......
# self keyword is mandatory for calling variables names into method
# constructor name should be "__init__"

class Demo_oops:
    num = 100
    # default constructor

    def getData(self):
        print("excecuting method in class")


obj = Demo_oops()  # syntax to create object in python
obj.getData()
print(obj.num)

print('**************************************************************')

############################### Constructor ################################

# constructor is one method which is automatically callled when we create object for any class.


class Caluclator:
    num = 100

    def __init__(self, a, b):
        self.firstnumber = a
        self.secondnumber = b

    def getData(self):
        print("excecuting method in class")

    def summation(self):
        return self.firstnumber + self.secondnumber + Caluclator.num


obj = Caluclator(10, 20)  # syntax to create object in python
obj.getData()
print(obj.summation())

bj = Caluclator(14, 40)  # syntax to create object in python
obj.getData()
print(obj.summation())
