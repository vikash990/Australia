"""
Program 2: Use while(condition controlled),
for(count controlled) loop in programs or 
nested looping
"""

#Implementation: Print factorials of all numbers between 1 to 10

count=int(input("enter the number to print factorial series"))

#nested loop
for i in range(1,2*count+1):            #count controlled for loop
        factorial=1
        factor=i
        if i==count:                     # If statement to ask user to if he want to continue or not
                print("Do you want to continue?")
                choice=input("Enter the choice Yes  to continueor No to discontinue")  # taking input from the user
                if choice=="Yes" or "yes":   # if yes then we will continue
                        continue
                elif choice=="No " or "no":                         # if no then we will break
                        break
                else:
                        print("Wrong Choice")  # if choice is wrong then we will give output wrong choice
        while(factor>=1):                       #condition controlled while loop
                factorial*=factor
                factor-=1
        print("Factorial of",i,"is",factorial)  #prints factorial of the ith number
        

        
               

        
       
                
              
                        

