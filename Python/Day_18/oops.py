class sla:
    student_count = 100

    def datascience(self):
        time = '1.5 months'
        print(time)
        print("ML","DL","AI",end ='\n')
    
    def full_stack(self):
        time = '1 month'
        print(time)
        print("Frontend","SQL","Backend",end='\n')


kk = sla()

kk.datascience()

kk.full_stack()

print(kk.student_count)