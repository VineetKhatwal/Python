dict = {'Name':"Vineet",'ID':10,"Salary":4050.35}
print(dict)
print(dict['Name'])
print(dict['ID'])
print(dict['Salary'])

print("Dictionary doesn't support indexing or Slicing")
print(len(dict))
print("------------- Updating the Value-----------------")
dict['Salary'] = 5000.00
print(dict)
print("------------- Adding the Value-----------------")
dict['Dept']="Finance"
print(dict)
print("------------- Deleting the Value-----------------")
del dict["Dept"]
print(dict)
print("------------- Availability of the Value-----------------")
print('Dept' in dict)
print('Name' in dict)
print('Dept' not in dict)
print('Name' not in dict)
print("------------- Duplicate keys are overridden-----------------")
dict['Name'] = "Test"
print(dict)

print("-------------- Dictionary Methods -----------------")
print("--------------- Deep Copy -------------")
dict2 = dict.copy()
print(dict2)
dict2["Dept"]="Finance"
print(dict2)
print(dict)
print("--------------- Update Value -------------")
dict2.update({"Dept":'QA'})
print(dict2)
dict2.update({"Temp":'test_update'})
print(dict2)

print("--------------- Keys and Values-------------")
print(dict2.keys())
print(dict2.values())
print(dict2.items())

print("--------------- GET-------------")
print(dict2.get('ID'))
print(dict2.get('NotPresent',"Notfound"))

print("--------------- POP -------------")
print(dict2)
print(dict2.pop('Temp'))
print(dict2)

    
print("-------- eval() function to create dictionary---------")
dict1 = eval(input("Enter elements in the dictionary : {} - "))
print(dict1)
print(sum(dict1.values()))

