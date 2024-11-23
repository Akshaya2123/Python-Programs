print("\t\t\t\tSORTING OF NUMBERS")
ch='y'
while(ch=='y'):
    a=[]
    b=int(input("Enter the total number of elements inside the list:"))
    for i in range(1,b+1):
        value=int(input("Enter number %d:" %i))
        a.append(value)
    c=input("Enter type of sorting(a/d):")
    if(c=='a'):
        for i in range(b):
            for j in range(i+1,b):
                if(a[i]>a[j]):
                    temp=a[i]
                    a[i]=a[j]
                    a[j]=temp
        t=input("Do you want to write the output to a text file:")
        if(t=='y'):
            e=str(a[i])
            file=open("sort6.txt","w")
            file.write("Elements sorted in desending order:")
            for i in range(0,b):
                file.write(e)
            file.close()
        elif(t=='n'):
            print("Elements sorted in ascending  order")
            for i in range(0,b):
                print(a[i])
    elif(c=='d'):
        for i in range(b):
            for j in range(i+1,b):
                if(a[i]<a[j]):
                    temp=a[i]
                    a[i]=a[j]
                    a[j]=temp
        t=input("Do you want to write the output to a text file")
        if(t=='y'):
            e=str(a[i])
            file=open("sort6.txt","w")
            file.write("Elements sorted in desending order:")
            for i in range(0,b):
                file.write(e)
            file.close()
        elif(t=='n'):
            print("Elements sorted in desending  order")
            for i in range(0,b):
                print(a[i])
               
    ch=input("Do you want to run the program again(y/n):")
    if(ch=='y'):
        pass
    elif(ch=='n'):
        print("\t\t\tProgram ended")
        print("\t\t\t==========")
        exit()

