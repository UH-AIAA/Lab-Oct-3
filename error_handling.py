# code by Nathan Samuell

print("Script started!")

def divideNums(num1, num2):
  result = num1 / num2;
  print(result)


# This code works normally
divideNums(7, 9)
divideNums(9, 32)

# this code causes an error:
divideNums(8, 0)  # here, the program ends!!

# how can we handle this unexpected behavior?

def divideNumsWithErrorHandled(num1, num2):
  try:
    result = num1 / num2
    print(result)
  except ZeroDivisionError:
    print("Error: cannot divide by zero")
    print("Program keeps running!!")
  except Exception as e:
    print(str(e))


divideNumsWithErrorHandled(8, 0)



