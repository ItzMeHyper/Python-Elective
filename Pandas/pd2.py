import pandas as pd

# Read CSV file
df = pd.read_csv('employee.csv')

# 1. Print first 7 records
print("First 7 records:")
print(df.head(7))

# 2. Print employee names in alphabetical order
print("\nEmployee names in alphabetical order:")
print(df['name'].sort_values())

# 3. Name of employee with highest salary
print("\nEmployee with highest salary:")
print(df.loc[df['salary'].idxmax(), 'name'])

# 4. List names of male employees
print("\nMale employees:")
print(df[df['gender'] == 'Male']['name'])

# 5. Teams employees belong to
print("\nTeams:")
print(df['team'].unique())