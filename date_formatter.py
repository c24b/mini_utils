import re
import datetime
from collections import OrderedDict, namedtuple

def strp_time_xpr(date_list):
	if len(date_list) < 8:
		return date_list
	else:
		d_xpr = OrderedDict()
		d_xpr["dow"] ="a"
		d_xpr["day"]= "d" 
		d_xpr["month"]= "b"
		d_xpr["year"]= "y" 
		d_xpr["hour"]= "H" 
		d_xpr["min"]= "M"
		d_xpr["sec"]= "S"
		#d_xpr["tz"] = "z"
		
		dow, day, month, year, hour, min, sec, tz = date_list
				
		
		if tz == 2 and tz in ["AM", "PM"]:
			#tz format is %p
			d_xpr['tz'] = "p"
			# hour format is %I
			#d_xpr['hour'] = "%I"
		elif len(tz) == 3:
			d_xpr['tz'] = d_xpr['tz'].upper()
		elif len(tz) >= 4:
			tz = "+"+tz
			d_xpr['tz'] = d_xpr['tz'].lower()
		
		elif tz.startswith("+"):
			d_xpr['tz'] = d_xpr['tz'].lower()
		elif tz.startswith("-"):
			d_xpr['tz'] = d_xpr['tz'].lower()
		else:
			pass
			#del date_list[-1]
			#del d_xpr['tz']
			#d_xpr['tz'] = "%"
				#~ #format will be %%
				
		#month
		if len(month) > 3:
			d_xpr["month"] = d_xpr['month'].upper()
			
		if len(year) > 2:
			d_xpr['year'] = d_xpr['year'].upper()
			
		return [str("%"+n) for n in d_xpr.values()]


def check_gmt(value):
	#['Fri', '17', 'Apr', '92', '11', '42+0000']
	r_utc = re.compile("^(?P<ms>\d{2})?(?P<utc>.\d{4})$")
	value = re.sub("\(|\)","", value)
	
	if len(value) == 3:
		utc = value
		sec = "00"
		f = "gmt"
		return [sec, utc]
		
	elif len(value) == 2 and value.isdigit():
		sec = value
		utc = "0000"
		f = "utc"
		return [sec, utc]
	else:
		m = re.match(r_utc, value)
		if m is not None:
			sec = m.group('ms')
			utc = m.group('utc')
			f = "utc"
			if sec is None:
				sec = "00"
		else:
			sec = "00"
			utc="0000"
		return [sec, utc]

def format_timelist(liste):
	'''check a list and transform it to a date format named tuple '''
	if liste[0].isdigit():
		liste.insert(0, "Sun")
	
	if len(liste) < 6:
		return liste
		
	if len(liste) == 6:
		utc = check_gmt(liste[-1])
		del liste[-1]
		liste.extend(utc)
		liste.append("+0000")
		#print len(liste)
	elif len(liste) == 7:
		utc = check_gmt(liste[-1])
		del liste[-1]
		liste.extend(utc)
		
	elif len(liste) == 8:
		utc = check_gmt(liste[-1])
		del liste[-1]
		del liste[-1]
		liste.extend(utc)
		
	else:
		if len(liste[-2]) == 4:
			liste[-2] = "+"+liste[-2]
		liste[-1] = re.sub("\(|\)","", liste[-1])
		
	return liste[0:7]	
	#dow, day, month, year, hour, min, sec, tz = date_list[0:7]		
		
def format_date(date_list):
	date_list = format_timelist(date_list)
	date_str =  "-".join(date_list)
	#~ xpr = "-".join(strp_time_xpr(date_list))
	#~ try:
		#~ #datetime.strptime(date_string, format)
		#~ return datetime.datetime.strptime(date_str, xpr)
	#~ except ValueError as err:
		#~ print err
	return date_str
	
