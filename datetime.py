import datetime
now = datetime.datetime.now()
period = now.hour
if period>=00 and period < 12:
    print("Good Morning")
elif period>=12 and period <17 :
    print("good afternoon")
elif period>=17 and period <20 :
    print("Good evening")
elif period>=20 and period <=24:
    print("good night")
