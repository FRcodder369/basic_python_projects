import os

def renaming():
    address = input('please enter address of the file: ')
    address = address.replace('\\','/')
    address.rstrip('\\')
    address += '/'


    general_name = input('please enter general name: ')
    extension = input('please enter extension name: ').lstrip('.')

    i = 0
    for filename in os.listdir(address):
        old_path = address + filename
        new_path = address + general_name + str(i) + '.' + extension
        os.rename(old_path, new_path)
        i += 1

renaming()