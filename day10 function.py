#practice

def recurs_exp(k):
    if k>0:
        result = k+recurs_exp(k-1)
        print(result)
    else:
        result = 0
    return result
print("recursion exmaple result")
recurs_exp(10)



def recurs(k):
    if k>0:
        result = k+recurs(k-1)
        print(result)
    else:
        result = 0
    return result

print(recurs(20))

def item(a):
    if a>0:
        value = a+item(a-1)
        print(value)
    else:
        value = 0
    return value

print(item(10))


def my_fun(m):
    if m>0:
        result = m+my_fun(m-1)
        print(result)
    else:
        result=0
    return result

print(my_fun(5))



def my_num(x):
    if x>1:
        result = x+my_num(x-1)
        print(result)
    else:
        result = 0
    return result

print(my_num(10))



def regular(a):
    if a>0:
        value = a+regular(a-1)
        print(value)
    else:
        value=0
    return value
print(regular(20))