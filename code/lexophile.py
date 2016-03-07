# Import word2vec class
import word2vec


# What's the class that I want to extend?
class Lexophile(word2vec_model_object):

	# Anything to init?
	def __init__(self):
		pass

	# These might already exist
	def load_model(self, filename):
		pass

	def save_model(self, filename):
		pass

	def is_present(self, word):
		'''
		Checks if a word is in the model, i.e. is known.
		Input: word
		Output: boolean
		'''
		pass

	def create_librarian(self, word):
		'''
		Creates a Librarian object
		Input: unknown word
		Output: Librarian object
		'''
		pass

	def dispatch_libarian(self, librarian):
		'''
		Starts a Librarian object and gets its results, i.e. a list of strings
		Input: Librarian object
		Output: Librarian's results as phrase_generator
		'''
		pass

	def learn_word(self, phrase_generator):
		'''
		Learns a new words
		Input: phrase generator object
		Output: none or should it return something so that we can dismiss
		the librarian?
		'''
		pass

	'''
	Probably want some testing functions, plus things to use the model, or not
	since it extends word2vec model object