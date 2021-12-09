age=int(input("put age"))
while age<0 or age>120:
    print("eror")
    age = int(input("put age"))
    if(age>=0)or(age<=20):
        print("child")
    if (age>=21) or(age<=60):
        print("adult")
    if (age>=61) or (age<=120):
        print("old")
