#Funcion in Python:

def text_fun(): #when we called our function then this two line will executed which located in our function
    print("Hi!, The Functhion is started right now")
    print("hi function")


print("please write your funcion now!")
text_fun()
print("Yeah ths is my 1st function")


#2 Parameter in function
def abroad_user(name):
    print(f"hi {name}")
    print("welcome to the ireland")


abroad_user("tamjid")
abroad_user("nahiyn")


#practice

def sports(name):
    print(f"lets's Play {name}!")


print("hey! today is sports day!")
sports("football")


#practice

def result(number,fail,passed):
    print(f"{number} have got A+, {fail}  failed, total {passed} passed ")


print("there are 200 students in a school")
result("50 students","20 students","160 students")


#practice 
def family(first,second,third):
    print(f"first {first} from dhaka, second {second} from ctg, last  {third} from noakhali")

print("there are sixty family in a apartment")


family("thirty","twenty","ten")


#practice

def student(six,seven,eight,total):
    print(f'''hello tamjid, 
    class six have {six} students,
    class seven have {seven} students,
    class eight have {eight} students
    total students are {total}
    
    ''')


student(100,200,300,600)



#return functions value

def square(number):
    return number*number

square(100)
result = square(100)

print(result)

#practice

def calc(value,student,teacher,school):
    return (value-(student+teacher+school))

calc(12000,1893,3546,5657)
remain = calc(12000,2000,3000,5000)
print(remain)


#practice

def salary(basic,conv,houserent,vat):
    return(basic+conv+houserent-vat)


salary(12000,3000,8000,300)
gross = salary(12000,3000,8000,300)
print(gross)

#practice

def market(amount,meat,vegitbables,oil,riksha):
    return(amount-(meat+vegitbables+oil+riksha))


market(10000,5000,1000,2000,60)

remain_amount = market(10000,5000,1000,2000,60)
print(remain_amount)


#practice

def left(total,six,seven,eight,nine,ten):
    return(total-(six+seven+eight+nine+ten))


left(10000,2000,1000,1000,1000,2000)

bal = left(10000,2000,1000,1000,1000,2000)
print(bal)
