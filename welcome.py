class Student:
    college_name="Texas"

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks


    def Welcome(self):
        print("Welcome student,",self.name)

    def Get_marks(self):
        return self.marks

s1= Student("Karan",97)
s1.Welcome()
print(s1.Get_marks())