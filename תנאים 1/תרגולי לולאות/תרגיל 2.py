age=int(input("put age: "))
while age<0 or age>120:
    print("eror")
    age = int(input("put age: "))
else:
    if(age>=0)and(age<=20):
        print("child")
    if (age>=21) and(age<=60):
        print("adult")
    if (age>=61) and (age<=120):
        print("old")
