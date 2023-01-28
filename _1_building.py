#class----blueprint
#object---it is instance of class
#methods-functions which are created inside the class
#        -every function defined inside the class must have self keyword as first parameter
#self -----its a keyword
#     -----it represent current class object

class Building:
    def door(self):  
        print("The building has total 20 doors")
    def doors(self,no_of_doors):  
        print(f"The building has total {no_of_doors} doors")
    def windows(self):
        print("The building has total 40 windows")
building=Building()  #object creation
building.door ()
building.windows()
building.doors(10)
