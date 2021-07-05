from OopsDemo import Caluclator


class ChildImpl(Caluclator):
    num2 = 200

    def __init__(self):
        Caluclator.__init__(self, 10, 20)

    def getCompleteData(self):
        return ChildImpl.num2 + self.num + self.summation()
        # o/p ---> 200 + 100 + (100+10+20)  = 430


obj = ChildImpl()
print(obj.getCompleteData())


# https://www.journaldev.com/13949/python-tutorial-beginners
#       Thank you........
