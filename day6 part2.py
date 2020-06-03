#dictionaries:
#a customer have name,id, email, phn no, address etc


#1
customer = {
    "id" : 1, 
    "name": "tamjid",
    "address" : "mirpur",
    "phn no:" : "01718044655",
    "email" : "tamjid@gmail.com",
    "age" : 30,
    "is_varified" : True


}
print(customer.get("name"))
print(customer["age"])
print(customer.get("age"))
print(customer)
customer["name"] = "aynul islam"
print(customer)
customer["name"] = "Tamxeed Islamm"
print(customer)
customer["address"] = "Mirpur 10"
print(customer)
print(customer["address"])
print(customer.get("address"))

phone = input("phone: ")

digit_mapping = {

"1" : "one",
"2" : "two",
"3" : "three",
"4" : "four",
"5" : "five",
"6" : "six",
"7" : "seven",
"8" : "eight",
"9" : "nine",
"10" : "ten"
"0" "zero"
}

output = ""

for char in phone:
    output += digit_mapping.get(char) + " "
print(output)


entry = input("enter entry: ")
new_dict = {

"1": "mango",
"2" : "apple",
"3" : "banana",
"4" : "orrange",
"a": "akram",
"b" : "nahian",
"c" : "sabik",
"d" : "ameka",

} 

new_output = ''

for value in new_dict:
    new_output += new_dict.get(value) + " "
print(new_output)
    
