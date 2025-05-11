
from helper import *
y=0
while(y==0):
    op=menu()
    if(op==1):
        create_expense()
    if(op==2):
        display_expense()
    if(op==3):
        edit_expense()
    if(op==4):
        delete_expense()
    y=int(input("Do you want to continue?press 0 for Yes"))
    if(y!=0):
        save_data()
