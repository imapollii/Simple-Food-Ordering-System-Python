import os
import time


os.system('CLS')

# Greettings!
print("Hey there! Welcome to Poli's Milktea Shop")


# Define Menu and price list
MilkTea = ["Classic","Taco","Matcha","Strawberry","Chocolate","Cookies and Cream","Cappuccino"]
MilkTeaPrice = [120.0,110.0,130.0,100.0,130.0,120.0,150.0]
Quantity = 0
Sub_Total = 0




while(True):
    # Menu Option
    print("----------------------------------------------------\n")
    print("- 0. ",MilkTea[0]," --------------------------- ",MilkTeaPrice[0]," -")
    print("- 1. ",MilkTea[1]," ------------------------------ ",MilkTeaPrice[1]," -")
    print("- 2. ",MilkTea[2]," ---------------------------- ",MilkTeaPrice[2]," -")
    print("- 3. ",MilkTea[3]," ------------------------ ",MilkTeaPrice[3]," -")
    print("- 4. ",MilkTea[4]," ------------------------- ",MilkTeaPrice[4]," -")
    print("- 5. ",MilkTea[5]," ----------------- ",MilkTeaPrice[5]," -")
    print("- 6. ",MilkTea[6]," ------------------------ ",MilkTeaPrice[6]," -")
    print("\n----------------------------------------------------\n")
    
    print("Choose a number you prefer : ",end="")
    choose = int(input())
    
    if(choose == 0):
        print(MilkTea[0])
    elif(choose == 1):
        print(MilkTea[1])
    elif(choose == 2):
        print(MilkTea[2])
    elif(choose == 3):
        print(MilkTea[3])
    elif(choose == 4):
        print(MilkTea[4])
    elif(choose == 5):
        print(MilkTea[5])
    elif(choose == 6):
        print(MilkTea[6])
        
    
    # Ask user to input the quantity
    print("Quantity : ",end="")
    Quantity = int(input())
    
    # Compute the sub total and print the receipt
    Sub_Total = MilkTeaPrice[int(choose)] * Quantity
    print("Sub Total : ",Sub_Total)
    print("\n----------------------------------------------------\n")
    time.sleep(1)
    print("3s ",end="")
    time.sleep(1)
    print("2s ",end="")
    time.sleep(1)
    print("1s ",end="")
    time.sleep(1)
    
    
    os.system('CLS')
    
    
    
    print("Printing Receipt",end="")
    time.sleep(1)
    print(" . ",end="")
    time.sleep(1)
    print(" . ",end="")
    time.sleep(1)
    print(" . ")
        
    print("\n----------------------------------------------------\n")
    
    print("Purchased : ", MilkTea[int(choose)],Quantity,"x ----- ",Sub_Total)
    
    print("\n----------------------------------------------------\n")
    
    
    print("To order again [y] and [n] to quit",end="")
    choose1 = input()
    
    if(choose1 == "y"):
        os.system('CLS')
        continue
    elif(choose1 == "n"):
        os.system('CLS')
        break
        
    
    



