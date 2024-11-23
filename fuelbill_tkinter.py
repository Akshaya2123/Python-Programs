from tkinter import*
from tkinter import messagebox
import atexit
bot=Tk()
bot.title("Eb bill")
bot.geometry("500x500")
label=Label(bot,text=" ",fg="black",font=("Times New Roman",16,"bold")).grid(row=500,column=400)
label1=Label(bot,text=" ",fg="black",font=("Times New Roman",16,"bold")).grid(row=700,column=400)
label2=Label(bot,text="\t\t\t\t\tEB BILLING \n\t\t\t\t\t===========\n\t\t\t\t\tDone by:Akshayasree.S/26931/Archana" ,fg="black",font=("Times New Roman",15, "bold")).grid(row=10,column=1)
label3=Label(bot,text="1.Enter Consumer Service Number:",fg="black",font=("Times New Roman",15)).grid(row=50,column=1)
label33=Label(bot,text=" ",fg="black",font=("Times New Roman",15)).grid(row=40,column=7)
label4=Label(bot,text="2.Enter Previous Meter Readings(PMR): ",fg="black",font=("Times New Roman", 15)).grid(row=70,column=1)
label44=Label(bot,text=" ",fg="black",font=("Times New Roman",15)).grid(row=110,column=7)
label5=Label(bot,text="3.Enter Current Meter Readings(CMR): ",fg="black", font=("Times New Roman",15)).grid(row=90,column=1)
label55=Label(bot,text=" ",fg="black", font=("Times New Roman", 15)).grid(row=190,column=7)
entry1=Entry(bot,bd=7,font=('Calibri',10))
entry2=Entry(bot,bd=7,font=('Calibri',10))
entry3=Entry(bot,bd=7,font=('Calibri',10))
entry1.grid(row=50,column=2)
entry2.grid(row=70,column=2)
entry3.grid(row=90,column=2)
con=""
pmr=""
units=" "
cmr=""
price=""
d=""
t=""
a=""
bill=1
def meterreading():
  global con
  while True:
    con=entry1.get()
    if(con.isdigit()):
      if(len(con)==11):
        if((int(con[0])==0 and int(con[1])==1) or (int(con[0])==1 and int(con[1])==1) or (int(con[0])==2 and int(con[1])==1)):
          if(int(con[2])==0 and int(con[3])==6 and (int(con[4])==1 or int(con[4])==2 or int(con[4])==3 or int(con[4])==4 or int(con[4])==5)):
            if(int(con[5])==0 and (int(con[6])>=0 and int(con[6])<=5) and (int(con[7])>=1 and int(con[7])<=9)):
              if((int(con[8])>=0 and int(con[8])<=9)and (int(con[9])>=0 and int(con[9])<=9) and (int(con[10])>=1 and int(con[10])<=9)):
                global bill
                bill=1
                break
              else:
                messagebox.showerror("Error","The value entered must be only integer")
                break
            else:
              messagebox.showerror("Error","The value entered must be only 11 digits or it shouldnt be a null")
              break
          else:
            messagebox.showerror("Error","The value of first two digits must be 01/11/21")
            break
        else:
          messagebox.showerror("Error","The value after the first two digits must be 061/062/063/064/065")
          break
      else:
        messagebox.showerror("Error","The value of the middle three numbers must be from 001 to 050")
        break
    else:
      messagebox.showerror("Error","The value of the last three digits must be from 001 to 999")
      break
button1=Button(bot,text="OK",padx=20,pady=7,font=("Georgia",8),activebackground="blue",command=meterreading).grid(row=50,column=3) 
def meter():
  global pmr
  while True:
    pmr=entry2.get()
    if(pmr.isdigit()):
      if(len(pmr)==5):
        pass
        break
      else:
        messagebox.showerror("error","pmr must be a 5 digit number")
        break
    else:
        messagebox.showerror("error","the value of pmr must be only an integer")
        break 
button2=Button(bot,text="OK",padx=20,pady=7,font=("Georgia",8),activebackground="blue",command=meter).grid(row=70,column=3)         
def bill():
  global cmr
  while True:
    cmr=entry3.get()
    if(cmr.isdigit()):
      if(len(cmr)==5):
        if(int(cmr)>int(pmr)):
          pass
          break
        else:
          messagebox.showerror("error","cmr must be greater than pmr")
          break
      else:
        messagebox.showerror("error","cmr must be a 5 digit number")
        break
    else:
      messagebox.showerror("error","the value of cmr must be only an integer")
      break

button3=Button(bot,text="OK",padx=20,pady=7,font=("Georgia",8),activebackground="blue",command=bill).grid(row=90,column=3)    
def billing():
    global units
    global price
    global d
    global t
    global a
    global pmr
    global cmr
    units=int(cmr)-int(pmr)
    if(units==100):
      price=0
      d=0
      t=d+price
    elif(units>=101 and units<=250):
      price=units*2.6
      d=0
      t=d+price
    elif (units>=251 and units<=400):
      price=units*3.5
      d=0
      t=d+price
    elif (units>=401 and units<=600):
      price=units*4.8
      d=0
      t=d+price
    elif (units< 600):
      price=units*5
      d=price*0.2
      t=d+price
    return units
    return price
    return d
    return t
def ending():
  global label6
  global label7
  global label8
  global label9
  global label10
  global label11
  global label12
  global label13
  global label14
  global label15
  global label16
  global label17
  global frame1
  global units
  global d
  global t
  global price
  frame1=Frame(bot,bd=12,width=600,height=500,bg="White",padx=80,pady=80,relief=RIDGE)
  frame1.grid(row=120,column=1)
  label6=Label(frame1,text="Output ",fg="cadet blue",bg="white",font=("calibri",15,"bold"))
  label6.grid(row=120,column=1)
  label7=Label(frame1,text="Tamilnadu Electricity Board",fg="black",bg="white",font=("georgia",12))
  label7.grid(row=125,column=1)
  label8=Label(frame1,text="Sembium,Perambur,Chennai-600011",fg="black",bg="white",font=("georgia",12))
  label8.grid(row=128,column=1)
  label9=Label(frame1,text="\nConsumer Service No.           :"+str(con),fg="black",bg="white",font=("georgia",12))
  label9.grid(row=135,column=1)
  label10=Label(frame1,text=" Previous Meter Reading (PMR)    :"+str(pmr),fg="black",bg="white",font=("georgia",12))
  label10.grid(row=140,column=1)
  label11=Label(frame1,text=" Current Meter Reading (CMR)     :"+str(cmr),fg="black",bg="white",font=("georgia",12))
  label11.grid(row=150,column=1)
  label12=Label(frame1,text=" No.of units consumed            :  "+str(units)+" Units",fg="black",bg="white",font=("georgia",12))
  label12.grid(row=155,column=1)
  label13=Label(frame1,text=" Current consumption charges(CCC):Rs."+str(price),fg="black",bg="white",font=("georgia",12))
  label13.grid(row=160,column=1)
  label14=Label(frame1,text=" Deposite Charges(DC)            :Rs."+str(d),fg="black",bg="white",font=("georgia",12))
  label14.grid(row=165,column=1)
  label16=Label(frame1,text=" ===========================",fg="black",bg="white",font=("georgia",12))
  label16.grid(row=170,column=1)
  label15=Label(frame1,text=" Total eb bill payable          :Rs."+str(t),fg="black",bg="white",font=("georgia",12))
  label15.grid(row=175,column=1)
  label17=Label(frame1,text=" ============================",fg="black",bg="white",font=("georgia",12))
  label17.grid(row=180,colum=1)
def delete():
    entry1.delete(0,'end')
    entry2.delete(0,'end')
    entry3.delete(0,'end')
    frame1.destroy()
    label6.destroy()
    label7.destroy()
    label8.destroy()
    label9.destroy()
    label10.destroy()
    label11.destroy()
    label12.destroy()
    label13.destroy()
    label14.destroy()
    label15.destroy()
    label16.destroy()
    label17.destroy()
    global bill
    bill=1
    return
button4=Button(bot,text="Show",padx=20,pady=7,font=("Georgia",8),activebackground="blue",command=lambda:[billing(),ending(),meter(),meterreading]).grid(row=100,column=2)
button6=Button(bot,text="Clear",padx=20,pady=7,font=("Georgia",8),activebackground="blue",command=delete).grid(row=100,column=3)
def exitbill():
  again=messagebox.askquestion("exit","Do you want to exit the program?")
  if (again=="yes"):
    bot.destroy()
  else:
    return None    
atexit.register(exitbill)
button5=Button(bot,text="Exit",padx=20,pady=7,font=("Georgia",8),activebackground="red",command=exitbill).grid(row=100,column=4)
bot.mainloop()
