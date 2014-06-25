import sys

def compress(text):
	dictionary = []
	data = []
	compressed_data = ""
	for line in text:
		for word in line.split(" "):
			#print "compressing \"%s\" " % word
			lowerword = word.lower().strip()
			if lowerword in dictionary:
				compressed_data += str(dictionary.index(lowerword))
			else:
				dictionary.append(lowerword)
				compressed_data += str(dictionary.index(lowerword))
			if word == word.upper():
				compressed_data += "!" #capitalize the whole word
			elif word.istitle():
				compressed_data += "^" #capitalize just the first letter
			compressed_data += " "
		compressed_data += 'R ' #newline after each line
	
	compressed_data += 'E ' #EOR
	return dictionary, compressed_data
	
	
if __name__ == "__main__":
	inputtext = open(sys.argv[1]).readlines()
	dictionary, compressed_data = compress(inputtext)
	print len(dictionary)
	for word in dictionary:
		print word
	print compressed_data