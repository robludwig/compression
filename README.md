compression
===========

Reddit Programming Challenge #162-4

This is a quick solution to the three Reddit programming challenge problems pertaining to
compression, starting with the one linked here:
http://www.reddit.com/r/dailyprogrammer/comments/25clki/5122014_challenge_162_easy_novel_compression_pt_1/
which is solved in decompress.py

followed by the intermediate challenge at
http://www.reddit.com/r/dailyprogrammer/comments/25hlo9/5142014_challenge_162_intermediate_novel/
which has its solution in compress.py

Both of these programs take a single line of input and can be invoked as python [de]compress.py filename.txt
to compress or decompress a file.


The final challenge, linked at 
http://www.reddit.com/r/dailyprogrammer/comments/25o2bd/5162014_challenge_162_hard_novel_compression_pt_3/
requires simply packaging up everything in a command line program, which I've added here as compressor.py

The final program can be run using compressor.py [-c | -d] input.txt output.txt
