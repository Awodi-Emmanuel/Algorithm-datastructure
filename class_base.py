class MyInt:
   value = 0
   def __str__(self):
        self.value +=1



P1 = MyInt()
print(P1.__str__())