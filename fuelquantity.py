print(" \t\t\tFUEL QUANTITY CALCULATOR")

ch='y'
while(ch=='y'):
     fuel_name=str(input("Enter the type of fuel(Petrol / Diesel)(P/D):"))
     fuel_price=int(input("Enter the amount of the Fuel between Rs.(50-10000):"))
     def fuel(fuel_price):
          if (fuel_name=='p'or fuel_name=='P'):
               c=fuel_price/75
          elif(fuel_name=='d' or fuel_name=='D'):
               c=fuel_price/70
          return c
     if (fuel_name=='p' or fuel_name=='P'):
          print("Quantity of  Petrol for Rs.%0.2f"%fuel_price,"is %0.2f"%fuel(fuel_price),"litres")
     elif(fuel_name=='d'or fuel_name=='D'):
          print("Quantity of  Petrol for Rs.%0.2f"%fuel_price,"is %0.2f"%fuel(fuel_price),"litres")
     ch=input("Do you want to run the program again(y/n):")
     if(ch=='y'):
          pass
     elif(ch=='n'):
          print("\t\t\t\tProgram ended")
          print("\t\t\t\t===========")
          exit()

