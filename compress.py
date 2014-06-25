import sys

def compress(text):
	dictionary = []
	data = []
	compressed_data = ""
	
	return dictionary, compressed_data
	
	
if __name__ == "__main__":
	inputtext = open(sys.argv[1]).read()
	dictionary, compressed_data = compress(inputtext)
	print len(dictionary),
	for word in dictionary:
		print word
	print compressed_data