#1 split() method takes string and gives us list 

message = input(" enter your message please: ")
print(message.split())

#2 strip() method gives us spacess 
message = input(" enter your message please: ")
print(message.strip())


#3
message = input("enter your input please :")
words = message.split(" ")
emojis = {

    ":)" : "smile emoji",
    ":(" : "sad emoji"

}

output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)