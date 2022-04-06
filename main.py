def add(num1, num2) :
  return num1+num2
def substract(num1, num2) :
  return num1-num2
def devide(num1, num2) :
  return num1/num2
def multiply(num1, num2) :
  return num1*num2

operator_dictionary = {
  "+": add , 
  "-": substract ,
  "/": devide,
  "*": multiply 
}

from art import logo
print(logo)

num = float(input("What's your first number ? :"))
while True:
  operator = input("Operation +-/* ? :")
  second_num = float(input("What's next number ? :"))
  calculation = operator_dictionary[operator]
  answer = calculation(num, second_num)
  print(f"{num} {operator} {second_num} = {answer}")
  num = answer  
  
  if input("try again y/n ?:") != 'y':
    break