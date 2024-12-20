from collections import Counter

class A:
    def __init__(self):
        print('Its me A')
    # ...existing code...

class A1:
    def __init__(self):
        print('Its me A1')
    # ...existing code...

class B(A, A1):
    def __init__(self):
        print('Its me instance of B')

    def getdetails(self, *arg):
        """This is the documentation string for getdetails."""
        print(type(arg))
        vals = lambda x: str(arg)
        print('Value :' + vals(arg))

    def ShowUniqueVal(self):
        lst = [1, 2, 1, 3, 3]
        st = set(lst)
        for i in st:
            dupcnt = 0
            for j in lst:
                if i == j:
                    dupcnt += 1
                if (dupcnt > 1 and i==j):
                    print('Dup. Value Count of  ', i, ' is: ', dupcnt)

if __name__ == "__main__":
    obj = B()
    obj.ShowUniqueVal()







