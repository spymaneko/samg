user=str(input("enter your position: (teacher,cleaner or security) "))
if user=='teacher':
    print("welcome",user)
    a=str(input("enter your name:"))
    b=int(input("enter your age:"))
    c=str(input("enter your grade:"))
    if b>100:
        print("your old enough i don't know if your sure to teach")
    else:
        print("your welcome ",a)
    d=str(input("enter the module you can teach: python,cyber,cloud "))
    if d=='python':
        print("you are admitted to teach in kha")
        print("to verify your information insert this code on your phone : *182*8*1*1472583*500*your pin#")
    elif d=='cyber':
       print("you are admitted to teach in kha")
       print("to verify your information insert this code on your phone : *182*8*1*1472583*500*your pin#")
    elif d=='cloud':
        print("you are admitted to teach in kha")
        print("to verify your information insert this code on your phone : *182*8*1*1472583*500*your pin#")
    else:
        print("there is no place of your modue")
    z=int(input("enter your telephone number :"))
    print("thank you ",a," you will be mooping staff rooms and for update we will contact you on ",z)
elif user=='cleaner':
    print("your welcome",user)
    e=str(input("enter your name "))
    f=int(input("enter your age "))
    g=str(input("enter your grade"))
    if f>100:
        print("your old enough i don't know if your sure you can clean")
    elif g=='a' or 'b' or 'c' or 'd' or 'e':
         print(e," your welcome")
         print("you are admitted to teach in kha")
         print("to verify your information insert this code on your phone : *182*8*1*1472583*500*your pin#")
    else:
        print("your not allowed to work in kha")
    y=int(input("enter your telephone number :"))
    print("thank you ",e," you will be mooping staff rooms and for update we will contact you on ",y)
elif user=='security':
    print("welcome")
    i=str(input("enter your name "))
    j=int(input("enter your age "))
    k=str(input("enter your grade "))
    if k=='a' or 'b' or 'c' or 'd':
        print("welcome",i)
        print("you are admitted to teach in kha")
        print("to verify your information insert this code on your phone : *182*8*1*1472583*500*your pin#")
    else:
        print("your not allowed to secure kha")
    x=int(input("enter your telephone number :"))
    print("thank you ",i," you will be mooping staff rooms and for update we will contact you on ",x)
    
    
    
       
        
