from datetime import datetime
import pytz

german_tz = pytz.timezone('Europe/Berlin')
indian_tz = pytz.timezone('Asia/Kolkata')
us_tz = pytz.timezone('US/Eastern')


def convert_to_indian_time(german_time_str):

    german_time = datetime.strptime(german_time_str, '%Y-%m-%d %H:%M')
    german_time = german_tz.localize(german_time)

    indian_time = german_time.astimezone(indian_tz)
    return indian_time.strftime('%Y-%m-%d %H:%M')

def convert_to_us_time(german_time_str):

    german_time = datetime.strptime(german_time_str, '%Y-%m-%d %H:%M')
    german_time = german_tz.localize(german_time)

    indian_time = german_time.astimezone(us_tz)
    return indian_time.strftime('%Y-%m-%d %H:%M')

def convert_to_german_time(indian_time_str):

    indian_time = datetime.strptime(indian_time_str, '%Y-%m-%d %H:%M')
    indian_time = indian_tz.localize(indian_time)

    german_time = indian_time.astimezone(german_tz)
    return german_time.strftime('%Y-%m-%d %H:%M')


print(convert_to_indian_time('2025-05-15 18:57'))
print(convert_to_german_time('2025-05-15 22:29'))

print(convert_to_us_time('2025-05-15 19:04'))