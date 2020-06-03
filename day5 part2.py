#1
a = ['a','b','c','d',['a',2,'m'], (1,3,'k'), {'name':'tamjid','age':28}]
a[5] = "hello"
print(a)
print(a[5])
print(a[-1])
print(a[2:-1])
print(len(a))
m = (a.append("aynul"))
print(m)

#2 largest number print in list

number = [2,4,6,8,10]
max_num = number[0]
for value in number:
    if value > max_num:
        max_num = value
print(max_num)
#print(max(number))


#practice
value = [2,4,6,8,10,100]
max_value = value[0]
for item in value:
    if item > max_value:
        max_value = item
print(max_value)

