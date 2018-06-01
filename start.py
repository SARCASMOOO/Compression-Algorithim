
from helper import *

def menu():
	while True:
		print("#1. Encode a File \n#2. Decode a File \n#3. Exit")
		option = input()
		if(option == "1"):
			print("Input Source Filepath: ")
			source = input()
			print("\nInput Destination Filepath:")
			dest = input()
			encode(source, dest)
		elif(option == "2"):
			print("Input Source Filepath: ")
			filePath = input()
			print("\nInput Destination Filepath:")
			destPath = input()
			decode(filePath, destPath)
		elif(option == "3"):
			exit()
		else:
			print("Invalid entry..\n")

menu()

