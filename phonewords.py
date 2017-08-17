import itertools

# Dictionary words file from:
# http://www-01.sil.org/linguistics/wordlists/english/wordlist/wordsEn.txt
words_file = open("words.txt", "r")

# Phone number
phone = "2010043556"

# Dialpad where the index corresponds to the digit
dialpad = [[], [], ["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"],
			["j", "k", "l"], ["m", "n", "o"], ["p", "q", "r", "s"],
			["t", "u", "v"], ["w", "x", "y", "z"]]

# Returns a sorted list of all subphrases in a given phrase: abc => [a, ab, abc, b, bc, c]
def get_subphrases(phrase):
	subphrases = set()
	for i in range(0, len(phrase)):
		nums = 1
		for j in range(i, len(phrase)):
			subphrases.add(phrase[i:i+nums])
			nums += 1
	return sorted(list(subphrases))

# Translates a given list of phrases into a dictionary of the digits turned into character sequences.
# The key of the dictionary is the word and the value is always True.
# A dictionary was chosen for the sake of much quicker checks to see if a key is in a dictionary.
# This is because searching a list for a key was found to be much slower.
# Returns the dictionary
def translate_phrases(phrases):
	translations = {}
	for phrase in phrases:
		char_lists = []
		for digit in phrase:
			char_lists.append(dialpad[int(digit)])
		combos = list(itertools.product(*char_lists))
		for combo in combos:
			combine = ""
			for char in combo:
				combine += char
			translations[combine] = True
	return translations

# Returns a list of words that exist in the word file
def get_dialpad_words(translations):
	results = []
	for word in words_file:
		w = word.strip("\n")
		try:
			index = translations[w]
		except KeyError:
			continue
		results.append(w)
	return sorted(results)

# Embeds the word into the phone number
# Returns a dictionary where the key is the word and the value is the embedded phone number
def insert_into_phone(words):
	numbers = {}
	for w in words:
		word_digits = ""
		for char in w:
			for digits in range(0, len(dialpad)):
				try:
					index = dialpad[digits].index(char)
				except ValueError:
					continue
				word_digits += str(digits)
		numbers[w] = phone.replace(word_digits, w)
	return numbers

sp = get_subphrases(phone)
# print sp
tp = translate_phrases(sp)
# print tp
cd = get_dialpad_words(tp)
# print cd
iip = insert_into_phone(cd)
print iip