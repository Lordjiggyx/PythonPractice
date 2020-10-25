#Dates

"Python does not have a date type instead you can use the datetime module to work with dates as date objects"

import datetime

x = datetime.datetime.now()
print(x)

"To creaate a date object we can use the datetime calss from the module"
date = datetime.datetime(2020,10,25)
print(date)

"the datetime class can take in year month day , hour minute second microsecond and timezone"

"The datetime object has a method for formatting its called the strftime method it takes in one parameter to specify the format of the rerurned string"

"""
%a	Weekday, short version	Wed	
%A	Weekday, full version	Wednesday	
%w	Weekday as a number 0-6, 0 is Sunday	3	
%d	Day of month 01-31	31	
%b	Month name, short version	Dec	
%B	Month name, full version	December	
%m	Month as a number 01-12	12	
%y	Year, short version, without century	18	
%Y	Year, full version	2018	
%H	Hour 00-23	17	
%I	Hour 00-12	05	
%p	AM/PM	PM	
%M	Minute 00-59	41	
%S	Second 00-59	08	
%f	Microsecond 000000-999999	548513	
%z	UTC offset	+0100	
%Z	Timezone	CST	
%j	Day number of year 001-366	365	
%U	Week number of year, Sunday as the first day of week, 00-53	52	
%W	Week number of year, Monday as the first day of week, 00-53	52	
%c	Local version of date and time	Mon Dec 31 17:41:00 2018	
%x	Local version of date	12/31/18	
%X	Local version of time	17:41:00	
%%	A % character	%

"""