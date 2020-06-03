

#1
First_name = "Aynul"
Last_name = " Islam"
Full_name = First_name + Last_name
message = (Full_name + ' ' +  "is a coder")
msz = f'{First_name}{Last_name} is a coder'   #both printed same output 

print(message)
print(msz)
print(len(message))
print(message.upper())
print(message.lower())
print(message.find('I'))
print(message.replace('Islam','Tamjid'))
print(message.replace('A','M'))
print('Aynul' in message)


#2
a = 7
b = 3
c = a/b
d = a//b
e = b**a

print(int(c))
print(float(c))
print(c)
print(d)
print(e)


#3
x = 10
x = x+10
x += 3
x -= 10
print(x)


#4
m = (3 + 19) * (4 ** 2)
x = 3 + 19 * 4 ** 2.4
y = 3 - 19 * 4 ** 2.4

print(m)
print(x)
print(round(x))
print(y)
print(abs(y))


#5
import math

a = 2.67
print(math.ceil(a))
print(math.floor(a))
print(math.factorial(int(a))) # bcz factorial only accept integer value 



