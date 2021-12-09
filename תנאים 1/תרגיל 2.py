num=int(input('put a number'))
if num>=100 and num<=999:
    print(int(num%10)+(num//10%10)+(num//100))
else:
    print("erorr")