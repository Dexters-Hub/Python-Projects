def add(P, Q):    
   # Function used for adding two numbers   
   return P + Q   
def subtract(P, Q):   
   # Function used for subtracting two numbers   
   return P - Q   
def multiply(P, Q):   
   # Function used for multiplying two numbers   
   return P * Q   
def divide(P, Q):   
   # Function used for dividing two numbers    
   return P / Q    
# Taking inputs from the user    
print ("Select the operation.")    
print ("a. Add")    
print ("b. Subtract")    
print ("c. Multiply")    
print ("d. Divide")    
    
choice = input("Please enter choice (a/ b/ c/ d): ")    
    
num1 = int (input ("Please enter the first number: "))    
num2 = int (input ("Please enter the second number: "))    
    
if choice == 'a':    
   print (num1, " + ", num2, " = ", add(num1, num2))    
    
elif choice == 'b':    
   print (num1, " - ", num2, " = ", subtract(num1, num2))    
    
elif choice == 'c':    
   print (num1, " * ", num2, " = ", multiply(num1, num2))    
elif choice == 'd':    
   print (num1, " / ", num2, " = ", divide(num1, num2))    
else:    
   print ("This is an invalid input")    
