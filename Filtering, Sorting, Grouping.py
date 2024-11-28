import pandas as pd
data = pd.DataFrame({
    'name': ['moner','fahim','tushar','tanvir','tuhin'],
    'age':[10,20,30,40,50],
    'salary':[20000,21000,22000,23000,2400],
    'department':['tach','hr','sales','hr','tach']
})
# print(data.sort_values(by='age',ascending=True))
# print(data.groupby('department')['salary'].mean())
# print(data.groupby('department')['salary'].min())
# print(data.groupby('department')['salary'].max())
print(data.groupby('department')['age'].mean())

# print(data.min)