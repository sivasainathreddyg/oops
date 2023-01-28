#class method-are used to specifically deal with static/class variable


class Collage:
    collage_name="RLJIT"  #static variable/class variable
    def __init__(self,name,age,rollno):   #constructor
        self.name=name
        self.age=age
        self.rollno=rollno
    def display(self):         #instance method
        print("student name:",self.name)
        print("student age:",self.age)
        print("student rollno:",self.rollno)
    
    @classmethod
    def set_collage_name(cls,collage_name):
        cls.collage_name=collage_name
    
    @classmethod
    def get_collage_name(cls):
        return cls.collage_name
 

print(Collage.collage_name)
collage=Collage("siva",21,30)
collage.display()

cname=collage.get_collage_name()
print("collage_name:",cname)

collage.set_collage_name("coder")

cname=collage.get_collage_name()
print("collage_name:",cname)





