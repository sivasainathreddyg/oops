class Collage:
    collage_name="RLJIT"  #static variable
    def __init__(self,name,age,rollno):
        self.name=name
        self.age=age
        self.rollno=rollno
    def display(self):
        print("student name:",self.name)
        print("student age:",self.age)
        print("student rollno:",self.rollno)
Collage.collage_name="EDYODA"

print(Collage.collage_name)
collage1=Collage("siva",21,30)
collage1.display()

print(Collage.collage_name)
collage2=Collage("vishnu",22,100)
collage2.display()

print(Collage.collage_name)
collage3=Collage("upendra",21,97)
collage3.display()
