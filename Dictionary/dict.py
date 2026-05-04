info = {}

print(info)

info["Name"] = "user1" 
print(info)


info["Age"] = 26
print(info)

info["Name"] = "Bob" 
info["Age"] = 36
info["Name"] = "Ravi" 
info["Age"] = 36
print("Updated Dictionary: ", info)


print("Users with age 36: ", info.get("Name", 36))