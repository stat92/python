def show_audios(list_of_audios):

	for (numb, audio) in enumerate(list_of_audios):
		print '%s. %s - %s' % (numb+1, audio['artist'], audio['title'])


def count_artists(list_of_audios):

	artists = {}

	for audio in list_of_audios:

		for artist in artists.keys():
			if audio['artist'] == artist:
				artists[artist] += 1	
				break	
		else:
			artists[audio['artist']] = 1

	return artists


def test_count_artists(func, right_artists):

	artists = func

	for artist in right_artists.keys():
		if right_artists[artist] != artists[artist]:
			print 'It\'s bad'
			break
	else:
		print 'It\'s OK'



audios = [{'artist': 'Queen', 'title': 'We are the champions'},
		  {'artist': 'Queen', 'title': 'Rock'},
		  {'artist': 'M.Jackson', 'title': 'Beat It'}]

right_artists = {'M.Jackson': 1, 'Queen': 2}


show_audios(audios)
print count_artists(audios)
test_count_artists(count_artists(audios),right_artists)