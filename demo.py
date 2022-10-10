class MyDemo():
    value = 0

@classmethod
def incre(cls, value):
    value.value += 1

@classmethod
def main(cls, args):
    var = cls.MyDemo()
    print("Value:", var.value)
    cls.incre(var)
    print("Incre Value:", var.value)