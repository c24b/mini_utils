import datetime

def check_format(value, format=None):
	if format is None:
		try:
			date = int(value)
			return True
		except ValueError:
			return False
	else:
		try:
			date = datetime.datetime.strptime(value,str("%"+format))
			return True
		except ValueError:
			try:
				date =  datetime.datetime.strptime(value,str("%"+format.lower()))
				return True
			except ValueError:	 
				return False
			except Exception, e:
				return False
