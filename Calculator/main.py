# Calculator
from art import logo
print(logo)
# Add
def add(n1, n2):
  return n1 + n2

# Sub
def subtract(n1, n2):
  return n1 - n2

# Mul
def multiply(n1, n2):
  return n1 * n2

# Div
def divide(n1, n2):
  return n1 / n2

operation = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  num1 = float(input("What's the first number?: "))
  for symbol in operation:
    print(symbol)

  is_continue = True
  while is_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operation[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    is_continue_calculate = input(
      f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: "
    ).lower()
    if is_continue_calculate == "y":
      num1 = answer
    else:
      is_continue = False
      calculator()


calculator()