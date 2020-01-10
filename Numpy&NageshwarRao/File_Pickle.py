import pickle

class Emp:

    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal

    def display(self):
        print("{:5d} {:20s} {:10.2f}".format(self.id,self.name,self.sal))

f = open("/Users/Shaheen/Desktop/Vineet/MS_SE_Spring2019/Python/Files/picke.dat",'wb')
n = int(input("How many records"))

for i in range(n):
    id = int(input("Please enter the id"))
    name = input("Please enter the name")
    sal = float(input("Please enter the salary"))

    e = Emp(id,name,sal)
    pickle.dump(e,f)

f.close()

f = open("/Users/Shaheen/Desktop/Vineet/MS_SE_Spring2019/Python/Files/picke.dat",'rb')
print("Employee Details")
print("----------------")

while True:
    try:
        obj = pickle.load(f)
        obj.display()
    except EOFError:
        print("EOF Reached")
        break

f.close()
                      
             
    
