#it is a special kind of method
#it is defined using __init__()
#you need not have to call it explicitly ,it gets called automatically when a object is created
#it is used to create  an object
#it is use to initialize instance variable
#constructor has same name as class name

#NOTE----it is  not recommanded to write logical code in inside constructor

# class constructor():
#     def __init__(self):
#         print("constructor")
# obj=constructor()   #creating object


#it is use to initialize instance variable
class constructor:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"name :{self.name} and age:{self.age}")
obj=constructor("siva",21)
obj.display()



# class employee:
#   def __init__(self, first, last, salary):
#     self.first = first
#     self.last = last
#     self.salary = salary
#     self.email = first + '.' + last + '@edyoda.com'

#   def fullname(self):
#     return 'first name {} and last name {} and the salary is {}'.format(self.first, self.last, self.salary)

#   def apply_value(self):
#     print(self.salary * 200)
# emp1=employee("siva","sai",1000000)
# print(emp1.email)
# print(emp1.fullname())
# emp1.apply_value
