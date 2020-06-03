#multiple user input 

a, b, c = input('enter your age :').split()
print(a)
print(b)
print(c)


#all and any  conditions in list
age = 30
salary = 50000000
tax = 800

conditions =[
    age <= 30,
    salary <= 40000,
    tax <=500,
]
if all(conditions):
    print("salary procees in bank")
elif any(conditions):
    print("salary in cash")



#cross check value

subs = 200
likes = 100
print(subs, likes)

temp = subs
subs = likes
likes = temp

print(subs, likes)

#cross check shortcut
sub = 500
like = 800
print(sub,like)

sub,like = like,sub
print(sub,like)


#remove duplicate value
a = [1,2,3,4,2,3,4,2,2,3,2,4,5,6,6,7,4,6,7,8,10,11,9]
print(a)
print(list(set(a)))


#maximum number of duplicate value
m = [1,3,4,5,6,7,8,3,4,5,11,6,12,24,5,18,77,8,8,20,4,5,25,7,22,23,9,9,21,5,2,5,5,6,7,8,11,7,2,2,3,4,8,5]

max_dup = max(set(m), key=m.count())
print(max_dup)


print(list(set(m)))

#for loop in list

a = [for m in range(10) while m%2==0]