# imports

class Librarian(object):

	def __init__(self, word_to_lookup):
		self.word_to_lookup = word_to_lookup
		self.baseURL = ''
		self.query = ''
		self.reference_links = ''

	def create_query():
		'''
		Creates query URL based on baseURL and word_to_lookup
		Input: None
		Output: None
		'''
		pass

	def get_reference_links(self):
		'''
		Gets all the links to check. I.e. first 30 on Google
		Input: None
		Output: list of reference links as strings
		'''
		pass

	def get_reference_content(self):
		'''
		Gets content from reference links. Good time for
		Input: None
		Output: List of content as strings
		'''
		pass

	def get_usages(self):
		'''
		Extracts usages
		Input: None
		Output: List of usages as strings (generator?)
		'''
		pass