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

def check_month(month):	
	month = month.capitalize()
	try:
		return datetime.datetime.strptime(month, r"%b")
	except ValueError:
		try:
			return datetime.datetime.strptime(month, r"%B")
		except ValueError:
			return False

def check_year(year):	
	try:
		if len(year) == 4:
			return datetime.datetime.strptime(year,"%Y")
		else:
			return datetime.datetime.strptime(year,"%y")
	except ValueError:
		try:
			return datetime.datetime.strptime(year, r"%y"))
		except ValueError:
			try:
				return year.is_digit()
			except ValueError:
				return False

def check_dow(dow):
	try:
		return datetime.datetime.strptime(dow,"%a")
		except ValueError:
			try:
				return datetime.datetime.strptime(dow, r"%A"))
			except ValueError:
				if dow.is_digit():
					return False
				else:
					return True
				

def check_format(value, format="A"):
	if format is None:
		return value.is_digit()
	else:
		try:
			return datetime.datetime.strptime(value,str("%"+format))
		except ValueError:
			return datetime.datetime.strptime(value,str("%"+format.lower()))
