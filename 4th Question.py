#Accept string from a user and display only those characters
#which are present at an even index number
def EvenChar(str):
  for i in range(0, len(str)-1, 2):
    print(str[i] )

inputStr = input("Enter String ")

print("Printing only even characters")
EvenChar(inputStr)
