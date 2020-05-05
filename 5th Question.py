start = int(input("Enter starting Number"))
end = int(input("Enter ending Number"))
print("Prime numbers in the range are: ",)
for val in range(start, end + 1):
    if val> 1:
        for n in range(2, val//2 + 2):
            if (val % n) == 0:
                break
            else:
                if n == val//2 + 1:
                    print(val)
                    break
num=int(input("Enter the number"))
for i in range(2,num):
        if (num % i )==0:
            print(num,"is not a prime number")
            break
else:
        print(num,"is a Prime number")


