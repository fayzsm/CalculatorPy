def add(n1, n2):
  """Adds two inputs"""
  return n1+n2

def subtract (n1, n2):
  """Subtracts two ints"""
  return n1-n2

def multiply(n1,n2):
  """Multiplies two ints"""
  return n1*n2

def divide(n1,n2):
  """Divides two ints"""
  return n1/n2

operations={
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def format_num(n):
  if n.is_integer():
    return "{:.0f}".format(n)
  else:
    return "{:.2f}".format(n)

def calculator():
  num1= float(input("What is first number?: "))
  for symbol in operations:
    print(symbol, end=' ')
  
  oper_symbol=input("\nPick operation symbol from line above: ")
  num2= float(input("What is second number?: "))
  
  
  
  calc = operations[oper_symbol]
  answer = calc(num1, num2)
  answer=format_num(answer)
  num1=format_num(num1)
  num2=format_num(num2) 

  print(f"{num1} {oper_symbol} {num2} = {answer}")
  
  cont=input("Do you want to continue? y or n or x to exit ")
  flag=False
  if cont == 'y':
    flag = True
  elif cont == 'x':
    flag=False  
  else:
    calculator()
  
  while flag:
    for symbol in operations:
      print(symbol, end=' ')
    oper_symbol=input("\nPick operation symbol from line above: ")
    num2= float(input("What is next number?: "))
    calc = operations[oper_symbol]
    num1=answer
    answer = calc(answer, num2)
    answer=format_num(answer)
    num1=format_num(num1)
    num2=format_num(num2) 
    print(f"{num1} {oper_symbol} {num2} = {answer}")
    cont=input("Do you want to continue? y or n or x to exit")
    if cont == 'n':
      flag=False
      calculator()
    elif cont == 'x':
      flag=False

calculator()