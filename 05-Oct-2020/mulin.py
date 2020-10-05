# Multiple Inheritance

class ClassA:
    def m1():
        return 'Class A'
class ClassB:
    def m2():
        return 'Class B'
class ClassC(ClassA,ClassB):
    def m3():
        return 'Class C'

obj17 = ClassA
obj27 = ClassB
obj7 = ClassC

print(obj7.m3())
print(obj17.m1())
print(obj27.m2())

