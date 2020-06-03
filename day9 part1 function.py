#practice

def total(*numbers):
    initial_total = 0
    for number in numbers:
        initial_total *= number
    return initial_total
print(total(100,200,300,400))


#function practice

def amount(balance,waste):
    return(balance + waste)


print(amount(100,120))


#practice

def salary(basic,rent,conv,vat):
    return (basic+rent+conv+vat)

print(salary(12000,6000,6000,3000))


#practice

def gross(basic,conv,rent,food,vat):
    return(basic+conv+rent+food-vat)

gross(12000,3000,8000,4000,450)

amount=gross(12000,3000,8000,4000,450)
print(amount)




#practice

def my_func(*amounts):
    initial_value = 1
    for amount in amounts:
        initial_value *= amount
    return initial_value
print(my_func(10,20,30))

#practice
def multi(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total
print(multi(100,20,30,40))


#practice

def grosss_salary(*amounts):
    initial_salary = 0
    for amount in amounts:
        initial_salary += amount
    return initial_salary
print(f" total gross salary: {grosss_salary(12000,8000,3000,2000,1000)}")


#keywords argument

def user_list(**user):
    print(user)

user_list(id=1,name="tamjid",area="mirpur 2")



#pracice
def friend_list(**friend):
    print(friend)

friend_list(id=3,name="sabik", area = "mirpur 6")

#practice 

def company_list(**company):
    print(company)

company_list(id=4,name="DRL",area="mirpur")
company_list(id=5,name="DGL",area="gazipur")
company_list(id=6,name="GGl",area="gazipur")

#practice

def student_list(**student):
    print(student["age"])

student_list(id=7, name="abid", area="uttara", age=20)
student_list(id=8, name="shahi", area="feni", age=25)
student_list(id=9, name="shuvo", area="feni", age =30)
student_list(id=10, name="mithu", area="sathkhira",age=27)

#practice
