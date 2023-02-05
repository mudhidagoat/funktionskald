import string

alphabet = string.ascii_letters

num1 = input("skriv det første nummer: ")
if num1 in alphabet:
    print("skriv et tal")
else:
    num1 = float(num1)
op = input("skriv dit beregningsform: ")
num2 = float(input('skriv det andet nummer: '))
if num2 in alphabet:
    print("skriv et tal")
else:
    num2 = float(num2)



if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("du skal write to tal kom nu")
