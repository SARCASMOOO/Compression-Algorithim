'''
	checkEncoding
	
	Take in user input file name,
	then check text to be valid for encoding
'''

def checkEncoding(fileName):
	#Check if file is valid
	try:
		file  = open(fileName, "r")
	except:
		print("Invalid file\n")
		return False
		
	file.flush()
	#Check if all characters are valid
	check = True
	unsuported = ""
	badCharacters = {'!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '"', "'", "{", "[", "]", "}", "|", ";", ":", "<", ",", ">", ".", "/", "?"}
	for line in file:
		for char in line:
			if(char in badCharacters):
				check = False
				unsuported += ", " + char
	if(check == False):
		print("ERROR: Unsoported characters found\n")
		print(unsuported)
	file.close()
	return check

'''
	checkDecoding
	
	Take in user input file name,
	then check encoded text for proper encoding before decoding
'''

def checkDecoding(fileName):
	#Check if file is valid
	try:
		file = open(fileName, "r")
	except:
		print("Invalid file\n")
		return False
		
	file.flush()
	#Check if all characters are valid
	check = True
	count = 0
	badCharacters = {'!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '"', "'", "{", "[", "]", "}", "|", ";", ":", "<", ",", ">", ".", "/", "?"}
		
	file.flush()
	
	for line in file:
		i = 0
		for char in line:
			if(char == "\n"):
				buffer += "\n"
				count -= 1
			elif((count % 2 == 0 and count > 1) or count == 0):
				#check for invalid scheme
				#If valid only numbers should come here
				try:
					int(char)
				except:
					#Expected int was not found
					print("ERROR: expected run was not found\n")
					return False
			else:
				#Check for bad characters
				if(char in badCharacters):
					print("ERROR: Unsuported characters found\n")
					return False
			count += 1
		count = 0
	
	file.close()
	return True