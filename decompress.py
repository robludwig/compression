import sys
'''
Quick program to solve reddit challenge 162.
Store the entirety of the input in a text file, then call decompress.py input.txt to
decompress the file and output it to the screen
'''



def parse_input(input_list):
	dictionary_size = int(input_list[0])
	dictionary_entries = input_list[1:dictionary_size + 1]
	compressed_data = input_list[dictionary_size + 1:]
	return dictionary_entries, compressed_data

def decompress_symbol(symbol, dictionary, delimiter):
	numeric_symbol = "".join([digit for digit in symbol if digit.isdigit()])
	if not delimiter:
		delimiter = ""
	#print "symbol was %s and numeric_symbol was %s, delimiter is \"%s\"" % ( symbol, numeric_symbol, delimiter)
	#handle the non-numeric stuff separately
	if not numeric_symbol:
		#sys.stdout.write( delimiter )
		#print "non-numeric symbol \"%s\" and lowercase " % symbol, symbol.lower()
		if symbol.lower() == 'r':
			return '\n'
		elif symbol.lower() == 'e':
			sys.stdout.write( delimiter )
			return None #end of file...
		elif symbol == '-':
			return '-'
		else: #any other punctuation etc.
			sys.stdout.write(symbol)
			return ""
		return
	#handle the numeric symbols now, first by handling the numeric part, then the postfix
	else:
		#print( "numeric symbol (with optional suffix?) %s " % symbol
		word = dictionary[int(numeric_symbol)].lower()
		if symbol.endswith("!"):
			word = word.upper()
		elif symbol.endswith("^"):
			word = word.capitalize()
		#print ( "word without delimiter \"%s\"" % word
		sys.stdout.write( delimiter + word)
		return " "
		
			
if __name__ == "__main__":
	inputfile = open(sys.argv[1]).readlines()
	dictionary, data = parse_input(inputfile)
	clean_dictionary = []
	for word in dictionary:
		clean_dictionary.append(word.lower().strip())
	for line in data:
		symbols = line.split(" ")
		delimiter = ""
		for symbol in symbols:
			delimiter = decompress_symbol(symbol.strip(), clean_dictionary, delimiter)
		sys.stdout.write ("\n")

	
