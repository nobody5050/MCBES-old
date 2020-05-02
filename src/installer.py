# this file is part of the mcbes project
#   _  _   ___  ____  ____      ____ 
#  ( \/ ) / __)(  _ \(  __)___ / ___)
#  / \/ \( (__  ) _ ( ) _)(___)\___ \
#  \_)(_/ \___)(____/(____)    (____/

#MCBES Installer
#runs on first boot

import os

print(" ")
print("Welcome to MCBES Proxy Server ! You're about to setup the server!")
print(" ")
if not os.path.exists('/config_files/config.py'):
    os.mknod('/config_files/config.py')
    install = true

while install = true:
  servername = input("Please put in your mcpe server name: ")
  print('You picked', servername)
  print("	")
  
f = open("/config_files/config.py", "a")
f.write(servername, "= true")
f.close()

print('Setup complete!')
#THIS FILE IS A REMNANT OF WHERE I FORKED THIS FROM. EVENTUALLY IT WILL BE MERGED TO ANOTHER FILE.
