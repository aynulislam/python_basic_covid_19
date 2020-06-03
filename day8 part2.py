#1 
try:
    age =int(input("enter your age: "))
    print(age)
except ValueError:
    print("invalid code")


#practice

try:
    age = int(input("enter your age: "))
    print(age)
except ValueError:
    print("value error")


#practice

try:
    int(input("enter your age please: "))
    print(age)
except ValueError:
    print("key error")


#2
try:
    number = int(input("enter your number: "))
    income = 20000
    risk = income/number
    print(risk)
except ZeroDivisionError:
    print("age cannot be 0")
except ValueError:
    print("invalid value")

#practice

try:
    salary = int(input("enter your salary please: "))
    houserent = int(input("enter your houserent please: "))
    conv = int(input("enter your conv please: "))
    vat = int(input("enter your vat please: "))
    cost = houserent+conv+vat
    remain = salary-cost
    print(f"your total cost is {cost}")
    print(f"your remain balance is {remain}")
except ValueError:
    print("input error")






