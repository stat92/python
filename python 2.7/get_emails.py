emails = [{'from': 'bmstu@gmail.com', 'title': 'Title1', 'important': False},
		  {'from': 'bmstu2@gmail.com', 'title': 'Title2', 'important': True},
		  {'from': 'bmstu@gmail.com', 'title': 'Title3', 'important': False},
		  {'from': 'bmstu2@gmail.com', 'title': 'Title4', 'important': False},
		  {'from': 'bmstu@gmail.com', 'title': 'Title5', 'important': False},
		  {'from': 'bmstu1@gmail.com', 'title': 'Title6', 'important': True}]


def get_sorted(arr):
	emails = sorted(arr, key=lambda e: e['from'])
	before = ''

	for email in emails:
		
		if email['from'] != before:
			print email['from']
		
		if email['important']: 
			print '     [!]', email['title']
		else: 
			print '    ',email['title']
		
		before = email['from']

get_sorted(emails)

