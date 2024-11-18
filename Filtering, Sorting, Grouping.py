import pandas as pd
data = pd.read_csv("percent_bachelors_degrees_women_usa.csv")
# print(data.iloc[15])
data = pd.DataFrame({
    'a1':[1,2,3],
    'a2':[4,5,6],
    'a3':[7,8,9],
},index=['x','y','z'])
print(data)

print(data.loc['x'])