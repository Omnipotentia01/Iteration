#Repeat given message a given number of times.
#Tommy Cakebread

message = input("Please enter a message: ")
number = int(input("Please enter the nuber of time you would like to repeat it: "))

for count in range(number):
    print(message)
