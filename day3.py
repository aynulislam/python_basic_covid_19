


#1
is_student = True

if is_student:
    print("hei students, read the book")
print("enjoy your day")

#2
is_teacher = False
if is_teacher:
    print("hei teacher, go to your classroom")
print("hello teacher, dont go to your class please")


#3
is_hot = True

if is_hot:
    print("wear slim fabric")

else:
    print("wear fat fabric")
print("enjoy your day")

#4
is_hot = False

if is_hot:
    print(" wear slim fabric")
else:
    print("wear cold fabric")
print("enjoy your day")

#5
is_hot = True
is_cold = False

if is_hot:
    print("wear slim fabric")
    print("stay healthy")
elif is_cold:
    print('wear hot fabric')
    print('saty safe')
else:
    print("have a nice day")

#6
is_hot = False
is_cold = False

if is_hot:
    print("really hot")
elif is_cold:
    print("its really cold")
else:
    print("have a nice day yaar")

#7
price = float(input("enter your total price: "))
#vat = float(input("enter your total vat: "))

is_cash_credit = False
is_in_bank = True
vat = float(price /22.4)
if is_cash_credit:
    print(f"your salary is: {price} $")
elif is_in_bank:
    print(f"your salary is {price-vat} $ ")
else:
    print(f"your salary is{price} $")


#8
has_high_income = True
has_good_credit = True
has_criminal_record = True

if has_high_income and has_good_credit:
    print("eligable for Loan")
else:
    print("not eligible for loan")


if has_high_income or has_good_credit:
    print("loan no accepted")
else:
    print("please maintain all task for loan")

if has_good_credit and not has_criminal_record:
    print(" give them loan")
elif has_good_credit and has_criminal_record:
    print(" not giving any type of loan")
else:
    print("arrest them")
  

#9
is_temp = float(input("enter your tem: "))

if is_temp>30:
    print("it's hot day")
elif is_temp<=20:
    print("it's cold day") 
else:
    print(" normal day")


#10
name = str(input("enter your name pleae:"))

if len(name)==3:
    print(f"{name} has a 3 charaacter")
elif len(name)<10 and len(name)>3:
    print(f"{name} has more than 3 character and less than 10 character")
else:
    print(f"{name} has undefined character")

#11
weight = int(input("enter your weight :"))
unit = (input("pound or kg : "))
print(type(unit))

if unit == "pound":
    converted = weight * 0.45
    print(f"you are  {converted} kg")
else:
    converted = weight / 0.45
    print(f"you are  {converted} pound")





