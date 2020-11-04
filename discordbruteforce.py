import socket
import ssl 
import itertools
import socket_method 
from sys import argv

from selenium import webdriver


def main():
    script, method = argv
    if(method=='socket_method'):
        socket_method.run()
    elif(method=='selenium_method'):
        selenium_method()
    else:
        print('Niepoprawna nazwa methody')
        exit()




main()
