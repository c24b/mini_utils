def cookies_converter(cookies):	
	'''self-made method to store cookies from spynner(Netscape TXT) and send it to python-requests (dict) formats'''
	cookies_dict = {}
	for l in re.split("\n",cookies)[2:]:
		domain = re.split("\t", l)[0]
		cookies_dict[re.split("\t", l)[5]] = re.sub("\"", "", re.split("\t", l)[6])
	return cookies_dict
