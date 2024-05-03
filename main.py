class user:
    def __init__(self,name,email,address,typez):
        self.name=name
        self.email=email
        self.address=address
        self.tpe=typez
        self.balance=0
        self.history={}
        self.loan_tken=0
        self.loan_bl=0
        self.account_no=0
    def check_balance(self):
        print(f'Your available Balance:{self.balance}')
        
    def check_transaction_history(self):
        for i in self.history:
            if i=='Deposit':
                print("-----Deposit-----")
                for j in range(len(self.history[i])):
                    print(f"Deposited - {self.history[i][j]}")
            elif i== "Loan":
                print("-----Loan Taken-----")
                for j in range(len(self.history[i])):
                    print(f'Loan - {self.history[i][j]}')
            elif i=="Withdrawal":
                print("-----Withdrawal-----")
                for j in range(len(self.history[i])):
                    print(f'Withdrawn - {self.history[i][j]}')
            elif i== "Transferred":
                print("-----Transferred-----")
                for j in range(len(self.history[i])):
                    print(f'Loan Taken - {self.history[i][j]}')
            elif i=="Recv":
                print("-----Received-----")
                for j in range(len(self.history[i])):
                    print(f"Received Money - {self.history[i][j]}")
                    
    def take_loan(self,amount,bnk):
        if bnk.bankrupt==False and bnk.loan==True and self.loan_tken<=1:
            print("Loan Taken Successfully")
            self.loan_tken+=1
            self.balance+=amount
            self.loan_bl+=amount
            if "Loan" in self.history:
                self.history["Loan"].append(amount)
            else:
                self.history["Loan"]=[amount]
        else:
            if bnk.bankrupt==True:
                print("Bank is bankrupted. You can't take the loan.")
            elif bnk.loan==False:
                print("Bank doesn;t currently give you loan")
            else:
                print("The limit for your loan has exceeded.")
    def deposit(self,amount,bnk):
        if bnk.bankrupt==False:
            if "Deposit" in self.history:
                self.history["Deposit"].append(amount)
                self.balance+=amount
            else:
                self.history["Deposit"]=[amount]
                self.balance+=amount
        else:
            print("Sorry! Can't deposit money. The bank has got banrupted.")
        
    def withdraw(self,amount,bnk):
        if bnk.bankrupt==False:
            if self.balance>=amount:
                self.balance-=amount
                print(f"{amount} has been deducted from your bank account.")
                if "Withdrawal" in self.history:
                    self.history["Withdrawal"].append(amount)
                else:
                    self.history["Withdrawal"]=[amount]
            else:
                print("You don't have sufficient Balance.")
        else:
            print("The bank got bankrupted.")
    def transfer(self,acc_no,amount,bnk):
        if bnk.bankrupt==False:
            if acc_no in bnk.accounts:
                if self.balance>=amount:
                    print(f"The {amount} has been transferred.")
                    self.balance-=amount
                    bnk.accounts[acc_no].balance+=amount
                    if "Transferred" in self.history:
                        self.history["Transferred"].append(amount)
                    else:
                        self.history["Transferred"]=[amount]
                    if "Recv" in bnk.accounts[acc_no].history:
                        bnk.accounts[acc_no].history["Recv"].append(amount)
                    else:
                        bnk.accounts[acc_no].history["Recv"]=[amount]
                else:
                    print("You don't have sufficient Balance.")
            else:
                print("The account number is not of this bank.")
        else:
            print("The bank is bankrupted.")
            
            
            
class Admin:
    def __init__ (self,id,password):
        self.id=id
        self.password=password
        
    def delete_account(self,account_id,bnk):
        if account_id in bnk.accounts:
            del bnk.accounts[account_id]
            print("ID removed")
        else:
            print("Account not found")
    
    def user_accounts(self,bnk):
        bnk.showusers()
        
    def bank_balance(self,bnk):
        sm=0
        for i in bnk.accounts:
            sm+=bnk.accounts[i].balance
        print(f"The current balance of bank is: {sm}")
        
    def loan_amount(self,bnk):
        sm=0
        for i in bnk.accounts:
            sm+=bnk.accounts[i].loan_bl
        print(f"The current amount of loan given is: {sm}")
        
    def loan_feature(self,bnk):
        if bnk.loan==True:
            bnk.loan=False
            print("The loan giving feature is turned off.")
        else:
            bnk.loan=True
            print("The loan giving feature is turned on.")
    def bankruptcy(self,bnk):
        if bnk.bankrupt==False:
            bnk.bankrupt=True
            print("The bank has been declared bankrupt.")
        
        else:
            bnk.bankrupt=False
            print("The bank has been freed from bankrupt.")
    
    
class Bank:
    
    def __init__(self,name):
        self.name=name
        self.acc_no=1
        self.accounts={}
        self.loan=True
        self.bankrupt=False
    def add_user(self,usr):
        usr.account_no=self.acc_no
        self.acc_no+=1
        self.accounts[usr.account_no]=usr
        
        
    def showusers(self):
        print(f"The clients of {self.name}: ")
        for i in self.accounts:
            print(f'Name: {self.accounts[i].name} Account Number: {self.accounts[i].account_no} Account Type: {self.accounts[i].tpe} Account Balance: {self.accounts[i].balance}')
            

naam=Bank("Thread Corps")
admin=Admin('admin',1234)
def callout():
    while True:
        print(f"Welcome to {naam.name} Banks ")
        
        print('''1.Admin
2.Client
3.Exit''')
        entry=int(input("Enter your selection:"))
        if entry==1:
            nm=input("Enter username: ")
            pass_key=int(input("Enter a password: "))
            if nm==admin.id and pass_key==admin.password:
                while True:
                    print('''1.Create An Account
2.Delete Account
3.User info
4.Balance of Bank
5.Total Loan
6.Loan giving:
7. Declare bankruptcy
Press any key to exit''')
                    usr_entry=int(input("Enter your selection:"))
                    if usr_entry==1:
                        name=input("Enter your name: ")
                        email=input("Enter your email address: ")
                        address=input("Enter your address: ")
                        account_type=input("Enter your account type: ")
                        z=user(name,email,address,account_type)
                        naam.add_user(z)
                        print("You have successfully created your account.")
                        print(f'Your account id is: {z.account_no}')
                    elif usr_entry ==2:
                        acc_no=int(input("Enter the account no: "))
                        admin.delete_account(acc_no,naam)
                    elif usr_entry ==3:
                        admin.user_accounts(naam)
                    elif usr_entry ==4:
                        admin.bank_balance(naam)
                    elif usr_entry == 5:
                        admin.loan_amount(naam)
                    elif usr_entry ==6:
                        admin.loan_feature(naam)
                    elif usr_entry==7:
                        admin.bankruptcy(naam)
                    else:
                        break
        elif entry==2:
            while True:
                print('''1. Create a new account:
2.Show Available Balance
3.Transaction History
4.Transfer 
5.Withdraw
6.Deposit
7.Loan
8.Exit''')
                usr_entry=int(input("Enter your selection:"))
                if usr_entry==1:
                    name=input("Enter your name: ")
                    email=input("Enter your email address: ")
                    address=input("Enter your address: ")
                    account_type=input("Enter your account type: ")
                    z=user(name,email,address,account_type)
                    naam.add_user(z)
                    print("You have successfully created your account.")
                    print(f'Your account id is: {z.account_no}')
                
                elif usr_entry==2:
                    acc=int(input("Your account number:"))
                    if acc in naam.accounts:
                        naam.accounts[acc].check_balance()
                    else:
                        print("Sorry the account is not in our Bank.")
                
                elif usr_entry==3:
                    acc=int(input("Enter your account number: "))
                    if acc in naam.accounts:
                        naam.accounts[acc].check_transaction_history()
                
                elif usr_entry==4:
                    sender=int(input("Type in your account number: "))
                    receiver=int(input("Type in the receivers account number:"))
                    amount=int(input("Enter the amount required: "))
                    if sender in naam.accounts:
                        naam.accounts[sender].transfer(receiver,amount,naam)
                    else:
                        print("The above account was not found.")
                elif usr_entry==5:
                    acc=int(input("Enter your account no: "))
                    amount=int(input("Enter the amount you want to withdraw: "))
                    if acc in naam.accounts:
                        naam.accounts[acc].withdraw(amount,naam)
                    else:
                        print("Account not found")
                elif usr_entry==6:
                    acc=int(input("Enter your account no: "))
                    amount=int(input("Enter the amount you want to deposit: "))
                    if acc in naam.accounts:
                        naam.accounts[acc].deposit(amount,naam)
                    else:
                        print("Account not found")
                elif usr_entry==7:
                    acc_no=int(input("Enter the account number: "))
                    amount=int(input("Enter the amount: "))
                    if acc_no in naam.accounts:
                        naam.accounts[acc_no].take_loan(amount,naam)
                    else:
                        print("Account not found")
                else: break
        elif entry==3:
            
            break
        else:
            print("Wrong entry. Please try again")
        
        
        
        
        
callout()