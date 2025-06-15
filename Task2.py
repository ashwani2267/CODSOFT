mode = input("Choose an operator (+, -, *, /, ^): ")

first_number = float(input("First Number: "))
second_number = float(input("Second Number: "))

if mode == "+":
    sum = first_number + second_number
    print(sum)
elif mode == "-":
    sum = first_number- second_number
    print(sum)
elif mode == "*":
    sum = first_number * second_number
    print(sum)
elif mode == "/":
    sum = first_number / second_number
    print(sum)
elif mode == "^":
    sum = first_number ** second_number
    print(sum)
else:
    print("Wasn't a compatible operator to begin with.")