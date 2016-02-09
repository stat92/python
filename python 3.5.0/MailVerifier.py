import re


class MailVerifier (object):


	def verify_full_email (self, email):

		splitted_email = self.split_email(email)

		if splitted_email: name, domain = splitted_email
		else: return 0

		if self.verify_name(name) and self.verify_domain(domain): return 1
		else: return 0


	def split_email (self, email):

		# Checking an amount of @-symbol before splitting
		if len( re.findall(r'@', email) ) != 1: return 0

		# If there is only one @-symbol in email, split it
		return email.split('@')


	def verify_domain (self, domain):

		# Length of the domain must be less than 256 & more than 3
		if len(domain) > 256 or len(domain) < 3: return 0
			 
		# Domain is wrong
		if re.match(r'^[^a-z\d_].*|.*[^-a-z\d_.].*|.*\.-.*|.*-\..*|.*[^a-z\d_]$', domain): 
			return 0

		# Domain is correct
		return 1


	def verify_name (self, name):

		# Length of the name must be less than 128
		if len(name) > 128 or len(name) < 1: return 0	

		# Name must consist only a-z0-9"._- symbols & no double points (..)
		if re.match(r'.*[^-a-z\d"_.!:,].*|.*\.\..*', name): return 0	
	 	
	 	# Only paired quotes " "	
		if len( re.findall(r'"', name) ) % 2 != 0: return 0

		# Symbols !,: must be between quotes " "	
		for (prev, after) in re.findall(r'(.)?(?:[!:,])(.)?', name):
			if prev != '"' or after != '"': return 0

		# Name is correct
		return 1
