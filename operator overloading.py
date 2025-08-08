class A:
    def __init__(self,a):
        self.a= a
    def __lt__(self,other):
        if self.a<other.a:
            return "object1 is less than object2"
        else:
            return "object2 is less than object1"
    def __eq__(self, other):
        if self.a == other.a:
            return "both are equal"
        else:
            return "they are not equal"
obj1=A(8)
obj2=A(5)
print("given values", obj1.a,obj2.a)
print(obj1<obj2)
obj3=A(4)
obj4=A(3)
print("given values are",obj3.a,obj4.a)
print(obj3==obj4)