#1 two dimensonal list

matrix = [
   [10,20,30],
   [12,16,18],
   [15,25,35],

]
print(matrix[0][0])
print(matrix[1][2])
print(matrix[2][1])


for row in matrix:
    for item in row:
        print(item)



#practice
mat = [

[1,2,3,],
[2,3,4,],
[4,5,6],

]

for a in mat:
    for b in a:
        print(b)

#2
numbers = [1,2,3,4,6,7,8,9]
print(numbers)

numbers.append(30)  #insert item in last index
print(numbers)

numbers.insert(0,10) #insert new item in specific index
print(numbers)

numbers.sort()    #sort the list
print(numbers)

numbers.remove(30) #remove specific item
print(numbers)

numbers.pop()     #remove last item of a list
print(numbers)


print(numbers.count(5)) #count how many times 5 in the list
numbers.count(100)  #count the all item in the list by key words
print(numbers)

print(numbers.index(2)) #print the specific index number by his keywords item


numbers.reverse() #reverse all item in the list
print(numbers)

numbers_2 = numbers.copy() #copy the full list in new list
print(numbers_2)

numbers.clear()   #remove all items in a list
print(numbers)



new_list = [ 'tamjid', 'islam', 'naim', 'hasan'] #print the specific index number by his keywords item 
print(new_list.index('hasan'))



#3 remove duplicate item in the list

numbers = [2,2,4,5,6,7,7,8,11,3,4,7,9]
null_list = []
for number in numbers:
    if number not in null_list:
        null_list.append(number)
print(null_list)

#practice 

ages = [10,20,11,20,17,18,30,35,20,10,35,18]
null_age = []

for age in ages:
    if age not in null_age:
        null_age.append(age)
print(null_age)
null_age.sort()
print(null_age)

#tuples
#tuples have only two method count and index 

numbers = (10,10,1,20,20,20,30)
print(numbers.count(20))
print(numbers.index(10))


#unpacking tuple,list

coordinates = (10,12,20)
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

print(x * y * z)

x,y,z = coordinates
print(x*y*z)


coordinates_1 = [10,20,30]
x,y,z = coordinates_1
print(x+y+z)
