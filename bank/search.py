# -*- coding: utf-8 -*-

'''
Search algorithms for my bank management system
The key is the account number
I do a binary search
'''
import bank
from math import floor


def search(list, acc_number):
    low = 0
    high = len(list)-1
    while low<=high:
        mid = floor((low+high)/2)
        if acc_number == list[mid].number:
            return mid
        elif acc_number < list[mid].number:
            high = mid - 1
        else:
            low = mid + 1
    return -1

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
