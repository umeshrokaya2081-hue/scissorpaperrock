class Student: #creating class
     #default constructor
    def __init__ (self):
        pass
    college_name="Texas college "
    name="Anonymous" #Class Attribute
    #parameterized constructor
    def __init__ (self,name,marks):
        self.name=name #instance/Object attribute 
        self.marks=marks #instance attribute 
        print("Adding new students in database ....")
    name="ram"

s1=Student("Umesh",98)
print(s1.name,s1.marks)
print(s1.college_name)

s2=Student("",55)
print(s2.name,s2.marks)
print(s2.college_name)
