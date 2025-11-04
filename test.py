# ejercicio 1
temperature = int(input("Enter the temperature: "))

if(temperature < 0):
    print("Freezing weather")


# ejercicio 2

number = int(input("Enter a number: "))

if(number > 0):
    print("Positive")
else:
    print("Not Positive")


# ejercicio 3

currentHour = int(input("Enter the hour: "))

if(currentHour < 12):
    print("Good morning")
elif(currentHour < 18):
    print("Good afternoon")    
else:
    print("Good evening")


# ejercicio 4 

traficLight = input("Enter the color: ")

if(traficLight == "red"):
    print("Stop")
elif(traficLight == "yellow"):
    print("Ready")    
elif(traficLight == "green"):
    print("Go")
else:
    print("Invalid color")

# ejercicio 5 

for x in range(1,11):
  print("Value: ", x)


# ejercicio 6

for x in range(1,21):
  if(x % 2 == 0):
    print("Even number: ", x)

# ejercicio 7
for x in input("Enter your name: "):
  print(x)


# ejercicio 8
index = 10
while(index > 0):
   print("Value: ", index)
   index -= 1


# ejercicio 9
password = "admin123"
entry = ""
# while(True):
#    if(input("Enter password: ") == "admin123"):
#       print("Access granted!")
#       break

while(entry != password):
   entry = input("Enter password: ")
print("Access granted!")



# ejercicio 10

def isOdd(number):
   return number % 2 != 0

num1 = int(input("Enter a number: "))
print("Is it odd Number: ", isOdd(num1))

# ejercicio 11

def isEven():
    num2 = int(input("Enter a number: "))
    if(num2 % 2 == 0):
       print("Even")
    else:
      print("Odd")

isEven();

# ejercicio 12

def square(num):
   return num * num

print("Square value is: ", square(int(input("Enter a number: "))))