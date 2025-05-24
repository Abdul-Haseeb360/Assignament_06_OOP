class A():
    def show(self):
        print("Show form A")

class B(A):
    def show(self):
         print("Show form B")

class C(A):
    def show(self):
         print("Show form C")   
    
class D(B, C):
    pass

object1 = D()
object1.show()
print(D.__mro__)