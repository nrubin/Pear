#let's play around with dates
import arrow
import calendar

class ScheduleItem(object):
	"""
	Represents a single appointment using a 
	begin datetime and a duration in minutes
	"""

	def __init__(self,start,duration):
		"""
		start can be any argument to arrow.get
		"""
		self.start = arrow.get(start)
		self.duration = duration
		self.refresh_times()

	def __repr__(self):
		return "Appointment from %s to %s" % (self.formatted_start,self.formatted_end)

	def refresh_times(self):
		self.end = arrow.get(self.start.timestamp + (self.duration *  60))
		self.formatted_start = self.start.format('YYYY-MM-DD HH:mm')
		self.formatted_end = self.end.format('YYYY-MM-DD HH:mm')

	def set_time(self,hour,minute):
		new_time = self.start.replace(hour=hour,minute=minute)
		self.start = new_time
		self.refresh_times()

def parse_timestamp_with_tz(app_time_utc_ms, tz_str):
	t = arrow.get(app_time_utc_ms).to(tz_str)
	return t

#generate all days between two times
def generate_days(start_date,end_date):
	"""
	Generates all dates between two dates (time on the days defaults to midnight)
	"""
	days = [ d[0] for d in arrow.Arrow.span_range('day',start_date,end_date)]
	return days

def filter_by_weekday(days,weekday_filter,exclude=False):
	"""
	filters a list of days by a weekday filter. days are new Arrow objects.	The weekday filter lists which days of the week (0-6) should be kept or removed.
	the exclude flag will remove all weekday matches, and defaults to false.
	"""
	filtered_days = []
	for day in days:
		if (day.weekday() in weekday_filter) ^ exclude:
			filtered_days.append(arrow.get(day))
	return filtered_days

def filter_by_blackout_dates(days,blackout_day_filter):
	blackout_date_filter_as_string = [blackout_day.format("YYYYMMDD") for blackout_day in blackout_day_filter]
	filtered_days = []
	for day in days:
		if (day.format("YYYYMMDD") not in blackout_date_filter_as_string):
			filtered_days.append(arrow.get(day))
	return filtered_days

def create_activity_schedule(range_start,range_end,start_hour,start_minute,duration,weekday_filter):
	"""
	Creates all schedule items given a schedule. Assumes US blackout dates.
	"""
	holidays = [arrow.get(2014,1,1),arrow.get(2014,2,14), arrow.get(2014,5,28), arrow.get(2014,12,25)]
	all_days_no_time = filter_by_blackout_dates(filter_by_weekday(generate_days(range_start,range_end),weekday_filter),holidays)
	schedule = []
	for day in all_days_no_time:
		sched_item = ScheduleItem(day,duration)
		sched_item.set_time(start_hour,start_minute)
		schedule.append(sched_item)
	return schedule

def get_nth_weekday_of_month(n,weekday,month,year):
	"""
	Gets the nth occurence of a weekday in a month
	if n = 0, it returns the last day of the month.
	if an nth weekday is not found, it returns None.
	"""
	weekday_of_first_of_month, days_in_month = calendar.monthrange(year,month)
	if n == 0:
		backwards_day = days_in_month
		day = arrow.get(year,month,backwards_day)
		while day.weekday() != weekday:
			day = arrow.get(year,month,backwards_day)
			backwards_day -= 1
		return day
	else:
		counter = 0 #we will iterate through the month
		first_day = arrow.get(year,month,1)
		last_day = arrow.get(year,month,days_in_month)
		for day_range in arrow.Arrow.span_range('day',first_day,last_day):
			day = day_range[0]
			if day.weekday() == weekday:
				counter += 1
				if counter == n:
					return day
		return None

def get_last_weekday_of_month(weekday,month,year):
	return get_nth_weekday_of_month(0,weekday,month,year)

if __name__ == '__main__':
	"""
	NOTE: MONDAY IS 0.
	"""
	#print parse_timestamp_with_tz(1399437480, "US/Eastern")
	start = arrow.get(2014,1,1)
	end = arrow.get(2014,1,19)
	#print create_activity_schedule(start,end,15,30,90,[2,4])
	print get_nth_weekday_of_month(1,5,2,2014)
	print get_last_weekday_of_month(5,2,2014)