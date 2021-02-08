def add (x, y):
  return x + y

def subtract (x, y):
  return x - y

def multiply (x, y):
  return x * y

def divide (x, y):
  return x / y

def remainder (x, y):
  return x % y

def menuCal():
  print("Select a operator")
  print ("1. Add")
  print ("2. Subtract")
  print ("3. Multiply")
  print ("4. Divide")
  print ("5. Remainder")


def calculator ():

  choice = input("Select Choices:")

  while choice != "0":
    print("\n")

    if choice in ("'1', '2', '3', '4', '5'"):

      num1 = int(input("Enter first number: "))
      num2 = int(input("Enter second number: "))

      if choice == '1':
        print (num1, '+', num2, '=', add(num1, num2))

      elif choice == '2':
        print (num1, '-', num2, '=', subtract(num1, num2))

      elif choice == '3':
        print (num1, '*', num2, '=', multiply(num1, num2))

      elif choice == '4':
        print (num1, '/', num2, '=', divide(num1, num2))

      elif choice == '5':
        print (num1, '%', num2, '=', remainder(num1, num2))
    else:
      print("Invalid! Select a number from 1 - 5 : ")
      choice = input("Select Choices:")


    print("Would you like to calculate another? (1 for yes | 2 for no)")
    select = input("Selection : ")
    if(select == '2'):
      print("\n")
      menuCal()
      calculator()

menuCal()
calculator()
