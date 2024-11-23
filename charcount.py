print(" \t\t\tCOUNTING OF CHARACTERS IN A GIVEN STRING")
ch='y'
while(ch=='y'):
    a=input("Enter any String (Example: Welcome to CSC) :")
    print("Number of Characters (with Space) :",len(a))
    ch=input("Do you want to run the program again(y/n):")
    if(ch=='y'):
        pass
    elif(ch=='n'):
        print("\t\t\t\tProgram ended")
        print("\t\t\t\t===========")
        exit()

