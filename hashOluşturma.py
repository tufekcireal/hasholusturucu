#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import hashlib
from termcolor import colored
karakterGirin = input("String Girin: ")
##MD5
print(colored("    <<<<<<<<<<<<<<<<<<Md5>>>>>>>>>>>>>>>>> " , "blue"))

hashjob = hashlib.md5()
hashjob.update(karakterGirin.encode())
print(colored(hashjob.hexdigest(),"green")) 

#Sha1
print(colored("    <<<<<<<<<<<<<<<<<<Sha1>>>>>>>>>>>>>>>>> " , "red"))

hashjob = hashlib.sha1()
hashjob.update(karakterGirin.encode())
print(colored(hashjob.hexdigest(),"green")) 
##
print(colored("    <<<<<<<<<<<<<<<<<<Sha256>>>>>>>>>>>>>>>>> " , "blue"))

hashjob = hashlib.sha256()
hashjob.update(karakterGirin.encode())
print(colored(hashjob.hexdigest(),"green")) 
#
print(colored("    <<<<<<<<<<<<<<<<<<Sha 512>>>>>>>>>>>>>>>>> " , "white"))

hashjob = hashlib.sha512()
hashjob.update(karakterGirin.encode())
print(colored(hashjob.hexdigest(),"green")) 


