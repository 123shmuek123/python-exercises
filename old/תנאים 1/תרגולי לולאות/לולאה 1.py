num=int(input("put number"))
while num<100 or num>999:
    print("eror")
    num=int(input("put number"))
else: print((num%10)+(num//10%10)+(num//100))



