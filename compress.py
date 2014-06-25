import sys
'''
Quick program to solve reddit challenge 163.
Store the entirety of the input in a text file, then call compress.py input.txt to
compress the file and output the compressed contents to the screen
'''

VALID_PUNCTUATION = [ '.', ',', '?', '!', ';', ':']

def compress(text):
	dictionary = []
	data = []
	compressed_data = ""
	for line in text:
		for word in line.split(" "):
			#print "compressing \"%s\" " % word
			lowerword = word.lower().strip()
			
			#strip out the punctuation so we don't cheat on the compression
			raw_word = "".join([letter for letter in lowerword if letter.isalpha()])
			#print "lemmatized the word to %s " % raw_word
			
			#put it in the dictionary and get the index
			if raw_word in dictionary:
				compressed_data += str(dictionary.index(raw_word))
			else:
				dictionary.append(raw_word)
				compressed_data += str(dictionary.index(raw_word))
				
			#handle the capitalization...
			if word == word.upper():
				compressed_data += "!" #capitalize the whole word
			elif word.istitle():
				compressed_data += "^" #capitalize just the first letter
			
			#handle the punctuation... rules are you get one symbol per word
			for symbol in VALID_PUNCTUATION:
				if symbol in word:
					compressed_data += " " + symbol
					break #TODO: add error handling if you have more than one symbol...
			
			#add space and move on to the next thing...
			compressed_data += " "		
		compressed_data += 'R ' #newline after each line
	
	compressed_data += 'E ' #EOF
	return dictionary, compressed_data
	
	
if __name__ == "__main__":
	inputtext = open(sys.argv[1]).readlines()
	dictionary, compressed_data = compress(inputtext)
	print len(dictionary)
	for word in dictionary:
		print word
	print compressed_data