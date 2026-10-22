expanse_dict = {
    "name" : [],
    "catagary" : [],
    "amount" : []
}


def add_expanse() :
    def append_to_dict() :
        expanse_dict["amount"].append(expanse_amount) 
        expanse_dict["name"].append(expanse_name)
        expanse_dict["catagary"].append(expanse_catagary.upper().strip())
   
   
    expanse_name = input("\nEnter expanse name :")
    expanse_catagary = input("Enter the expanse catagary:")

    try :
        expanse_amount = float(input("Enter the amount:"))
    
        if expanse_amount <= 0 :
            print("\nPlease enter the values greater than zero in the amount section !")  
        elif expanse_name.strip() == "" :
            print("\nplease enter the expanse name dont leave it empty !")
        elif expanse_catagary.strip() == "" :
            print("\nplease enter the expanse catagary dont leave it empty")
        else :
            append_to_dict()
            print("\nExpanse added sucssfully!\n")
               
    except ValueError :
        print("\nEnter only numbers in the amount section !")  

    
def view_expanse() :
    if expanse_dict["name"] == [] :
         print("\nno xepanse has been recoreded yet !!")
    else :
        print("\n===== ALL EXPENSES =====")
        for i in range(len(expanse_dict["amount"])) :
            print("\nname :",expanse_dict["name"][i])
            print("catagary :",expanse_dict["catagary"][i])
            print("amount :",expanse_dict["amount"][i])

def total_expanse() :
    if expanse_dict["amount"] == [] :
        print("No expanse has been recoreded yet !")
    else :
        print("\n===== TOTAL EXPENSES =====")
        total = 0
        for i in range(len(expanse_dict["amount"])) :
            total += expanse_dict["amount"][i]
        print("\nTotal expanse :",total)    

def expanse_by_catagary() :
    catagary = input("\nEnter the catagary :")
    total_catagary_expanse = 0
    
    
    if expanse_dict["catagary"] == [] :
        print("There is no expanse has been recorded yet !")
    elif catagary.strip() == "" :
        print("please enter the catagary to search")
    elif catagary.upper().strip() not in expanse_dict["catagary"]  :
                print("there is no such a catagary in your expanse record !!")
    else :
        print(f"\n===== {catagary.upper()} EXPENSES =====")
        for i in range(len(expanse_dict["catagary"])) :
            if catagary.upper().strip() == expanse_dict["catagary"][i] :
                print(expanse_dict["name"][i]," : ",expanse_dict["amount"][i])
                total_catagary_expanse += expanse_dict["amount"][i]
        print(f"\nTotal {catagary.upper()} Expanse :{total_catagary_expanse}")

while True :
    print("\n=======Expanse Tracker======== \n")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Calculate Total Expenses")
    print("4. View Expenses by Category")
    print("5. Exit \n")

    try :
        choice = int(input("Enter your choice :"))
    except ValueError :
        print("Please enter only numbers !!")
        continue
         
    if choice == 1 :
        add_expanse()
    elif choice == 2 :
        view_expanse()
    elif choice == 3 :
        total_expanse()
    elif choice == 4 :
        expanse_by_catagary()
    elif choice == 5 :
        print("Thank you for using Expense Tracker!")
        break
    else :
        print("Invalid Choice Yoo!!")
    