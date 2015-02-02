import urllib2, urllib
header = {"X-TechChallenge" : 'true'}
val = {"test" : 'c'}
data = urllib.urlencode(val)
req = urllib2.Request('http://2014.fallchallenge.org',data,header)
response = urllib2.urlopen(req)
the_page = response.read()
with open("code.gz", "wb") as code:
	code.write(the_page)