# -*- coding: utf-8 -*-

'''
+-----------------------------------------------------------------+
|        Small banking management system by alexcarchiar v 1.0    |
|        I already made one in the past in C that I can't find    |
|        I accidentaly deleted it                                 |
|        So I decided to create a new one in Python which         |
|        - I hope at least - is going to be easier and quicker    |
+-----------------------------------------------------------------+
'''

'''
Functions to add in the menu:
--- Create account
--- Delete account
--- Search account
--- Modify account
--- Withdraw
--- Deposit
--- All account holders
--- Close program
'''

import bank
import sort
import search

"""
Ale = bank.Account('current', 'EUR', 'Alessandro', 'Chiarelli', 'Via croce rossa 81', 'ID', 'AY56')
Ale.deposit(2, 'EUR')
Ale.show_info()
"""

Accounts = []


def show_menu():
    print("Welcome to bank management system by alexcarchiar")
    print("Version 1.0")
    flag = 1
    while (flag != 9):
        print("Available functions: press the right number key")
        print("1 - Create account")
        print("2- Delete account")
        print("3- Search account holder")
        print("4- Withdraw")
        print("5- Deposit")
        print("6- Modify account")
        print("7- Money transfer")
        print("8- Show all account holders")
        print("9- Close program")
        flag = int(input("Your choice: "))
        if flag == 1:
            print("Fill in the information")
            type = input("Account type: ")
            currency = input("Currency: ")
            name = input("Name: ")
            surname = input("Last name: ")
            address = input("Address: ")
            doc_type = input("Document type: ")
            doc_num = input("Document number: ")
            number = int(input("Account number: "))
            Accounts.append(bank.Account(type, currency, name, surname, address, doc_type, doc_num, number))
            sort.insertion_sort(Accounts)
        elif flag == 2:
            acc_number = int(input("Insert the account number: "))
            acc = search.search(Accounts, acc_number)
            if acc == -1:
                print("The account does not exist")
            else:
                Accounts[acc].show_info()
                print("Are you sure you want to delete this account? Press 1 to confirm, any other key to cancel")
                dele = int(input())
                if dele == 1:
                    del Accounts[acc]
                    print(bank.Account.Count)
                else:
                    print("Deletion cancelled")
        elif flag == 3:
            acc_number = int(input("Insert the account number: "))
            acc = search.search(Accounts, acc_number)
            if acc == None:
                print("The account does not exist")
            else:
                Accounts[acc].show_info()
        elif flag == 4:
            acc_number = int(input("Insert the account number: "))
            acc = search.search(Accounts, acc_number)
            if acc == -1:
                print("The account does not exist")
            else:
                print("Available balance: ", Accounts[acc].balance, " ", Accounts[acc].currency)
                amount = int(input("Amount to withdraw?"))
                Accounts[acc].withdraw(amount)
        elif flag == 5:
            acc_number = int(input("Insert the account number: "))
            acc = search.search(Accounts, acc_number)
            if acc == -1:
                print("The account does not exist")
            else:
                print("Available balance: ", Accounts[acc].balance, " ", Accounts[acc].currency)
                amount = int(input("Amount to deposit?"))
                curr = input("currency?")
                Accounts[acc].deposit(amount,curr)
        elif flag == 6:
            pass
            #I can add the options to modify the various parts of the account
            # informations but that is just a series of if-elif...-else
            # and inputs so I'm just too lazy to do it
        elif flag == 7:
            acc_number = int(input("Insert the sender's account number: "))
            acc1 = search.search(Accounts, acc_number)
            if acc1 == -1:
                print("The account does not exist")
            else:
                acc_number = int(input("Insert the receiver's account number: "))
                acc2 = search.search(Accounts, acc_number)
                if acc2 == -1:
                    print("The account does not exist")
                else:
                    amount = int(input("How much money from the sender's account?"))
                    bank.transfer(Accounts[acc1], Accounts[acc2],amount)
        elif flag == 8:
            print("Account number, name, surname")
            for i in range(0, len(Accounts)):
                print(Accounts[i].number," ",Accounts[i].owner.name, " ", Accounts[i].owner.surname)
        elif flag == 9:
            save_data()
            print("Bye Bye!")
        else:
            print("Wrong input. Please try again")


def get_data():
    fin = open("database.txt","r")
    database = fin.read()
    database = database.split(sep='\n')
    for i in range(0,len(database)-1):
        words = database[i].split(sep=' ')
        address = ''
        for j in range(bank.AccountInfo,len(words)):
            address += ' ' + words[j]
        Accounts.append(bank.Account(words[3], words[5], words[0], words[1], address, words[6], words[7], int(words[2])))
        Accounts[i].deposit(int(words[4]), words[5])
    fin.close()

def save_data():
    fout = open("database.txt", 'w')
    for i in range(0,len(Accounts)):
        line = Accounts[i].owner.name + ' ' + Accounts[i].owner.surname + ' ' + str(Accounts[i].number) + ' ' + Accounts[i].acc_type + ' ' + str(Accounts[i].balance) + ' ' + Accounts[i].currency + ' ' + Accounts[i].owner.doc_type + ' ' + Accounts[i].owner.doc_num + Accounts[i].owner.address + '\n'
        fout.write(line)
    fout.close()

get_data()
show_menu()
input("press any key to close")
exit()
