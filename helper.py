
from tabulate import tabulate
expenses=[]
def menu():
    print("Expense Manager")
    print("1->Create New Expense")
    print("2->Display Expense")
    print("3->Edit Expense")
    print("4->Delete Expense")
    opt=int(input("Enter Your Choice"))
    return opt
def create_expense():
    expense_title=input("Enter expense_title")
    amount=input("Enter Amount")
    date=input("Enter date")
    #print(expense_title+" "+amount+" "+date)
    expenses.append((expense_title,amount,date))
def display_expense():
    #print(expenses)
    table1=[]
    for item in expenses:
        #print(item[0]+" "+item[1]+" "+item[2])
        table1.append([item[0],item[1],item[2]])
    print(tabulate(table1, headers=['expense_title', 'Amount','Date']))
def edit_expense():
    display_expense()
    i=int(input("Enter the record index you want to Edit "))  
    expense_title=input("Enter New expense_title")
    amount=input("Enter New Amount")
    date=input("Enter New date")
    expenses[i]=(expense_title,amount,date)
    display_expense()

def delete_expense():
    display_expense()
    i=int(input("Enter the record index you want to delete "))
    del expenses[i]
    display_expense()
def save_data():
    fp=open("data.txt","a")
    for item in expenses:
        data=item[0]+"-"+item[1]+"-"+item[2]+"\n"
        fp.write(data)
    fp.close()


