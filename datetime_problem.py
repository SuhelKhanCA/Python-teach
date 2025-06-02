from datetime import datetime, timedelta
now = datetime.now()

print("German time: ", now.strftime("%H:%M"))

india_time = now + timedelta(hours=3, minutes=30)
print("Indian time: ", india_time.strftime("%H:%M"))


from datetime import datetime
import pytz

german_tz = pytz.timezone('Europe/Berlin')
indian_tz = pytz.timezone('Asia/Kolkata')

german_time = datetime.strptime('2025-05-23 16:13', '%Y-%m-%d %H:%M')

german_time = german_tz.localize(german_time)

indian_time = german_time.astimezone(indian_tz)
print(indian_time)