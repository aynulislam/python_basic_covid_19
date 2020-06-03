#car game advance
car_started = False
command = ""
while True:
    command =  input("enter your command please: ")
    if command == "start":
        if car_started:
            print("car is being started")
        else:
            car_started == True
            print("car is runnig")
    elif command == "stop":
        if not car_started:
            print("car is alredy stopped")
        else:
            car_started == False
        print("stop the car")
    elif command == "help":
        print("""

start = start the car       
stop = stop the car
slow = slow the car
quit = quit the car game

        """)
    elif command == "quit":
        print(" I quit the car game")

    else:
        print(' this car game is not for me')
    break




#1
i=0
while i<=10:
    print('*' * i)
    i+=1
print("ok")

#2
i=1
while i<=10:
    if i%2==0:
        print(i)
    i+=1
print("yes got difference ")

#3
i=0
while i<10:
    if i%2!=0:
        print("even number")
    i+=1
print("we got even number")

#4 number guess game

my_guess = 10
number = my_guess * 10
guess_count = 0
chance = 3
while guess_count<chance:
    guess_no = int(input("enter your guess no: "))
    guess_count += 1
    if guess_no == number:
        print("you gues right number")
        break
        #guess_count += 2
    else:
        print("you are wrong, try again ")
else:
    print(f"sorry you are failed, the correct ans is {number}")
        

#5 car start game 

command = str(input("enter your command :"))
if command.lower() == "start":
    print("hey start the car")
elif command.lower() == "stop":
    print("hey stop the car")
elif command.lower() == "slow":
    print("slow the car")
else:
    print("command not acceptable")


#car game
command = ""
while True:
#while command!="quit":
    command = input("enter your car command :").lower()
    if command == "start":
        print("start the car please")
    elif command == "stop":
        print("please stop the car")
    elif command == "help":
        print(""" 

start = start the car
stop = stop the car
slow = slow the car
quit = quit this program

        """)
    elif command == "slow":
        print("slow the car") 
    elif command == "quit":
        break
    else:
        print("this car is not for me")

 
#car game advance
car_started = False
command = ""
while True:
    command =  input("enter your command please: ")
    if command == "start":
        if car_started:
            print("car is being started")
        print("start the car")
    elif command == "stop":
        if not car_started:
            print("car is alredy stopped")
        else:
            car_started == False
        print("stop the car")
    elif command == "help":
        print("""

start = start the car       
stop = stop the car
slow = slow the car
quit = quit the car game

        """)
    elif command == "quit":
        print(" I quit the car game")

    else:
        print(' this car game is not for me')
    break



     







