from datetime import datetime
import time

def fractionateYear(date):
	def sinceEpoch(date): # returns seconds since epoch
		return time.mktime(date.timetuple())
	s = sinceEpoch
	year=date.year
	start_of_year=datetime(day=1,month=1,year=year)
	start_of_next_year=datetime(day=1,month=1,year=year+1)
	year_elapsed = s(date) - s (start_of_year)
	year_duration = s(start_of_next_year) - s(start_of_year)
	fraction = year_elapsed/year_duration
	return date.year + fraction

#usage
#fractionateYear(datetime.strptime('18/11/2013','%d/%m/%Y'))  


