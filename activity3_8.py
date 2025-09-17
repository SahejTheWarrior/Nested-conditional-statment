#your customised ride
print("select you'r ride")
print("1. bike")
print("2. car")
choice=int(input("enter you'r choice: "))
if(choice==1):
    print("what type of bike")
    print("1. scooty\n")
    print("2. scooter\n")
    choice2=int(input("enter your choice2:"))
    if(choice2==1):
        print("you have selected scooty")
    else:
        print ("you have selected scooter")
elif(choice==2):
    print("what type of car do you want?")
    print("1. Range Rover")
    print("2. Tesla")
    choice3=int(input("enter your choice3:"))
    if choice3==1:
        print("you have selected Range Rover")
    else:
        print("you have selected Tesla") 
else:
    print("wrong choice!!!")