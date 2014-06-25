import sys
from argparse import ArgumentParser, FileType

from compress import compress
from decompress import decompress

if __name__ == "__main__":
	parser = ArgumentParser(description = "Compress or decompress a file using a simple dictionary method.")
	
	#could make better use of argparse to load the arguments as files directly
	group = parser.add_mutually_exclusive_group(required = True)
	group.add_argument("-d")
	group.add_argument("-c")
	parser.add_argument("output", nargs=1)
	
	args = parser.parse_args()
	
	
	outputfile = open(args.output[0], 'w')
	if args.c:
		inputfile = args.c
		compress_this = open(inputfile.readlines())
		outtext = compress(compress_this)
	elif args.d:
		inputfile = args.d
		decompress_this = compress_this = open(inputfile.readlines())
		outtext = decompress(decompress_this)
	
	outputfile.write(outtext)
	outputfile.close()
	
	