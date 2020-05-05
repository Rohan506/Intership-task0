#Accept n number from user and calculate the sum of all number between 1 and n including n
n=input("Enter Number")
n= int(n)
sum=0
for num in range(0, n+1, 1):
    sum = sum+num
print("SUM of first", n, "numbers is:",sum )
