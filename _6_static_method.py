#static method-- use to create utilities
#             ---deals with local and global variables

sname="siva"
class human:
    def __init__(self,name):
        self.name=name

    @staticmethod
    def utility():
        return f"hey {sname}"
        
human_obj=human("raj")
data=human_obj.utility()
print("name:",data)