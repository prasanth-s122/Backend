from abc import ABC,abstractmethod

class course(ABC):
    @abstractmethod
    def frontend(self):
        print("HTML,CSS,Bootstrap,Tailwind,Java Script,React")
    
    @abstractmethod
    def sql(self):
        print("Query,JOIN,Sub Query,Nested Query,Normalisation,DDL,DML,DQL")
    
class full_stack(course):
    def frontend(self):
        print("For frontend")

    def sql(self):
        print("Database")
    
    def python(self):
        print("Full Stack")


a = full_stack()

a.frontend()
a.sql()
a.python()