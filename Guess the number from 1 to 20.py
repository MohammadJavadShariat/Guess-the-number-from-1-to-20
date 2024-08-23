import random 
a, b = 1 , 20

#Choose a number from 1 to 20
rand = random.randint(a,b)

while(True):
    try:
        #Taking the guesswork out of the user
        number = input("Enter your number(Enter Exit to exit.):")
        
        #If Exit is entered, the program ends
        if number == "Exit" :
            break
        number = int(number)
        
        #Error message for a number that is not between 1 and 20
        if number > 20 or number <=0 :
            print("This data is not acceptable.")
        
        #If the number is between 1 and 20
        elif number <= 20 and number > 0 :
            #If it is true, the program ends
            if number == rand :
                print("Glory be to God! You guessed right!")
                break
            #Otherwise, the program will guide and ask questions again
            elif number < rand :
                print("go higher")
            elif number > rand :
                print("lower")
            else:
                print("This data is not acceptable.")
    except:
        print("This data is not acceptable.")