import pandas as pd

df=pd.read_csv('employee.csv')
df.drop(columns=['Position','DOB','Marital Status','Gender','Hire Date','Salaried','Vacation Hours','Sick Leave Hours','Encrypted Password','Modified'])
data=df.head()
data.to_csv('testfile', index=False)
print(data)