#Accept two integer numbers from a user and return their
#product and if the product is greater than 1000,then return their sum
def sum_or_multiplication(num1, num2):
  product = num1 *num2
  if(product <= 1000):
    return product
  else:
    return num1 +num2
num1 = int(input("Enter First Number"))
num2 = int(input("Enter Second Number"))
result = sum_or_multiplication(num1, num2)
print("The result is", result)
