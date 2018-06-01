from sanatize import *

'''
	Encode
	
	Take in user file names for the ouput and input files,
	then enocde text using the run algorithim
'''

def	encode(inputFile, outputFile):
	normalText = 0
	totalBuffer = ""
	
	fileIn  = open(inputFile, "r")
	fileOut = open(outputFile,"w") 
	
	fileIn.flush()
	fileOut.flush()

	#Check if text is valid
	if(not(checkEncoding(inputFile))):
		print("ERROR: File contains invalid characters")
		return
		
	print("\nEncoding in progress ...")
	#Encode each line while adding into the output file
	buffer = ""
	tempChar = ""
	for line in fileIn:
		run = 0
		index = 0
		
		#Check for one character
		if(len(line) == 1 and line != " "):
			totalBuffer += line
			fileOut.write("1" + line)
			normalText += 1
		elif(line):
			for char in line:
				index += 1
				run += 1
				normalText += 1
				if(index >= len(line)):
					#Last character
					if(line[index - 1] == "\n"):
						normalText -= 1
						break
					buffer += str(run) + char
					run = 0
				elif(char != line[index]):
					buffer += str(run) + char
					run = 0
			totalBuffer += buffer
			fileOut.write(buffer + "\n")
			buffer = ""
	
	fileIn.close()
	fileOut.close()
	
	"Note compression ratio does not include new line characters"
	print("Encoding completed ...") 
	print("Compression Ratio: " + str(normalText) + "/" + str(len(totalBuffer))) 

'''
	Decode
	
	Take in user file names for the ouput and input files,
	then decode text using the run algorithim
'''

def	decode(inputFile, outputFile):
	#Check if decoding scheme is valid
	if(not(checkDecoding(inputFile))):
		return
	
	fileIn  = open(inputFile, "r")
	fileOut = open(outputFile,"w")
	 
	print("\nDecoding in progress ...")
	
	count = 0
	buffer = ""
	
	fileIn.flush()
	fileOut.flush()
	
	for line in fileIn:
		i = 0
		for char in line:
			if(char == "\n"):
				buffer += "\n"
				count -= 1
			elif((count % 2 == 0 and count > 1) or count == 0):
				#check for last character
				while(i < int(char)):
					buffer += line[count + 1]
					i += 1 
				i = 0
			count += 1
			fileOut.write(buffer)
			buffer = ""
		count = 0
	
			
	print("Decoding completed ...") 	