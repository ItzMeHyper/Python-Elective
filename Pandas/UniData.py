import pandas as pd 

uni_data = {
    'Reg.No' : ["ABC123", "ECH265", "FET345", "GMT734"],
    'Name' : ["Ganesh Kumar", "John Mathew", "Reena K", "Adil M"],
    'Semester' : ["S8", "S7", "S6", "S5"],
    'College' : ["ABC", "ECH", "FET", "GMT"],
    'CGPA' : [9.8, 9.9, 9.7, 9.75]
}

df = pd.DataFrame(uni_data)
print(df)

df.to_csv("University Data.csv", index = False)
print("\nDataFrame saved to University Data.csv")