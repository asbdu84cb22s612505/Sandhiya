def recursion_fact(x):
  if x == 1:
    return 1
  else:
    return (x * recursion_fact(x - 1))


num = int(input("enter a number:"))
if num >= 1:
  print("the factorial of", num, "is", recursion_fact(num))