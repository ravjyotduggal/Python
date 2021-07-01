import datetime
import pytz

while True:
    country = {

        1: "US/Alaska",
        2: "Singapore",
        3: "Pacific/Midway",
        4: "Mexico/General",
        5: "Europe/Warsaw",
        6: "Europe/Saratov",
        7: "Brazil/DeNoronha",
        8: "Australia/Victoria",
        9: "Asia/Kolkata",
        0: "Exit"
    }

    for x in country:
        print(x, country[x])
    choice = int(input("Please choose any 1 country: "))
    if choice != 0:
        print(country[choice])
        time_zone = pytz.timezone(country[choice])
        local_time = datetime.datetime.now(tz=time_zone)
        print("Local time is {}".format(local_time.strftime('%A %x %X %z')))
        print("UTC time is {}".format(local_time.utcnow()))
        print("Time zone is {}".format(local_time.tzname()))
    else:
        break


