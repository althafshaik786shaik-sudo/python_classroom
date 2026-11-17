#for x in "123456":
   # print(x)
    
    
#for x in range(5,0,-1):
 #     print(x)    

  
      
      
# ATM machine problem      
current_password = "admin123"

for attempt in range(1, 4):
    password = input("Enter your password: ")

    if password == current_password:
        print("Login successfully")
        break

    else:
        print("Wrong password!")

        if attempt == 3:
            print("Account locked")  
 
 
# for loop concept            
total=0
for n in range (1,6):
   total +=n
print("sum:",total)          
            