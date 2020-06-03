
#1
values = [10,20,30,40]
sum = 0
for value in values:
    sum += value
    print(sum)    #print loops inside sum


#2
x = [10,20,30]
y=['a','b','c']

for m in x,y:
    print(m)

#3
for x in range(0,20,2):
    for y in range(0,20,2): 
        print(f"{x} and {y}")

#4
items = [2,3,4,5,6,3,5]

for x_item in items:
    print(x_item * 'x')

#5 same problem different solve using nested loop
numbers = [2,5,7,9]
for x_numbers in numbers:
    output = ""
    for count in range (x_numbers):
        output += 'x'
    print(output)

#6 practice 

numbers = [10,7,4,1]
for x_number in numbers:
    new_output = ""
    for new_num in range(x_number):
        new_output += "%"
    print(new_output)
