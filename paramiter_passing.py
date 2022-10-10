# class ParameterPass:
#     def __init__(self):
#         A = [1, 2]
#         self.change(A)
#         print (A)

#     def change(self, B):
#         B.append(B)

# P1 = ParameterPass(B)
# print(P1.change())

def increament(cls, newvar):
    newvar += 1

def main(cls, args):
    var = 10
    print("Value before increament :", var)
    cls.increament(var) 
    print("Value after increament :", var)   