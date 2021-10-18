num1 = int( input("Enter value for num1: "))  
num2 = int( input("Enter value for num2: "))  

#values before swapping
print ("The Value of num1 before swapping: ", num1)  
print ("The Value of num2 before swapping: ", num2) 

# To swap the value of two variables  
# we will user third variable which is a temporary variable  
temp = num1 
num1 = num2  
num2 = temp 

#values after swapping
print ("The Value of num1 after swapping: ", num1)  
print ("The Value of num2 after swapping: ", num2) 
