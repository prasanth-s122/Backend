import pandas as pd # type: ignore
d1 = {"dept_no":[10,20,30],"dept_name":["IT","HR","DA"], "location" : ["Chennai","Coimbatore","Erode"]}
df = pd.DataFrame(d1)

print(df)

