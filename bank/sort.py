# -*- coding: utf-8 -*-
'''
Insertion sort
Justification: the accounts are inserted one by one -
hence comes natural to choose an insertion sort
Furthermore, when importing a database we already have
a sorted list of accounts

Credits: adjusted from https://www.programminginpython.com/insertion-sort-algorithm-python/
'''
import bank

def insertion_sort(sort_list):
    for i in range(1, len(sort_list)):
        key = sort_list[i]
        j = i - 1
        while j >= 0 and key.number < sort_list[j].number:
            sort_list[j + 1] = sort_list[j]
            j -= 1
        sort_list[j + 1] = key
