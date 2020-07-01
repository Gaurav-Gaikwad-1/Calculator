from tkinter import *
from tkinter import messagebox


root=Tk()
root.geometry("270x420+300+300")                    #300+300 so that our app should appear in middle
root.resizable(0,0)                                 #resizable is disabled so that we cannot maximize window so that our buttons wont affect
root.title("CALCULATOR")

val=""                                             #for storing exp (globally declared)
A=0
operator=""

# function for numerical button clicked
def but1_pressed():
    global val                                        #TO TELL THAT VAL IS NOT A LOCAL BUT A GLOBAL VARIABLE
    val=val + "1"
    data.set(val)

def but2_pressed():
    global val
    val=val + "2"
    data.set(val)

def but3_pressed():
    global val
    val=val + "3"
    data.set(val)

def but4_pressed():
    global val
    val=val + "4"
    data.set(val)

def but5_pressed():
    global val
    val=val + "5"
    data.set(val)

def but6_pressed():
    global val
    val=val + "6"
    data.set(val)

def but7_pressed():
    global val
    val=val + "7"
    data.set(val)

def but8_pressed():
    global val
    val=val + "8"
    data.set(val)

def but9_pressed():
    global val
    val=val + "9"
    data.set(val)

def but0_pressed():
    global val
    val=val + "0"
    data.set(val)

# functions for the operator button click

def plus_clicked():
    global A
    global val,operator
    A=int(val)                #when we enter 14 and + sign for addition then it looks as(14+) 14 is stored in A         
    operator="+"              #setting operator with +
    val=val+"+"               #concatenating + with prev value so it looks like (14 +)
    data.set(val)

def minus_clicked():
    global A
    global val,operator
    A=int(val)                
    operator="-"              
    val=val+"-"               
    data.set(val)

def div_clicked():
    global A
    global val,operator
    A=int(val)                
    operator="/"              
    val=val+"/"               
    data.set(val)

def mul_clicked():
    global A
    global val,operator
    A=int(val)                
    operator="*"              
    val=val+"*"               
    data.set(val)

def C_clicked():
    global A
    global val,operator
    A=0
    val=""
    operator=""
    data.set(val)

def result():
    global A
    global val,operator
    val2=val
    if operator=="+":
        x=int((val2.split("+")[1]))     # if (12+5) then we r spliting 12 and 5 wrt + so we get 2 lists with index 0 & 1
        C=A+x                                # 0th index contains 12 which gets stored in A var so we take value at index 1 i.e 5
        data.set(C)
        val=str(C)
    elif operator=="-":
        x=int((val2.split("-")[1]))     
        C=A-x                                
        data.set(C)
        val=str(C)
    elif operator=="*":
        x=int((val2.split("*")[1]))     
        C=A*x                                
        data.set(C)
        val=str(C)
    elif operator=="/":
        x=int((val2.split("/")[1]))  
        if(x==0):  
            messagebox.showerror("Error,Division by zero not supported")
            A=""
            val=""
            data.set(val)
        else:
            C=int(A/x)                                
            data.set(C)
            val=str(C)

data=StringVar()

lbl=Label(root,
        text = "Label",
        anchor="se",
        bg="white",
        font=("Verdana,24"),
        textvariable=data,)              
lbl.pack(expand=True,fill="both",)

butrow1=Label(root)                                #butrow1,butrow2,butrow3,butrow4 divides the geometry into
butrow1.pack(expand=True,fill="both",)            # 4 labels(compartments) so that each label will contain
                                                   # 4 buttons
butrow2=Label(root)
butrow2.pack(expand=True,fill="both",)

butrow3=Label(root)
butrow3.pack(expand=True,fill="both",)            #expand is if there is space then expand and fill is set to both means
                                                   #expand in both x & y directions

butrow4=Label(root)
butrow4.pack(expand=True,fill="both",)

     #BUTTONS FOR FRAME1
but1=Button(butrow1,
            text="1",
            font=("Verdana,24"),
            relief="raised",
            border="0",
            command=but1_pressed,                             #border=0 so that all buttons appear in 1 line
           )
but1.pack(side="left",expand="true",fill="both",)

but2=Button(butrow1,
            text="2",
            font=("Verdana,24"),
            relief="raised",
            border="0",
            command=but2_pressed, 
            )
but2.pack(side="left",expand="true",fill="both",)

but3=Button(butrow1,
            text="3",
            font="Verdana,24",
            relief="raised",
            border="0",
            command=but3_pressed,
            )
but3.pack(side="left",expand="true",fill="both",)

butadd=Button(butrow1,
            text="+",
            font="Verdana,24",
            relief="raised",
            border="0",
            command=plus_clicked,
            )
butadd.pack(side="left",expand="true",fill="both",)

#BUTTONS FOR FRAME2

but4=Button(butrow2,
            text="4",
            font="Verdana,24",
            relief="raised",
            border="0",
            command=but4_pressed,
            )
but4.pack(side="left",expand="true",fill="both",)

but5=Button(butrow2,
            text="5",
            font="Verdana,24",
            relief="raised",
            border="0",
            command=but5_pressed, 
            )
but5.pack(side="left",expand="true",fill="both",)

but6=Button(butrow2,
            text="6",
            font="Verdana,24",
            relief="raised",
            border="0",
            command=but6_pressed, 
            )
but6.pack(side="left",expand="true",fill="both",)

butminus=Button(butrow2,
            text="-",
            font="Verdana,24",
            relief="raised",
            border="0",
            command=minus_clicked)
butminus.pack(side="left",expand="true",fill="both",)

 #BUTTONS FOR FRAME3
but7=Button(butrow3,
            text="7",
            font="Verdana,24",
            relief="raised",
            border="0",
            command=but7_pressed, 
            )
but7.pack(side="left",expand="true",fill="both",)

but8=Button(butrow3,
            text="8",
            font="Verdana,24",
            relief="raised",
            border="0",
            command=but8_pressed, 
            )
but8.pack(side="left",expand="true",fill="both",)

but9=Button(butrow3,
            text="9",
            font="Verdana,24",
            relief="raised",
            border="0",
            command=but9_pressed, 
            )
but9.pack(side="left",expand="true",fill="both",)

butmul=Button(butrow3,
            text="*",
            font="Verdana,24",
            relief="raised",
            border="0",
            command=mul_clicked)
butmul.pack(side="left",expand="true",fill="both",)

#BUTTONS FOR FRAME4
butC=Button(butrow4,
            text="C",
            font="Verdana,24",
            relief="raised",
            border="0",
            command=C_clicked)
butC.pack(side="left",expand="true",fill="both",)

but0=Button(butrow4,
            text="0",
            font="Verdana,24",
            relief="raised",
            border="0",
            command=but0_pressed ,
            )
but0.pack(side="left",expand="true",fill="both",)

buteq=Button(butrow4,
            text="=",
            font="Verdana,24",
            relief="raised",
            border="0",
            command=result,)
buteq.pack(side="left",expand="true",fill="both",)

butdiv=Button(butrow4,
            text="/",
            font="Verdana,24",
            relief="raised",
            border="0",
            command=div_clicked)
butdiv.pack(side="left",expand="true",fill="both",)
root.mainloop()

