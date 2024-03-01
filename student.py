class student:
    def __init__(self,name,age,department,year):    
        self.name=name
        self.age=age
        self.department=department
        self.year=year
    def work(self):
        if(self.department=='cse'):
            print("software department and the student works on software")
        else:
            print("hardware department") 
s=student('sameena',19,'ece',3)           
s.work()
print(s.name)
print(s.age)
print(s.department)
print(s.year)