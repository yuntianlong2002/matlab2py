import datetime
import numpy

def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)  # this will never fail
    return next_month - datetime.timedelta(days=next_month.day)

def generate_next_x_months(month_need, start_date_str):
	dates = []
	start_date = datetime.datetime.strptime(start_date_str, '%Y/%m/%d').date()
	year = start_date.year
	month = start_date.month
	while month_need>=0:
		if month>=13:
			month = 1
			year = year + 1 # flip to the next year
		dates.append(last_day_of_month(datetime.date(year, month, 1)).strftime('%Y/%m/%d'))
		month+=1
		month_need-=1 # keep generating end of month date until this variable 0 
	return dates

		
