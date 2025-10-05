expression = str(input("Enter expression (like 1+1): "))

if expression.count("+") == 1:
    a, b = expression.split("+")
    result = float(a) + float(b)

elif expression.count("-") == 1:
    a, b = expression.split("-")
    result = float(a) - float(b)

elif expression.count("*") == 1:
    a, b = expression.split("*")
    result = float(a) * float(b)

elif expression.count("/") == 1:
    a, b = expression.split("/")
    result = float(a) / float(b)

else:
    result = "my calculator can only add, subtract, multiply, and divide two numbers."

print("Result:", result)