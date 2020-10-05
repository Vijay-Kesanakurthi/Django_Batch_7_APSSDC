''' class Hello: # Create a Class
    a = 10
    b = 20
    def display(): # userdefine Function
        print("hello iam display Function")
    
Hello.display() # Calling Function
print(Hello.a)
print(Hello.b)
'''
'''
# mathematical operatoions
class Math:
    def add(a,b):
        return a + b
    def sub(a,b):
        return a - b
    def mul(a,b):
        return a * b
# create object for class Math
mt = Math
print("Add is:",mt.add(10,5))
print("mul is:",mt.mul(50,5))
'''

'''
class Raj:
    # python OOPS Concepts and techniques
    # Django Framework
    
    def feature():
        f = ['python','multiple','inheritances']
        return f
    def applications():
        a = ['webdevelopment','machine learning','AI']
        return a

obj1 = Raj
print(obj1.feature())
print(obj1.applications())
print(obj1.__doc__)
'''

'''
class MathOperations:
    x,y,z = 10,30,40 # 80
    def sumNumbers():
        return MathOperations.x + MathOperations.y +MathOperations.z
    def multiply():
        return MathOperations.x * MathOperations.y #300

obj2 = MathOperations
'''

class Student:
    '''this student class gives information of student name and rollno'''

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno

    def display(self):
        return {'name':self.name,'rollno':self.rollno}

obj = Student('Prasanna Raj',2422)

print(obj.display())

































    









    
