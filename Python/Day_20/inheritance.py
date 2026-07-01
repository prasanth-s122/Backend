class python:
    def __init__(self):
        print("Python course")
    def loops(self):
        print("Loops")
    
    def functions(self):
        print("Functions")
    
    def pandas(self):
        print("Pandas")
    

class python_fullstack(python):
    def frontend(self):
        print("HTML,CSS,Bootstrap,Tailwind,Java Script,React")
    
    def sql(self):
        print("Query,JOIN,Sub Query,Nested Query,Normalisation,DDL,DML,DQL")

print("Single Inheritance")

s1 = python_fullstack()



s1.frontend()
s1.sql()
s1.loops()
s1.functions()
s1.pandas()