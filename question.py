
#Create a students class that takes name and maeks of 3 subjects as an arguments in constructor. Then create a method to print the average.


class Students:
    def __init__(self,name, marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
    # return total/3.    # this code is used to return value out of function 
        print("Hi", self.name,"Your average score is :",sum/3)

s1=Students("Umesh",[99,98,97])
s1.get_avg()
#avg=s1.get_avg()
#print("Hi", self.name,"Your average score is :",avg)
 


