# -*- coding: utf-8 -*-

OwnerInfo = 5
AccountInfo = OwnerInfo + 3

class Owner:
    """
    Class used to describe owners of an account
    The fields are:
    name --> first name
    surname --> last name
    address --> the address of the owner's residence
    doc_type --> the type of document the owner gave - passport, id, driving licence, etc
    doc_num --> the alphanumeric string that uniquely identifies the owner's document
    """
    Clients_num = 0

    def __init__(self, name, surname, address, doc_type, doc_num):
        self.name = name
        self.surname = surname
        self.address = address
        self.doc_type = doc_type
        self.doc_num = doc_num
        Owner.Clients_num += 1

    def change_name(self, new_name):
        self.name = new_name

    def change_surname(self, new_surname):
        self.surname = new_surname

    def change_address(self, new_address):
        self.address = new_address

    def change_doc_type(self, new_doc_type):
        self.doc_type = new_doc_type

    def change_doc_num(self, new_doc_num):
        self.doc_num = new_doc_num

    def __del__(self):
        Owner.Clients_num -= 1

    def show_info(self):
        print("The owner of this account is:")
        print(self.name, ' ', self.surname)
        print('Address: ', self.address)
        print("Document: ", self.doc_type, " ", self.doc_num)

class Account:
    """
    Class used to deal with bank accounts. It contains all the information needed:
    --- Owner
    --- balance
    --- currency
    --- account type
    --- number (account number to uniquely identify an account)
    it also computes the new balance with the given exchange rate
    """
    Count = 0

    def __init__(self, acc_type, currency, name, surname, address, doc_type, doc_num, number):
        self.owner = Owner(name, surname, address, doc_type, doc_num)
        self.acc_type = acc_type
        self.currency = currency.upper()
        self.balance = 0
        self.number = number
        Account.Count += 1

    def show_info(self):
        print("Account number: ", self.number)
        self.owner.show_info()
        print("This is a ", self.acc_type, " account")
        print("Current balance: ", self.balance, self.currency)

    def change_acc_number(self, new_acc_number):
        self.number = new_acc_number

    def change_acc_type(self, new_acc_type):
        self.acc_type = new_acc_type

    def change_currency(self, new_currency, rate):
        """
        It changes currency with the given exchange rate
        :param new_currency: the new currency to be used
        :param rate: the exchange rate
        :return:
        """
        self.currency = new_currency.upper()
        self.balance *= rate

    def deposit(self, amount, currency):
        if self.currency == currency.upper():
            self.balance += amount
        else:
            print("The currency of the account is %s and the currency of the deposit is %s" % (self.currency, currency))
            rate = float(input("Give exchange rate: "))
            self.balance += amount * rate

    def withdraw(self, amount):
        """
        Used to make withdrawals.
        :param amount: it's the amount you want to withdraw. If it is bigger than the balance, cannot complete
        :return:
        """
        if (self.balance - amount) >= 0:
            self.balance -= amount
            print("Withdrawal completed")
        else:
            flag = 1
            while (self.balance - amount) < 0 and flag:
                print("The amount you required is too high. Do you want to try again?")
                flag = int(input("Press 1 for yes, 0 for no "))
                if flag:
                    amount = float(input("Insert the new amonut"))
                    if (self.balance - amount) >= 0:
                        self.balance -= amount
                        print("Withdrawal completed")

    def __del__(self):
        Account.Count -= 1

def transfer(sender: Account, receiver: Account, amount):
    if (sender.balance - amount) < 0:
        print("Sender's balance not enough")
    else:
        if sender.currency == receiver.currency:
            sender.balance -= amount
            receiver.balance += amount
            print("Transfer completed")
        else:
            print("The two accounts have different currencies. Give exchange rate from %s to %s" % (
                sender.currency, receiver.currency))
            rate = float(input())
            sender.balance -= amount
            receiver.balance += amount * rate
            print('Transfer completed')
