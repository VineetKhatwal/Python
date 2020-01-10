reclen = 20

with open("/Users/Shaheen/Desktop/Vineet/MS_SE_Spring2019/Python/Files/City.bin",'wb') as f:
    n = int(input("How many records"))
    for i in range(n):
        city = input("Please enter the city name")
        ln = len(city)
        city = city + (reclen-ln)*" "
        city = city.encode()
        f.write(city)

with open("/Users/Shaheen/Desktop/Vineet/MS_SE_Spring2019/Python/Files/City.bin",'rb') as f:
    n = int(input("Enter record number"))
    f.seek(reclen * (n-1))
    str=f.read(reclen)
    print(str.decode())


