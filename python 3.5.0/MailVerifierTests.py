import unittest # Upload the unittest library if you need
from MailVerifier import MailVerifier



class SimpleTestCase(unittest.TestCase):

	def setUp(self):
		self.mv = MailVerifier()

	def tearDown(self):
		del self.mv

	def test_verify_full_email(self):
		msg = "Correct email found as wrong in verify_full_email()"
		self.assertEqual(self.mv.verify_full_email('makhambet@web.com.kz'), 1, msg)


	def test_split_email(self):	
		arguments = [ ('makhambet@web.com.kz', ['makhambet', 'web.com.kz'], "split_email() don't split correctly" ),
			          ('makha@web@kz',         0,             "split_email() haven't revealed an incorrect email" ) ]

		for ( sample, res, msg ) in arguments:
			self.assertEqual( self.mv.split_email(sample), res, msg )


	def test_verify_domain(self):
		arguments = [ ('web.com_9.k-z', 1, "verify_domain() returned incorrect answer"),
			          ('we',            0, "verify_domain() must reveal domain less than 3"),
			          ('w' * 257,       0, "verify_domain() must reveal domain more than 256") ]

		for ( sample, res, msg ) in arguments:
			self.assertEqual( self.mv.verify_domain(sample), res, msg )


	def test_verify_name(self):
		arguments = [ ('ma","":""!"kha.a-92', 1, "verify_name() returned incorrect answer"), 
		              ( ' ',                  0, "verify_name() must reveal name less than 1" ), 
		              ( 'm' * 129,            0, "verify_name() must reveal name more than 128" ) ]

		for ( sample, res, msg ) in arguments:
			self.assertEqual( self.mv.verify_name(sample), res, msg )



if __name__ == "__main__":
	unittest.main()
