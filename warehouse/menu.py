
import os
clear = lambda: os.system('clear') 

def print_menu():
    print("-" *30)
    print('warehouse control system')
    print("-" *30)
    print('[1] Register new items')
    print('[2] List items')
    print('[3] Update stock')
    print('[4] Value of inventory items')
    print('[5] Remove item')
    print('[6] Sale transction')
    print('[x] Close')

def print_header(title):
    clear()
    print('-' *75)
    print(' ' +title )
    print('-' *75)