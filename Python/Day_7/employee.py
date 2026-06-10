import pandas as pd  # type: ignore
employee = {"emp_id" : [1,2,3,4,5] , "emp_name" : ["Prasanth","Loki","James","Jack Sparrow","Connor"] , "emp_deptno" : [100,200,300,400,500] , "emp_salary" : [100000,205000,33000,40000,50000] , "emp_role" : ["Engineer","Finance Manager","Junior Developer","Senior Developer","HR manager"]}
df = pd.DataFrame(employee)
print(df)

print("Salary under 50000 ----> \n",df[df["emp_salary"]<= 50000])

d1 = {"dept_no":[10,20,30],"dept_name":["IT","HR","DA"], "location" : ["Chennai","Coimbatore","Erode"]}
df1 = pd.DataFrame(d1)

print(df1)

print(df[df["location"]=="Erode"])