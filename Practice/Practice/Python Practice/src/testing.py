import os
from time import sleep

class FileManip():
    
    
    
    def __init__(self):
        self.forbidden_dir = ['windows32', 'Documents', 'Desktop']
        self.name = 'user session'
        
        
    def creator(self):
        f = open(input('enter filename: '), 'w')
        f.write("this is {0} \n".format(self.name))
        f.close()
        
    def writer(self):
        f = open(input('enter filename: '), 'a')
        text_to_add = input("enter what you want to say:")
        
        f.write(f'{text_to_add} \n')
        f.close()
        
    def reader(self):
        f = open(input('enter filename: '), 'r')
        l = f.read()
        print(l)
        f.close()
        
    def deleter(self):
        if input('enter filename: ') in self.forbidden_dir:
            return('nope')
        else:
            os.remove(self.name)
        
    
#without the txt extension this will create a generic file.. who wouldve thought!
counter = 5           
starter = input('continue y/n: \n')
if starter == 'y':
    print("***WARNING DO NOT USE SYSTEM FILE NAMES WITH DELETER IT WILL REMOVE THEM ***")
    while counter != 0:
        print('.', end='')
        sleep(1)
        counter -= 1
    
    us = FileManip()
else:
    print('see you next time!')





    
