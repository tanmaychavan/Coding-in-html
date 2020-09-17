print('1. Square')
print('2. Cube')
choice = eval(input('Enter your choice: '))
num = eval(input('Enter any number: ',))
if choice == 1:
    print('The square of', num ,'is' , num*num )
elif choice == 2:   
    print('The cube of', num ,'is', num*num*num,'.' )
else:
    print("This choice is not available")

    
