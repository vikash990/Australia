"""
Program 1: Use simple functions which 
passes on user inputs to a function 
which performs the operation and returns 
the result to be displayed on the console.
"""

def Operation(value1, value2):		#function to recieve inputs from calculate() and return the desired operation of those inputs
        print("operation")              # Ask user to eneter his choice for operation
        print("1 for operation")         
        print("2 for subtraction")    
        print("3 for multiplication")
        print("4 for multiplication")
        choice=int(input("Enter You Choice"))   # Ask user to enter the desired choice for the opeartion
        if choice==1:                           # Perform addition
                return value1+value2
        elif choice==2:                          # Perform Subtraction
                return value1-value2
        elif choice==3:                          # Perform multiplication 
                return value1*value2
        elif choice==4:                         # Perform Division
                return value1/value2
        else:
                print("wrong coice")
        
	 

def calculate():						#function to input values, pass them to calculateSum() and print returned answer
	number1=int(input("Enter the first number: "))
	number2=int(input("Enter the second number: "))
	answer=Operation(number1,number2)						#calling calculateSum() function with inputs passed as parameters
	print("The operation  of",number1,"and",number2,"is",answer)

calculate()								#calling calculate() function
