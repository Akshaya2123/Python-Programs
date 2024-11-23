print("\t\t\tPROGRAM TO GET A STRING AND INTEGER AND PERFORM THE GIVEN FUNCTIONS")
ch='y'
while(ch=='y'or ch=='Y'):
    a=input("1.Enter a number:")
    b=input("2.Enter a statement:")
    print("Number of digits in",a,"are",len(a))
    c=input("Enter the digit:")
    print("The Digit ",c,"occurs",a.count(c),"times in",a)
    d=int(input("Enter the power:"))
    a1=int(a)

    s1=a1**d
    print(a,"power of",d,"is",s1)    
    v=0
    con=0
    spl=0
    for i in range(0,len(b)):
        if(b[i]=='a' or b[i]=='e'or b[i]=='i' or b[i]=='o' or b[i]=='u'):
            v=v+1
        elif not(b[i].isalpha()):
            spl=spl+1
        else:
            con=len(b)-v
    print("The Number of Vowel:",v)
    print("The Number of Consonants:",con)
    print("The Number of Special character:",spl)

    ch=input("Do you want to run again:")
    if(ch=='y'or ch=='Y'):
        pass
    elif(ch=='n'or ch=='N'):
        print("\t\t\t\tPROGRAM ENDED")
        print("\t\t\t\t=============")
        exit()
    else:
        print("invalid input")
        ch=input("Do you want to run again")

