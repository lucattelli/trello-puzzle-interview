#!/usr/bin/env python
# Trello Internal Software Developer Puzzle
# By Bruno Lucattelli - bruno@lucattelli.com
# PS: I got Python questions that got answered by StackOverflow :)
#
# usage: revhash.py [options] [args]
# Options and arguments
# -? : help (this dialog)
# -a : the valid alphabet to be considered
# -h : the desired hash you want to reverse

import sys, getopt

# default help dialog
def print_help():
	print "Trello Internal Software Developer Puzzle"
	print "By Bruno Lucattelli - bruno@lucattelli.com"
	print "usage: revhash.py [options] [args]"
	print "Options and arguments"
	print "-? : help (this dialog)"
	print "-a : the valid alphabet to be considered"
	print "-h : the desired hash you want to reverse"
	sys.exit(2)

# handles the user parameters and return a key:value list of them
def handle_parameters():
	try:
		options, arguments = getopt.getopt(sys.argv[1:], "a:h:?")
	except getopt.GetoptError:
		print "\033[91m" + "Invalid arguments!" +  "\033[0m"
		print_help()		
	params = {}
	for opt, arg in options:
		if opt == "-a":
			params["alphabet"] = str(arg)
		elif opt == "-h":
			params["hash"] = str(arg)
		elif opt == "-?":
			params["help"] = str(arg)
	return params

# calculates individual hashes
def hash(s, hash_alphabet):
	h = 7
	letters = hash_alphabet
	i = 0
	while i < len(s):
		h = h * 37 + letters.index(s[i])
		i = i + 1
	return h

# determine keyword by hash number
def reverse_hash(desired_hash, hash_alphabet):
	string_length = 0
	while string_length < 100:
		dictionary = hash_alphabet
		dictionary_index = len(dictionary) - 1
		string_prefix = ""
		last_string = ""
		while dictionary_index >= 0:
			test_string = string_prefix + dictionary[dictionary_index]
			while len(test_string) < string_length:
				test_string = test_string + dictionary[len(dictionary) - 1]
			test_hash = hash(test_string, hash_alphabet)
			if test_hash == desired_hash: # yay! \o/
				return test_string
			elif test_hash > desired_hash and dictionary_index > 0: # not yet what we wanted
				last_string = test_string
				dictionary_index = dictionary_index - 1
			elif last_string == "" and test_hash < desired_hash: #  word must be larger
				break
			else: # partially what we wanted
				if dictionary_index == 0: # prevents from breaking when "a" is the correct letter
					string_prefix = string_prefix + test_string[len(string_prefix)]
				else:
					string_prefix = string_prefix + last_string[len(string_prefix)]
				dictionary_index = 15
		string_length = string_length + 1

# make it executable
def main():
	parameters = handle_parameters()
	if "help" in parameters.keys():
		print_help()
	elif "hash" not in parameters.keys():
		print "\033[91m" + "Missing parameter: -h <hash>" + "\033[0m"
		print_help()
	elif "alphabet" not in parameters.keys():
		print "\033[91m" + "Missing parameter: -a <alphabet>" + "\033[0m"
		print_help()
	else:
		print "Your hash was reversed. The keyword is: " + "\033[92m" + str(reverse_hash(int(parameters["hash"]), str(parameters["alphabet"]))) + "\033[0m"

# execute!
if __name__ == "__main__":
	main()


# 01010100 01101000 01100001 01101110 01101011 00100000 01111001 01101111 01110101 00100001
# EOF @ 100 :)