def hash(s):
	h = 7
	letters = "acdegilmnoprstuw"
	i = 0
	while i < len(s):
		h = h * 37 + letters.index(s[i])
		i = i + 1
	return h

def discover_string_by_hash(desired_hash):
	string_length = 0
	while string_length < 100:
		dictionary = "acdegilmnoprstuw"
		dictionary_index = len(dictionary) - 1
		string_prefix = ""
		last_string = ""
		while dictionary_index >= 0:
			test_string = string_prefix + dictionary[dictionary_index]
			while len(test_string) < string_length:
				test_string = test_string + dictionary[len(dictionary) - 1]
			test_hash = hash(test_string)
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

print discover_string_by_hash(930846109532517) # returns promenade
print discover_string_by_hash(680131659347) # returns leepadg