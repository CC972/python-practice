import datetime


DAYS_IN_YEAR = 365.25

input_birthdays = [
    '1963-05-25',
    '1961-04-03',
    '1972-08-30',
    '1945-10-19',
    '1996-11-23',
    '1933-10-25',
    '1952-11-03',
    '1975-09-23',
]

number_of_birthdays = len(input_birthdays)

birthdays = [datetime.date.fromisoformat(birthday) for birthday in input_birthdays]

epoch_datetime = datetime.datetime.utcfromtimestamp(0)
epoch_date = datetime.datetime.utcfromtimestamp(0).date()

birthdays_in_milliseconds_since_epoch = [datetime.timedelta(milliseconds=(birthday - epoch_date).total_seconds() * 1000)
                                         for birthday in birthdays]

birthdays_in_milliseconds_total = datetime.timedelta(0)
for delta in birthdays_in_milliseconds_since_epoch:
    birthdays_in_milliseconds_total += delta

birthday_mean = datetime.datetime.utcfromtimestamp(0) + (birthdays_in_milliseconds_total / number_of_birthdays)

sorted_birthdays_in_milliseconds_since_epoch = sorted(birthdays_in_milliseconds_since_epoch)

median_index = int(number_of_birthdays / 2)
if number_of_birthdays % 2 == 0:
    birthday_median = epoch_datetime + (sorted_birthdays_in_milliseconds_since_epoch[median_index - 1] +
                                        sorted_birthdays_in_milliseconds_since_epoch[median_index]) / 2
else:
    birthday_median = sorted_birthdays_in_milliseconds_since_epoch[median_index]


birthday_range = max(birthdays_in_milliseconds_since_epoch) - min(birthdays_in_milliseconds_since_epoch)

average_age = int((datetime.datetime.today() - birthday_mean).days / DAYS_IN_YEAR)

print(f"Mean of birthdays: {birthday_mean}")
print(f"Median of birthdays: {birthday_median}")
print(f"Range of birthdays: {birthday_range}")
print(f"Average age: {average_age} years")
