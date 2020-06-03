#for loop in python

#1
for item in "python":
    print(item)

#2
for number in [1,2,3,4,5,6,7,8,9]:
    print(number)

#3
for item in range(0,100,10):
    print(item)

#4
for item in ["id","name","email","website","age"]:
    print(item)

#5
value = [1890,76896,305069,5678]
total = 0
for amount in value:
    print(f"my single amount is {amount}")

#6
prices = [10,20,30,40]
total = 0
for amount in prices:
    total += amount
print(f"total value is {total}")   #print initially total, outsides loops total

