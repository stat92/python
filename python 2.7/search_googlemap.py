#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 1 - search2.py

import urllib, urllib2, json


params = {'address': 'Yeltay Atyrau kazakhstan', 'oe': 'utf8'}
url = 'http://maps.googleapis.com/maps/api/geocode/json?' + urllib.urlencode(params)

rawreply = urllib2.urlopen(url).read()

reply = json.loads(rawreply)

print reply['results'][0]['geometry']['location']
