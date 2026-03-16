import pandas as pd 

my_dict = {
    'name' : ["a", "b", "c", "d", "e", "f", "g"],
    'age' : [20, 27, 35, 55, 18, 21, 35],
    'designation' : ["VP", "CEO", "CFO", "VP", "VP", "CFO", "CEO"]
}

df = pd.DataFrame(my_dict)
print(df)

df.to_csv("employee.csv", index = False)
print("\nDataFrame saved to employee.csv")