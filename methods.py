class Students:
    college_name="Texas" #class variable

    def __init__(self,name,marks):  # constructor. , student name is object variable.
        self.name=name
        self.marks=marks

    def welcome(self):         #methos welcome
        print("welcome students",self.college_name,self.name)


    def get_marks(self):
        return self.marks
    
s1 = Students("Karan", 97)
s1.welcome()
print(s1.get_marks())
