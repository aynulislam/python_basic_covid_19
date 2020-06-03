

#1
name = "John Smith"
age = 20
is_patient = True

print(name)
print(age)
print(is_patient)


#2
name = input("What is your name? :")

print("my name is :" + name)


#3
name = input("enter your name:")
like = input("and you like:")

print('my name is' + ' ' + name + ' ' + 'and I like' + ' ' + like)


#4
birth_year = int(input('enter your birth year:'))
print(type(birth_year))
now_year = int(input('enter the now year: '))
print(type(now_year))
your_age =  int( now_year - birth_year)
print(type(your_age))
print(int (your_age))

#5
pound = float(input("enter your pound's number:"))
print(type(pound))
kg = float((pound) % 2.2)
print(type(kg))
print(float( kg ))

#6
a = "a is a letter"
b = a[:]
print(a)
print(b[1:-1])
print(b[2:6])

