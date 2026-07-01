class sla:
    def __init__(self,sc,stc):
        self.student_count = sc
        self.staff_count = stc
        print("Start")
    
    def data_count(self):
        print("DA,DS")
    
    def frontend(self):
        print("Java,Python")


kk = sla(150,60)
n1 = sla(100,20)

print(f"Student count in KK nagar ----> {kk.student_count}")
print(f"Staff count in KK nagar ----> {kk.staff_count}")

print(f"Student count in Navalur ----> {n1.student_count}")
print(f"Staff count in Navalur ----> {n1.staff_count}")

